#!/usr/bin/env python3
"""
Style-aware prompt builder for AI image generation.

Reads designer style profiles from design-library/style-profiles/
and builds enhanced prompts with tactical rules, palette, mood, and negative constraints.

Usage as module:
    from prompt_builder import StyleLibrary
    lib = StyleLibrary()
    prompt = lib.build_prompt("cyberpunk poster", styles=["ash-thorp"])

Usage as CLI:
    python prompt_builder.py --list
    python prompt_builder.py --style ash-thorp "cyberpunk city at night"
    python prompt_builder.py --style "ash-thorp+kilian-eng" "fantasy landscape"
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass, field


LIBRARY_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = LIBRARY_ROOT / "style-profiles"


# Import comprehensive presets from presets.py
from presets import (
    DIRECTORS, PHOTOGRAPHERS, CAMERAS, LIGHTING, SHOT_TYPES,
    LENS_TYPES, FOCAL_LENGTHS, FILM_STOCKS, FILTERS,
    list_options as list_preset_options,
)


@dataclass
class CinemaParams:
    """Cinematography parameters for image generation."""
    camera: str = ""
    lighting: str = ""
    shot_type: str = ""
    film_stock: str = ""
    filters: list[str] = field(default_factory=list)
    aspect_ratio: str = ""
    focal_length: str = ""
    lens_type: str = ""
    director: str = ""
    photographer: str = ""

    def to_prompt_fragment(self) -> str:
        """Build a prompt fragment from cinema parameters."""
        parts = []
        if self.shot_type:
            val = SHOT_TYPES.get(self.shot_type, self.shot_type)
            parts.append(val)
        if self.camera:
            val = CAMERAS.get(self.camera, self.camera)
            parts.append(f"shot on {val}")
        if self.focal_length:
            val = FOCAL_LENGTHS.get(self.focal_length, f"{self.focal_length}mm lens")
            parts.append(val)
        if self.lens_type:
            val = LENS_TYPES.get(self.lens_type, self.lens_type)
            parts.append(val)
        if self.film_stock:
            val = FILM_STOCKS.get(self.film_stock, self.film_stock)
            parts.append(val)
        if self.lighting:
            val = LIGHTING.get(self.lighting, self.lighting)
            parts.append(val)
        if self.director:
            d = DIRECTORS.get(self.director)
            if d:
                parts.append(f"in the cinematic style of {d[0]}, {d[1]}")
            else:
                parts.append(f"in the cinematic style of {self.director}")
        if self.photographer:
            name = PHOTOGRAPHERS.get(self.photographer, self.photographer)
            parts.append(f"in the photographic style of {name}")
        if self.filters:
            filter_descs = []
            for f in self.filters:
                val = FILTERS.get(f, f)
                filter_descs.append(val)
            parts.append(", ".join(filter_descs))
        if self.aspect_ratio:
            parts.append(f"{self.aspect_ratio} aspect ratio")
        return ". ".join(parts) if parts else ""


@dataclass
class StyleProfile:
    slug: str
    name: str
    core_identity: str
    palette_hex: list[str]
    palette_description: str
    mood: str
    how_to_apply: list[str]
    negative_rules: list[str]
    signature_moves: list[str]
    when_to_apply: str = ""
    genre: str = ""


def _extract_section(text: str, heading: str) -> str:
    """Extract content under a ## heading, stopping at the next ## heading."""
    pattern = rf"^## {re.escape(heading)}.*?\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def _extract_section_fuzzy(text: str, heading_fragment: str) -> str:
    """Extract content under a ## heading that contains the fragment."""
    pattern = rf"^## .*?{re.escape(heading_fragment)}.*?\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def _extract_hex_codes(text: str) -> list[str]:
    """Pull all hex color codes from text."""
    return list(dict.fromkeys(re.findall(r"#[0-9A-Fa-f]{6}", text)))


def _strip_markdown(text: str) -> str:
    """Remove markdown bold/italic markers from text."""
    text = re.sub(r"\*{1,2}(.+?)\*{1,2}", r"\1", text)
    text = re.sub(r"_{1,2}(.+?)_{1,2}", r"\1", text)
    return text.strip()


def _extract_list_items(text: str) -> list[str]:
    """Extract markdown list items or numbered items, stripping markdown formatting."""
    items = []
    for line in text.splitlines():
        line = line.strip()
        m = re.match(r"^(?:\d+\.\s*|\-\s*|\*\s+)(.+)$", line)
        if m:
            items.append(_strip_markdown(m.group(1)))
        elif line.startswith("- "):
            items.append(_strip_markdown(line[2:]))
    return [i for i in items if i]


def _extract_negative_rules(text: str) -> list[str]:
    """Extract negative/avoid rules from text (lines with NOT, NO, don't, avoid, never)."""
    negatives = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.search(r"(❌|NOT for|NOT to use|NO |Don't|Never|Avoid)", stripped, re.IGNORECASE):
            clean = re.sub(r"^[\-\*\d.]+\s*", "", stripped)
            clean = clean.replace("❌", "").strip()
            clean = _strip_markdown(clean)
            if clean:
                negatives.append(clean)
    return negatives


def _extract_name_from_heading(text: str) -> str:
    """Extract designer name from # heading."""
    m = re.match(r"^#\s+(.+?)(?:\s*[—–-]\s*Style Profile)?$", text.splitlines()[0] if text else "")
    return m.group(1).strip() if m else ""


def parse_profile(path: Path) -> StyleProfile:
    """Parse a style profile .md file into structured data."""
    text = path.read_text(encoding="utf-8")
    slug = path.stem

    name = _extract_name_from_heading(text) or slug.replace("-", " ").title()

    core_section = _extract_section(text, "Core Identity")
    core_identity = core_section.split("\n")[0] if core_section else ""

    palette_section = _extract_section(text, "Palette")
    palette_hex = _extract_hex_codes(palette_section)
    palette_desc_lines = [
        l.strip() for l in palette_section.splitlines()
        if l.strip() and not l.strip().startswith("#")
    ]
    palette_description = " ".join(palette_desc_lines[:3])

    mood_section = _extract_section_fuzzy(text, "Mood")
    mood = _strip_markdown(mood_section.split("\n")[0]) if mood_section else ""

    how_to_apply_section = _extract_section_fuzzy(text, "How to apply")
    how_to_apply = _extract_list_items(how_to_apply_section)

    when_section = _extract_section_fuzzy(text, "When to apply")
    when_to_apply = when_section

    signature_section = _extract_section(text, "Signature Moves")
    signature_moves = _extract_list_items(signature_section)

    negatives = _extract_negative_rules(how_to_apply_section)
    negatives += _extract_negative_rules(when_section)

    genre_hints = []
    if "cyberpunk" in text.lower():
        genre_hints.append("cyberpunk")
    if "minimalism" in text.lower() or "minimalist" in text.lower():
        genre_hints.append("minimalism")
    if "retrofutur" in text.lower() or "synthwave" in text.lower():
        genre_hints.append("retrofuturism")
    if "typography" in text.lower() and "chaos" in text.lower():
        genre_hints.append("chaos typography")

    return StyleProfile(
        slug=slug,
        name=name,
        core_identity=core_identity,
        palette_hex=palette_hex,
        palette_description=palette_description,
        mood=mood,
        how_to_apply=how_to_apply,
        negative_rules=list(dict.fromkeys(negatives)),
        signature_moves=signature_moves[:7],
        when_to_apply=when_section,
        genre=", ".join(genre_hints) if genre_hints else "",
    )


class StyleLibrary:
    """Reads and indexes all style profiles from design-library."""

    def __init__(self, profiles_dir: Path | None = None):
        self.profiles_dir = profiles_dir or PROFILES_DIR
        self._profiles: dict[str, StyleProfile] = {}
        self._load()

    def _load(self):
        if not self.profiles_dir.exists():
            return
        for path in sorted(self.profiles_dir.glob("*.md")):
            try:
                profile = parse_profile(path)
                self._profiles[profile.slug] = profile
            except Exception as e:
                print(f"Warning: failed to parse {path.name}: {e}", file=sys.stderr)

    @property
    def designers(self) -> list[str]:
        return list(self._profiles.keys())

    def get(self, slug: str) -> StyleProfile | None:
        return self._profiles.get(slug)

    def list_styles(self) -> str:
        """Human-readable list of available styles."""
        lines = []
        for slug, p in self._profiles.items():
            genre = f" [{p.genre}]" if p.genre else ""
            lines.append(f"  {slug:<30} {p.name}{genre}")
            if p.core_identity:
                short = p.core_identity[:80] + ("..." if len(p.core_identity) > 80 else "")
                lines.append(f"  {'':30} {short}")
        return "\n".join(lines)

    def build_prompt(
        self,
        subject: str,
        styles: list[str] | None = None,
        cinema: CinemaParams | None = None,
        include_palette: bool = True,
        include_mood: bool = True,
        include_negatives: bool = True,
    ) -> str:
        """Build an enhanced image generation prompt from subject + style profiles + cinema params.

        Args:
            subject: The main image description (e.g. "cyberpunk city at night")
            styles: List of designer slugs to apply (e.g. ["ash-thorp", "kilian-eng"])
            cinema: Cinematography parameters (camera, lighting, shot type, etc.)
            include_palette: Include hex color references
            include_mood: Include mood/emotional register
            include_negatives: Include negative prompt constraints

        Returns:
            Enhanced prompt string ready for image generation APIs.
        """
        parts = [subject.strip().rstrip(".")]

        # Cinematography parameters (before style — they're physical/technical)
        if cinema:
            frag = cinema.to_prompt_fragment()
            if frag:
                parts.append(frag)

        if not styles and not cinema:
            return parts[0]
        if not styles:
            return ". ".join(parts)

        profiles = []
        for slug in styles:
            p = self.get(slug)
            if not p:
                print(f"Warning: style '{slug}' not found, skipping", file=sys.stderr)
                continue
            profiles.append(p)

        if not profiles:
            return parts[0]

        # Style attribution
        names = [p.name for p in profiles]
        if len(names) == 1:
            parts.append(f"In the style of {names[0]}.")
        else:
            parts.append(f"Combining styles of {' and '.join(names)}.")

        # Tactical rules (How to apply)
        all_rules = []
        for p in profiles:
            for rule in p.how_to_apply:
                if not any(neg in rule.upper() for neg in ["NO ", "NOT ", "NEVER", "AVOID"]):
                    all_rules.append(rule)
        if all_rules:
            rules_text = " ".join(all_rules[:10])
            parts.append(f"Style rules: {rules_text}")

        # Palette
        if include_palette:
            all_hex = []
            for p in profiles:
                all_hex.extend(p.palette_hex[:6])
            if all_hex:
                hex_str = ", ".join(dict.fromkeys(all_hex))
                parts.append(f"Color palette: {hex_str}.")

        # Mood
        if include_mood:
            moods = [p.mood for p in profiles if p.mood]
            if moods:
                parts.append(f"Mood: {' / '.join(moods)}")

        # Signature moves (top 3 per designer)
        moves = []
        for p in profiles:
            moves.extend(p.signature_moves[:3])
        if moves:
            parts.append(f"Key techniques: {'; '.join(moves[:6])}.")

        # Negative prompt
        if include_negatives:
            all_negs = []
            for p in profiles:
                all_negs.extend(p.negative_rules)
            if all_negs:
                negs_text = "; ".join(dict.fromkeys(all_negs))
                parts.append(f"Avoid: {negs_text}")

        return " ".join(parts)

    def build_negative_prompt(self, styles: list[str] | None = None) -> str:
        """Build a separate negative prompt string (for models that support it)."""
        if not styles:
            return ""
        negs = []
        for slug in styles:
            p = self.get(slug)
            if p:
                negs.extend(p.negative_rules)
        return ", ".join(dict.fromkeys(negs)) if negs else ""


def _list_cinema_options(category: str = "all") -> str:
    """Print available cinematography options."""
    return list_preset_options(category)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Build style-aware prompts from design-library profiles",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python prompt_builder.py --list
  python prompt_builder.py --list-cinema
  python prompt_builder.py --style ash-thorp "cyberpunk city at night"
  python prompt_builder.py --style "ash-thorp+kilian-eng" "dark fantasy landscape"
  python prompt_builder.py --camera hasselblad --lighting chiaroscuro "portrait"
  python prompt_builder.py --style ash-thorp --camera arri --lighting low-key \\
      --film-stock cinestill-800t --filter "grain,vignette" "dark alley at night"
        """,
    )
    parser.add_argument("subject", nargs="?", help="Image description / subject")
    parser.add_argument("--list", action="store_true", help="List available designer styles")
    parser.add_argument("--list-cinema", nargs="?", const="all", metavar="CATEGORY",
                        help="List cinema options. Categories: directors, photographers, cameras, "
                             "lighting, shots, lenses, focal-lengths, film-stocks, filters, aspect-ratios")
    parser.add_argument("--style", "-s", help="Designer slug(s), use + to combine: ash-thorp+kilian-eng")

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
    cinema_group.add_argument("--aspect-ratio", help="Aspect ratio (e.g. 16:9, 4:3, 2.39:1)")

    parser.add_argument("--no-palette", action="store_true", help="Exclude hex palette from prompt")
    parser.add_argument("--no-mood", action="store_true", help="Exclude mood from prompt")
    parser.add_argument("--no-negatives", action="store_true", help="Exclude negative rules")
    parser.add_argument("--negative-only", action="store_true", help="Output only the negative prompt")
    parser.add_argument("--profiles-dir", type=Path, help="Override profiles directory")

    args = parser.parse_args()
    lib = StyleLibrary(args.profiles_dir)

    if args.list:
        print(f"Available styles ({len(lib.designers)} designers):\n")
        print(lib.list_styles())
        return

    if args.list_cinema is not None:
        print(_list_cinema_options(args.list_cinema))
        return

    if not args.subject:
        parser.error("subject is required (or use --list / --list-cinema)")

    styles = args.style.split("+") if args.style else None

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

    if args.negative_only:
        neg = lib.build_negative_prompt(styles)
        if neg:
            print(neg)
        return

    prompt = lib.build_prompt(
        subject=args.subject,
        styles=styles,
        cinema=cinema,
        include_palette=not args.no_palette,
        include_mood=not args.no_mood,
        include_negatives=not args.no_negatives,
    )
    print(prompt)


if __name__ == "__main__":
    main()
