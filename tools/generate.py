#!/usr/bin/env python3
"""
Image Studio CLI — style-aware AI image generation.

Reads designer style profiles from design-library, builds enhanced prompts,
and generates images via HuggingFace Inference API or Google Gemini.

Usage:
    # List available styles
    uv run generate.py --list-styles

    # Prompt-only mode (no API key needed)
    uv run generate.py "cyberpunk city" --style ash-thorp --prompt-only

    # Generate with HuggingFace (needs HF_TOKEN env var)
    uv run generate.py "dark fantasy landscape" --style kilian-eng

    # Generate with Gemini (needs GEMINI_API_KEY env var)
    uv run generate.py "minimal book cover" --style kenya-hara --backend gemini

    # Mix styles
    uv run generate.py "festival poster" --style "ash-thorp+kilian-eng" --size 2K

Environment variables:
    HF_TOKEN          HuggingFace API token (for HF backend)
    GEMINI_API_KEY    Google Gemini API key (for Gemini backend)
"""

import argparse
import base64
import json
import os
import platform
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Add tools dir to path for prompt_builder import
sys.path.insert(0, str(Path(__file__).resolve().parent))
from prompt_builder import StyleLibrary, CinemaParams, _list_cinema_options
from presets import list_options as list_preset_options


LIBRARY_ROOT = Path(__file__).resolve().parent.parent
MY_WORKS_DIR = LIBRARY_ROOT / "my-works"

# HuggingFace defaults
HF_API_URL = "https://api-inference.huggingface.co/models"
HF_DEFAULT_MODEL = "black-forest-labs/FLUX.1-dev"

# Gemini defaults
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models"
GEMINI_DEFAULT_MODEL = "gemini-3-pro-image-preview"

SIZE_MAP = {
    "512": (512, 512),
    "1K": (1024, 1024),
    "2K": (2048, 2048),
    "landscape": (1344, 768),
    "portrait": (768, 1344),
    "wide": (1536, 640),
}


def detect_backend() -> str | None:
    """Auto-detect available backend from environment variables."""
    if os.environ.get("HF_TOKEN"):
        return "hf"
    if os.environ.get("GEMINI_API_KEY"):
        return "gemini"
    return None


def generate_hf(prompt: str, negative_prompt: str, model: str, width: int, height: int) -> bytes:
    """Generate image via HuggingFace Inference API. Returns PNG bytes."""
    token = os.environ["HF_TOKEN"]
    url = f"{HF_API_URL}/{model}"

    payload = {
        "inputs": prompt,
        "parameters": {
            "width": width,
            "height": height,
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
        },
    }
    if negative_prompt:
        payload["parameters"]["negative_prompt"] = negative_prompt

    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "image/png",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        print(f"HuggingFace API error (HTTP {e.code}): {error_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def generate_gemini(prompt: str, model: str, size: str) -> bytes:
    """Generate image via Gemini API. Returns PNG bytes."""
    api_key = os.environ["GEMINI_API_KEY"]
    url = f"{GEMINI_API_URL}/{model}:streamGenerateContent?key={api_key}"

    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE", "TEXT"],
            "imageConfig": {"image_size": size},
        },
    }

    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        print(f"Gemini API error (HTTP {e.code}): {error_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    # Extract image from streaming response
    candidates = data if isinstance(data, list) else [data]
    for candidate_wrapper in candidates:
        for candidate in candidate_wrapper.get("candidates", []):
            for part in candidate.get("content", {}).get("parts", []):
                if "inlineData" in part:
                    return base64.b64decode(part["inlineData"]["data"])

    print("Error: no image data in Gemini response", file=sys.stderr)
    sys.exit(1)


def make_output_dir(subject: str) -> Path:
    """Create a dated output directory in my-works/."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = subject.lower()[:40]
    slug = "".join(c if c.isalnum() or c in "-_ " else "" for c in slug)
    slug = slug.strip().replace(" ", "-")
    slug = slug or "untitled"

    out_dir = MY_WORKS_DIR / f"{date_str}-{slug}"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def save_metadata(out_dir: Path, **kwargs):
    """Save generation metadata as JSON."""
    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        **kwargs,
    }
    meta_path = out_dir / "metadata.json"
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")


def open_in_preview(path: Path):
    """Open file in macOS Preview or default viewer."""
    if platform.system() == "Darwin":
        subprocess.run(["open", str(path)], check=False)
    elif platform.system() == "Linux":
        subprocess.run(["xdg-open", str(path)], check=False)


def main():
    parser = argparse.ArgumentParser(
        description="Image Studio — style-aware AI image generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run generate.py --list-styles
  uv run generate.py --list-cinema
  uv run generate.py "cyberpunk poster" --style ash-thorp --prompt-only
  uv run generate.py "festival flyer" --style "kilian-eng+signalnoise" --size 2K
  uv run generate.py "dark alley" --style ash-thorp --camera arri --lighting chiaroscuro \\
      --film-stock cinestill-800t --filter "grain,vignette" --prompt-only
  uv run generate.py "portrait of old man" --camera hasselblad --lighting golden-hour \\
      --shot close-up --film-stock portra-400 --prompt-only
        """,
    )
    parser.add_argument("subject", nargs="?", help="Image description / subject")
    parser.add_argument("--list-styles", action="store_true", help="List available designer styles")
    parser.add_argument("--list-cinema", nargs="?", const="all", metavar="CATEGORY",
                        help="List cinema options (directors, photographers, cameras, lighting, etc.)")
    parser.add_argument("--style", "-s", help="Designer slug(s), use + to combine")
    parser.add_argument("--no-style", action="store_true", help="Generate without style profile")
    parser.add_argument("--prompt-only", "-p", action="store_true", help="Output prompt only, no generation")
    parser.add_argument("--backend", "-b", choices=["hf", "gemini", "auto"], default="auto",
                        help="Generation backend (default: auto-detect from env)")
    parser.add_argument("--model", "-m", help="Override model ID")
    parser.add_argument("--size", default="1K", choices=list(SIZE_MAP.keys()),
                        help="Output size (default: 1K)")
    parser.add_argument("--output", "-o", type=Path, help="Override output path")
    parser.add_argument("--no-open", action="store_true", help="Don't open result in Preview")
    parser.add_argument("--no-palette", action="store_true", help="Exclude palette from prompt")
    parser.add_argument("--no-negatives", action="store_true", help="Exclude negative rules")

    # Cinematography parameters
    cinema_group = parser.add_argument_group("cinematography")
    cinema_group.add_argument("--director", help="Director style (e.g. kubrick, villeneuve, wong-kar-wai)")
    cinema_group.add_argument("--photographer", help="Photographer style (e.g. annie-leibovitz, fan-ho)")
    cinema_group.add_argument("--camera", "-c", help="Camera model (e.g. hasselblad-500, arri-alexa)")
    cinema_group.add_argument("--lighting", "-l", help="Lighting setup (e.g. chiaroscuro, golden-hour)")
    cinema_group.add_argument("--shot", help="Shot type (e.g. close-up, wide, dutch)")
    cinema_group.add_argument("--lens-type", help="Lens type (e.g. anamorphic, petzval, tilt-shift)")
    cinema_group.add_argument("--film-stock", help="Film stock (e.g. portra-400, tri-x, cinestill-800t)")
    cinema_group.add_argument("--filter", "-f", help="Filters, comma-separated (e.g. grain,vignette,bokeh)")
    cinema_group.add_argument("--focal-length", help="Focal length in mm (e.g. 35, 50, 85)")
    cinema_group.add_argument("--aspect-ratio", help="Aspect ratio (e.g. 16:9, 2.39:1)")

    args = parser.parse_args()
    lib = StyleLibrary()

    # List styles
    if args.list_styles:
        print(f"Available styles ({len(lib.designers)} designers):\n")
        print(lib.list_styles())
        print(f"\nProfiles directory: {lib.profiles_dir}")
        return

    if args.list_cinema is not None:
        print(_list_cinema_options(args.list_cinema))
        return

    if not args.subject:
        parser.error("subject is required (or use --list-styles / --list-cinema)")

    # Parse styles
    styles = []
    if args.style and not args.no_style:
        styles = [s.strip() for s in args.style.split("+") if s.strip()]

    # Build cinema params
    cinema = None
    cinema_fields = [args.camera, args.lighting, args.shot, args.film_stock, args.filter,
                     args.focal_length, args.aspect_ratio, args.director, args.photographer,
                     getattr(args, 'lens_type', None)]
    if any(cinema_fields):
        cinema = CinemaParams(
            camera=args.camera or "",
            lighting=args.lighting or "",
            shot_type=args.shot or "",
            film_stock=args.film_stock or "",
            filters=[f.strip() for f in args.filter.split(",")] if args.filter else [],
            focal_length=args.focal_length or "",
            aspect_ratio=args.aspect_ratio or "",
            lens_type=getattr(args, 'lens_type', "") or "",
            director=args.director or "",
            photographer=args.photographer or "",
        )

    # Build prompt
    prompt = lib.build_prompt(
        subject=args.subject,
        styles=styles or None,
        cinema=cinema,
        include_palette=not args.no_palette,
        include_negatives=not args.no_negatives,
    )
    negative_prompt = lib.build_negative_prompt(styles or None)

    # Prompt-only mode
    if args.prompt_only:
        print("=== PROMPT ===")
        print(prompt)
        if negative_prompt:
            print("\n=== NEGATIVE PROMPT ===")
            print(negative_prompt)
        return

    # Detect backend
    backend = args.backend
    if backend == "auto":
        backend = detect_backend()
        if not backend:
            print("No API key found. Set HF_TOKEN or GEMINI_API_KEY, or use --prompt-only.", file=sys.stderr)
            print("\nFalling back to prompt-only mode:\n", file=sys.stderr)
            print("=== PROMPT ===")
            print(prompt)
            if negative_prompt:
                print("\n=== NEGATIVE PROMPT ===")
                print(negative_prompt)
            return

    width, height = SIZE_MAP[args.size]

    # Output path
    if args.output:
        out_path = args.output
        out_path.parent.mkdir(parents=True, exist_ok=True)
    else:
        out_dir = make_output_dir(args.subject)
        style_suffix = "-".join(styles) if styles else "no-style"
        out_path = out_dir / f"{style_suffix}.png"

    print(f"Subject:  {args.subject}")
    print(f"Style:    {', '.join(styles) if styles else '(none)'}")
    print(f"Backend:  {backend}")
    print(f"Size:     {args.size} ({width}x{height})")
    print(f"Output:   {out_path}")
    print(f"Generating...")

    # Generate
    if backend == "hf":
        model = args.model or HF_DEFAULT_MODEL
        print(f"Model:    {model}")
        image_bytes = generate_hf(prompt, negative_prompt, model, width, height)
    elif backend == "gemini":
        model = args.model or GEMINI_DEFAULT_MODEL
        size_gemini = "2K" if args.size == "2K" else "1K" if args.size in ("1K", "landscape", "portrait", "wide") else args.size
        print(f"Model:    {model}")
        image_bytes = generate_gemini(prompt, model, size_gemini)
    else:
        print(f"Unknown backend: {backend}", file=sys.stderr)
        sys.exit(1)

    # Save
    out_path.write_bytes(image_bytes)

    file_size = out_path.stat().st_size
    size_str = f"{file_size / 1024:.1f} KB" if file_size < 1024 * 1024 else f"{file_size / (1024 * 1024):.1f} MB"
    print(f"\nDone! {size_str}")
    print(f"File: {out_path}")

    # Save metadata
    meta_dir = out_path.parent
    cinema_dict = {}
    if cinema:
        cinema_dict = {
            "camera": cinema.camera, "lighting": cinema.lighting,
            "shot_type": cinema.shot_type, "film_stock": cinema.film_stock,
            "filters": cinema.filters, "focal_length": cinema.focal_length,
        }
    save_metadata(
        meta_dir,
        subject=args.subject,
        styles=styles,
        cinema=cinema_dict,
        prompt=prompt,
        negative_prompt=negative_prompt,
        backend=backend,
        model=args.model or (HF_DEFAULT_MODEL if backend == "hf" else GEMINI_DEFAULT_MODEL),
        size=args.size,
        output=str(out_path),
    )

    # Open
    if not args.no_open:
        open_in_preview(out_path)


if __name__ == "__main__":
    main()
