#!/usr/bin/env python3
"""
SVG Layout Checker — automated QA for generated poster SVGs.

Parses an SVG file, extracts all <text> elements, estimates their
bounding boxes using font metrics, and checks against:
  1. Frame overflow (text extends past outer frame or safe zone)
  2. Element overlap (two text elements with overlapping bboxes)
  3. Too-small typography (< 6pt warning)
  4. Line-length too long (Bringhurst: >85 chars warning)
  5. Missing real typographic glyphs (warns on "--" instead of "—", etc.)

Output: JSON report with passed:bool and issues:list.

Usage:
    python3 tools/check-layout.py my-works/.../poster.svg
    python3 tools/check-layout.py my-works/.../poster.svg --verbose
    python3 tools/check-layout.py my-works/.../poster.svg --json-only

Exit codes:
    0 = passed (no issues)
    1 = failed (critical issues present)
    2 = error (malformed SVG, file not found)

Called by ~/.claude/agents/layout-verifier.md (Claude subagent).

Not a perfect pixel-accurate renderer — it uses font-metrics estimates
(typical glyph widths as fraction of font-size) which are ~95% accurate
for detecting real overflow issues. Errs on the side of catching
false positives rather than missing real ones.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

# ── FONT METRICS (approximate avg glyph width as fraction of font-size) ──
# These are tuned for the SAN-SERIF / SERIF families we use in this library.
# Not perfect but catches ~95% of real overflow issues.

FONT_METRICS = {
    # family_substring (lowercase) : avg-glyph-width factor
    "impact":            0.42,   # Impact is narrow/condensed
    "arial black":       0.58,   # Arial Black is wide
    "helvetica neue":    0.52,
    "helvetica":         0.52,
    "sf pro display":    0.54,
    "sf pro text":       0.52,
    "sf pro":            0.53,
    "arial":             0.52,
    "inter":             0.51,
    "georgia":           0.52,
    "times new roman":   0.50,
    "times":             0.50,
    "ebgaramond":        0.47,
    "eb garamond":       0.47,
    "garamond":          0.47,
    "bodoni":            0.49,
    "didot":             0.48,
    "baskerville":       0.50,
    "caslon":            0.50,
    "courier new":       0.60,   # monospace
    "courier":           0.60,
    "monospace":         0.60,
    "serif":             0.50,
    "sans-serif":        0.52,
}

# Default if font unknown
DEFAULT_GLYPH_FACTOR = 0.55

# Cap height as fraction of font-size (how tall uppercase letters are)
CAP_HEIGHT_FACTOR = 0.72
# Descender depth as fraction of font-size
DESCENDER_FACTOR = 0.22

# ── VALIDATION THRESHOLDS ────────────────────────────────────────────────

MIN_LEGIBLE_FONT_SIZE = 6.0           # pt — below this, warn
MAX_LINE_LENGTH_CHARS = 85            # Bringhurst upper bound
OVERFLOW_TOLERANCE_PX = 1.0           # px — allow this much slop before flagging

# ── ISSUE TYPES ──────────────────────────────────────────────────────────

@dataclass
class Issue:
    type: str                 # "overflow_right" | "overflow_left" | "overlap" | "too_small" | "line_too_long" | "fake_glyph"
    severity: str             # "critical" | "warning"
    element: str              # short description of the offending text
    details: dict = field(default_factory=dict)
    suggestion: str = ""

    def to_dict(self):
        return {
            "type": self.type,
            "severity": self.severity,
            "element": self.element,
            "details": self.details,
            "suggestion": self.suggestion,
        }


@dataclass
class TextBox:
    """Estimated bounding box of a <text> element."""
    text: str
    x: float
    y: float                  # baseline y
    font_size: float
    font_family: str
    letter_spacing: float
    text_anchor: str          # start | middle | end
    width: float              # estimated total rendered width
    x_start: float            # actual left edge after anchor resolution
    x_end: float              # actual right edge
    y_top: float              # approx cap-top
    y_bottom: float           # approx descender bottom

    def overlaps_with(self, other: "TextBox") -> bool:
        x_overlap = not (self.x_end < other.x_start or other.x_end < self.x_start)
        y_overlap = not (self.y_bottom < other.y_top or other.y_bottom < self.y_top)
        return x_overlap and y_overlap


# ── SVG PARSING ──────────────────────────────────────────────────────────

SVG_NS = "http://www.w3.org/2000/svg"

def parse_svg_viewbox(root: ET.Element) -> tuple[float, float]:
    """Return (width, height) from viewBox or width/height attrs."""
    vb = root.get("viewBox")
    if vb:
        parts = vb.split()
        if len(parts) == 4:
            return float(parts[2]), float(parts[3])
    w = root.get("width", "612")
    h = root.get("height", "888")
    # Strip units
    w = re.sub(r"[a-zA-Z]+$", "", w)
    h = re.sub(r"[a-zA-Z]+$", "", h)
    return float(w), float(h)


def find_outer_frame(root: ET.Element) -> tuple[float, float, float, float] | None:
    """
    Look for an outer frame <rect> stroked but not filled,
    usually the first such rect in the document.
    Returns (x, y, width, height) or None.
    """
    for elem in root.iter():
        tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
        if tag == "rect":
            fill = elem.get("fill", "")
            stroke = elem.get("stroke", "")
            if (fill == "none" or fill.startswith("none")) and stroke and stroke != "none":
                try:
                    x = float(elem.get("x", "0"))
                    y = float(elem.get("y", "0"))
                    w = float(elem.get("width", "0"))
                    h = float(elem.get("height", "0"))
                    # Heuristic: only return if rect is large (>70% of viewport)
                    if w > 300 and h > 400:
                        return (x, y, w, h)
                except ValueError:
                    continue
    return None


def get_glyph_factor(font_family: str) -> float:
    """Find the best-matching glyph-width factor for this font family string."""
    if not font_family:
        return DEFAULT_GLYPH_FACTOR
    ff = font_family.lower()
    # Longest-match first so "arial black" beats "arial"
    for key in sorted(FONT_METRICS.keys(), key=len, reverse=True):
        if key in ff:
            return FONT_METRICS[key]
    return DEFAULT_GLYPH_FACTOR


def estimate_text_width(text: str, font_size: float, font_family: str, letter_spacing: float) -> float:
    """
    Estimate rendered width of a text string.
    avg glyph width = font-size * factor, then * n_chars, then + letter_spacing * (n-1).
    """
    if not text:
        return 0.0
    n = len(text)
    factor = get_glyph_factor(font_family)
    base_glyph_width = font_size * factor
    total = base_glyph_width * n + max(0, n - 1) * letter_spacing
    return total


def resolve_text_x_range(x_attr: float, anchor: str, width: float) -> tuple[float, float]:
    """Given the anchor-x and resolved width, return (x_start, x_end)."""
    if anchor == "middle":
        return (x_attr - width / 2, x_attr + width / 2)
    elif anchor == "end":
        return (x_attr - width, x_attr)
    else:  # start
        return (x_attr, x_attr + width)


def extract_text_boxes(root: ET.Element) -> list[TextBox]:
    """Walk SVG and build TextBox estimates for every <text> element."""
    boxes: list[TextBox] = []

    def collect_text_content(elem) -> str:
        """
        Get the text of an element, including <tspan> children.
        Trim/join to produce the rendered string length.
        """
        parts = []
        if elem.text:
            parts.append(elem.text)
        for child in elem:
            # Any tspan or similar — recurse
            if child.text:
                parts.append(child.text)
            if child.tail:
                parts.append(child.tail)
        # Normalize whitespace (SVG renders consecutive whitespace as one space)
        joined = " ".join(p for p in parts if p)
        return re.sub(r"\s+", " ", joined).strip()

    def resolve_inherited_attr(elem, attr_name, default):
        """Walk up parents to inherit attr (font-size, fill, etc.)."""
        current = elem
        while current is not None:
            val = current.get(attr_name)
            if val is not None:
                return val
            # Parent lookup is manual in ElementTree — done via the parent map below
            current = parent_map.get(id(current))
        return default

    # Build parent map for inheritance walk
    parent_map: dict[int, ET.Element] = {}
    for parent in root.iter():
        for child in parent:
            parent_map[id(child)] = parent

    for elem in root.iter():
        tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
        if tag != "text":
            continue

        text = collect_text_content(elem)
        if not text:
            continue

        # Skip textPath rendering (text along a curve) — bbox estimation doesn't apply cleanly
        has_textpath = any(
            (c.tag.split("}")[-1] if "}" in c.tag else c.tag) == "textPath"
            for c in elem
        )
        if has_textpath:
            continue

        try:
            x = float(elem.get("x", "0"))
            y = float(elem.get("y", "0"))
        except ValueError:
            continue

        font_size_raw = resolve_inherited_attr(elem, "font-size", "12")
        font_size_raw = re.sub(r"[a-zA-Z]+$", "", str(font_size_raw))
        try:
            font_size = float(font_size_raw)
        except ValueError:
            font_size = 12.0

        font_family = resolve_inherited_attr(elem, "font-family", "sans-serif")

        letter_spacing_raw = resolve_inherited_attr(elem, "letter-spacing", "0")
        letter_spacing_raw = re.sub(r"[a-zA-Z]+$", "", str(letter_spacing_raw))
        try:
            letter_spacing = float(letter_spacing_raw)
        except ValueError:
            letter_spacing = 0.0

        anchor = resolve_inherited_attr(elem, "text-anchor", "start")

        width = estimate_text_width(text, font_size, font_family, letter_spacing)
        x_start, x_end = resolve_text_x_range(x, anchor, width)

        y_top = y - font_size * CAP_HEIGHT_FACTOR
        y_bottom = y + font_size * DESCENDER_FACTOR

        boxes.append(TextBox(
            text=text,
            x=x, y=y,
            font_size=font_size,
            font_family=font_family,
            letter_spacing=letter_spacing,
            text_anchor=anchor,
            width=width,
            x_start=x_start,
            x_end=x_end,
            y_top=y_top,
            y_bottom=y_bottom,
        ))

    return boxes


# ── CHECKS ───────────────────────────────────────────────────────────────

def check_overflow(boxes: list[TextBox], frame: tuple[float, float, float, float] | None, viewbox: tuple[float, float]) -> list[Issue]:
    """Check if any text extends past the outer frame or viewport."""
    issues = []
    if frame:
        fx, fy, fw, fh = frame
        frame_left, frame_right = fx, fx + fw
        frame_top, frame_bottom = fy, fy + fh
    else:
        vw, vh = viewbox
        frame_left, frame_right = 0, vw
        frame_top, frame_bottom = 0, vh

    for b in boxes:
        truncated_text = b.text[:50] + ("…" if len(b.text) > 50 else "")
        if b.x_end > frame_right + OVERFLOW_TOLERANCE_PX:
            over = b.x_end - frame_right
            issues.append(Issue(
                type="overflow_right",
                severity="critical",
                element=f'"{truncated_text}" at y={b.y:.0f}',
                details={
                    "text": b.text,
                    "y": b.y,
                    "extends_to_x": round(b.x_end, 1),
                    "frame_right": frame_right,
                    "overflow_px": round(over, 1),
                    "font_size": b.font_size,
                    "letter_spacing": b.letter_spacing,
                    "text_anchor": b.text_anchor,
                },
                suggestion=f"Text extends {over:.1f}px past right frame. Reduce font-size, reduce letter-spacing, shorten text, or change text-anchor."
            ))
        if b.x_start < frame_left - OVERFLOW_TOLERANCE_PX:
            over = frame_left - b.x_start
            issues.append(Issue(
                type="overflow_left",
                severity="critical",
                element=f'"{truncated_text}" at y={b.y:.0f}',
                details={
                    "text": b.text,
                    "y": b.y,
                    "starts_at_x": round(b.x_start, 1),
                    "frame_left": frame_left,
                    "overflow_px": round(over, 1),
                    "font_size": b.font_size,
                    "letter_spacing": b.letter_spacing,
                    "text_anchor": b.text_anchor,
                },
                suggestion=f"Text starts {over:.1f}px past left frame. Reduce font-size, shorten text, or change position."
            ))
        if b.y_top < frame_top - OVERFLOW_TOLERANCE_PX:
            over = frame_top - b.y_top
            issues.append(Issue(
                type="overflow_top",
                severity="warning",
                element=f'"{truncated_text}" at y={b.y:.0f}',
                details={
                    "y_top": round(b.y_top, 1),
                    "frame_top": frame_top,
                    "overflow_px": round(over, 1),
                },
                suggestion=f"Text top extends {over:.1f}px above frame. Move text down or reduce font-size."
            ))
        if b.y_bottom > frame_bottom + OVERFLOW_TOLERANCE_PX:
            over = b.y_bottom - frame_bottom
            issues.append(Issue(
                type="overflow_bottom",
                severity="warning",
                element=f'"{truncated_text}" at y={b.y:.0f}',
                details={
                    "y_bottom": round(b.y_bottom, 1),
                    "frame_bottom": frame_bottom,
                    "overflow_px": round(over, 1),
                },
                suggestion=f"Text descender extends {over:.1f}px below frame. Move text up or reduce font-size."
            ))
    return issues


def check_overlaps(boxes: list[TextBox]) -> list[Issue]:
    """Check if any two text boxes overlap."""
    issues = []
    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            if a.overlaps_with(b):
                # Compute overlap size
                x_overlap = min(a.x_end, b.x_end) - max(a.x_start, b.x_start)
                y_overlap = min(a.y_bottom, b.y_bottom) - max(a.y_top, b.y_top)
                # Skip trivial overlaps (decorative overlays intended)
                if x_overlap < 2 or y_overlap < 2:
                    continue
                truncated_a = a.text[:30] + ("…" if len(a.text) > 30 else "")
                truncated_b = b.text[:30] + ("…" if len(b.text) > 30 else "")
                issues.append(Issue(
                    type="overlap",
                    severity="critical",
                    element=f'"{truncated_a}" (y={a.y:.0f}) ↔ "{truncated_b}" (y={b.y:.0f})',
                    details={
                        "elem_a": {"text": a.text, "y": a.y, "x_range": [round(a.x_start, 1), round(a.x_end, 1)]},
                        "elem_b": {"text": b.text, "y": b.y, "x_range": [round(b.x_start, 1), round(b.x_end, 1)]},
                        "overlap_x_px": round(x_overlap, 1),
                        "overlap_y_px": round(y_overlap, 1),
                    },
                    suggestion=f"Two text elements overlap. Move one vertically (recommended Δy ≥ {y_overlap + 4:.0f}px), reduce font-sizes, or shorten content."
                ))
    return issues


def check_font_sizes(boxes: list[TextBox]) -> list[Issue]:
    """Check for fonts below legibility threshold."""
    issues = []
    for b in boxes:
        if b.font_size < MIN_LEGIBLE_FONT_SIZE:
            truncated = b.text[:40] + ("…" if len(b.text) > 40 else "")
            issues.append(Issue(
                type="too_small",
                severity="warning",
                element=f'"{truncated}" at y={b.y:.0f}',
                details={
                    "font_size": b.font_size,
                    "recommended_min": MIN_LEGIBLE_FONT_SIZE,
                },
                suggestion=f"Font-size {b.font_size}pt is below minimum legible ({MIN_LEGIBLE_FONT_SIZE}pt). Increase or remove."
            ))
    return issues


def check_line_lengths(boxes: list[TextBox]) -> list[Issue]:
    """Check for body text lines exceeding Bringhurst's 85-char max."""
    issues = []
    for b in boxes:
        # Only flag body-sized text (font-size <= 14)
        if b.font_size <= 14 and len(b.text) > MAX_LINE_LENGTH_CHARS:
            issues.append(Issue(
                type="line_too_long",
                severity="warning",
                element=f'"{b.text[:40]}…" at y={b.y:.0f}',
                details={
                    "char_count": len(b.text),
                    "recommended_max": MAX_LINE_LENGTH_CHARS,
                    "font_size": b.font_size,
                },
                suggestion=f"Line is {len(b.text)} chars, exceeds Bringhurst 85-char maximum. Break into multiple lines or increase font-size."
            ))
    return issues


def check_fake_glyphs(raw_svg: str) -> list[Issue]:
    """
    Look for keyboard substitutes where real glyphs should be used.
    This is a warning-level check. Catches -- (should be em-dash),
    straight quotes that look like they're used as quotation marks, etc.
    """
    issues = []

    # Check for "--" which should be em-dash
    # But only when it's between words (not a CLI flag like --prompt-only)
    double_hyphen = re.findall(r"\w\s*--\s*\w", raw_svg)
    if double_hyphen:
        issues.append(Issue(
            type="fake_glyph",
            severity="warning",
            element="double-hyphen '--' found",
            details={"occurrences": len(double_hyphen)},
            suggestion="Replace '--' with em-dash '—' (U+2014) in body text per Bringhurst."
        ))

    # Straight quotes around words (looks like fake quotation marks)
    straight_quotes = re.findall(r'(?<=[>\s])"[A-Za-z]', raw_svg)
    if straight_quotes and len(straight_quotes) >= 2:
        issues.append(Issue(
            type="fake_glyph",
            severity="warning",
            element='straight quotes "..." used as quotation marks',
            details={"occurrences": len(straight_quotes)},
            suggestion='Replace straight quotes with curly quotes " " (U+201C U+201D) per Bringhurst.'
        ))

    # "..." ellipsis (should be …)
    dot_ellipsis = raw_svg.count("...")
    if dot_ellipsis > 0:
        # Subtract cases in XML comments / attribute values
        if re.search(r">\s*[A-Za-z].*\.\.\.", raw_svg):
            issues.append(Issue(
                type="fake_glyph",
                severity="warning",
                element="three-dot '...' ellipsis",
                details={"approximate_occurrences": dot_ellipsis},
                suggestion="Replace '...' with ellipsis character '…' (U+2026) per Bringhurst."
            ))

    return issues


# ── MAIN ─────────────────────────────────────────────────────────────────

def run_checks(svg_path: Path) -> dict:
    try:
        raw = svg_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {"passed": False, "error": f"File not found: {svg_path}", "issues": []}

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        return {"passed": False, "error": f"Malformed SVG: {e}", "issues": []}

    viewbox = parse_svg_viewbox(root)
    frame = find_outer_frame(root)
    boxes = extract_text_boxes(root)

    all_issues: list[Issue] = []
    all_issues.extend(check_overflow(boxes, frame, viewbox))
    all_issues.extend(check_overlaps(boxes))
    all_issues.extend(check_font_sizes(boxes))
    all_issues.extend(check_line_lengths(boxes))
    all_issues.extend(check_fake_glyphs(raw))

    critical = [i for i in all_issues if i.severity == "critical"]
    warning = [i for i in all_issues if i.severity == "warning"]

    return {
        "passed": len(critical) == 0,
        "file": str(svg_path),
        "viewbox": {"width": viewbox[0], "height": viewbox[1]},
        "frame": ({"x": frame[0], "y": frame[1], "width": frame[2], "height": frame[3]}
                  if frame else None),
        "text_elements_checked": len(boxes),
        "summary": {
            "critical": len(critical),
            "warning": len(warning),
            "total": len(all_issues),
        },
        "issues": [i.to_dict() for i in all_issues],
    }


def format_human_report(result: dict) -> str:
    """Human-readable report for terminal output."""
    lines = []
    lines.append(f"\n{'=' * 70}")
    lines.append(f"Layout check: {result.get('file', 'unknown')}")
    lines.append(f"{'=' * 70}")
    if result.get("error"):
        lines.append(f"ERROR: {result['error']}")
        return "\n".join(lines)

    vb = result["viewbox"]
    lines.append(f"Viewport: {vb['width']:.0f} × {vb['height']:.0f}")
    if result["frame"]:
        f = result["frame"]
        lines.append(f"Frame:    x={f['x']:.0f}, y={f['y']:.0f}, w={f['width']:.0f}, h={f['height']:.0f}")
    else:
        lines.append("Frame:    (no outer frame detected — using viewport as bounds)")
    lines.append(f"Text elements checked: {result['text_elements_checked']}")
    lines.append("")

    s = result["summary"]
    if result["passed"]:
        lines.append(f"✓ PASSED — {s['warning']} warning(s), 0 critical issues")
    else:
        lines.append(f"✗ FAILED — {s['critical']} critical issue(s), {s['warning']} warning(s)")

    if result["issues"]:
        lines.append("")
        lines.append("Issues:")
        for i, issue in enumerate(result["issues"], 1):
            marker = "✗" if issue["severity"] == "critical" else "⚠"
            lines.append(f"  {marker} [{issue['type']}] {issue['element']}")
            if issue.get("suggestion"):
                lines.append(f"      → {issue['suggestion']}")

    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="SVG layout checker for design-library posters")
    parser.add_argument("svg_path", type=Path, help="Path to SVG file to check")
    parser.add_argument("--json-only", action="store_true", help="Output only JSON result")
    parser.add_argument("--verbose", "-v", action="store_true", help="Include full issue details in human report")
    args = parser.parse_args()

    result = run_checks(args.svg_path)

    if args.json_only:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_human_report(result))
        if args.verbose:
            print("\nFull JSON:")
            print(json.dumps(result, indent=2, ensure_ascii=False))

    if result.get("error"):
        sys.exit(2)
    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
