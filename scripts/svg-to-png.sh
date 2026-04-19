#!/usr/bin/env bash
#
# svg-to-png.sh — convert an SVG poster to PNG for sharing / social / preview.
#
# Usage:
#   scripts/svg-to-png.sh <path-to-svg> [output-size]
#
# Examples:
#   scripts/svg-to-png.sh my-works/showcase-themed-2026/01-cinema-arrakis.svg
#   scripts/svg-to-png.sh my-works/.../poster.svg 2048
#
# Default output size: 1224 (2x the 612 canvas width for retina).
# Output file: same name as SVG, with .png extension, written alongside the SVG.
#
# Uses macOS `qlmanage` (built-in, no install needed) as primary method.
# Falls back to headless Chrome via `/Applications/Google Chrome.app` if qlmanage fails.
# Final fallback: `rsvg-convert` if you've installed librsvg (`brew install librsvg`).

set -euo pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <path-to-svg> [output-size]" >&2
    exit 1
fi

SVG_PATH="$1"
OUTPUT_SIZE="${2:-1224}"

if [[ ! -f "$SVG_PATH" ]]; then
    echo "Error: SVG file not found: $SVG_PATH" >&2
    exit 1
fi

# Derive output path (same dir, same name, .png extension)
PNG_PATH="${SVG_PATH%.svg}.png"

echo "Converting: $SVG_PATH"
echo "Output:     $PNG_PATH"
echo "Size:       ${OUTPUT_SIZE}px wide"

# Method 1 — qlmanage (macOS built-in QuickLook)
if command -v qlmanage >/dev/null 2>&1; then
    TMP_DIR=$(mktemp -d)
    if qlmanage -t -s "$OUTPUT_SIZE" -o "$TMP_DIR" "$SVG_PATH" >/dev/null 2>&1; then
        # qlmanage writes <basename>.svg.png — rename to .png
        GENERATED="$TMP_DIR/$(basename "$SVG_PATH").png"
        if [[ -f "$GENERATED" ]]; then
            mv "$GENERATED" "$PNG_PATH"
            rm -rf "$TMP_DIR"
            echo "✓ Converted via qlmanage"
            ls -lh "$PNG_PATH"
            exit 0
        fi
    fi
    rm -rf "$TMP_DIR"
    echo "qlmanage failed, trying next method..."
fi

# Method 2 — headless Chrome (if installed)
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [[ -x "$CHROME" ]]; then
    "$CHROME" --headless --disable-gpu --screenshot="$PNG_PATH" \
        --window-size="${OUTPUT_SIZE},${OUTPUT_SIZE}" "file://$(realpath "$SVG_PATH")" >/dev/null 2>&1
    if [[ -f "$PNG_PATH" ]]; then
        echo "✓ Converted via headless Chrome"
        ls -lh "$PNG_PATH"
        exit 0
    fi
    echo "Chrome method failed, trying next..."
fi

# Method 3 — rsvg-convert (if librsvg installed via homebrew)
if command -v rsvg-convert >/dev/null 2>&1; then
    rsvg-convert -w "$OUTPUT_SIZE" -o "$PNG_PATH" "$SVG_PATH"
    if [[ -f "$PNG_PATH" ]]; then
        echo "✓ Converted via rsvg-convert"
        ls -lh "$PNG_PATH"
        exit 0
    fi
fi

echo "Error: no working conversion method found." >&2
echo "Install one of:" >&2
echo "  - Google Chrome (headless)" >&2
echo "  - librsvg:  brew install librsvg" >&2
exit 1
