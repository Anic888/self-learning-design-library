# Bringhurst — The Elements of Typographic Style

*Robert Bringhurst, 4th edition (2012). The canonical micro-typography reference. These are the LLM-actionable rules — not the philosophy.*

## Measure (line length)

- Ideal body-text measure: **45–75 characters per line** (including spaces)
- Single-column books: aim for **60–72 characters**
- Multi-column / newspaper: **40–50 characters**
- If a column is too narrow, drop font size. If too wide, split into two columns.
- Never exceed 85 characters — eye fatigue kicks in hard.

## Leading (line-height)

- Body text: **120–145% of font size** (1.2–1.45 line-height)
  - 10pt body → 12–14pt leading
  - 12pt body → 14–17pt leading
- Headlines and display: **tighter**, often 100–110% (1.0–1.1)
- Wider measure → wider leading (35+ chars → 1.3, 65+ chars → 1.4, 75+ → 1.5)
- Captions and footnotes: match body leading proportionally

## Letter spacing (tracking)

- Lowercase body: **0 to –2%** (slightly tight for modern screens)
- UPPERCASE body: **+5% to +12%** — caps NEED air
- Small caps: **+8% to +15%**
- Display headlines: often **tight to negative** (–1% to –4%)
- Never track italic body text — italics are designed with their own rhythm

## Word spacing

- Should equal the width of a lowercase "t" roughly
- In justified text, keep min 85% / max 125% of natural spacing
- Ragged right generally reads better than bad justification

## Punctuation — use REAL glyphs, not keyboard substitutes

- Em dash — (U+2014) for parenthetical breaks
- En dash – (U+2013) for number ranges: 1998–2026
- Curly quotes " " ' ' — never straight "
- Ellipsis … (U+2026) — not three dots
- Proper apostrophe ' (U+2019) — not '
- Multiplication × (U+00D7) — not "x" letter
- Prime ′ and double prime ″ for feet/inches and minutes/seconds
- Non-breaking space (U+00A0) between figure and unit: "25 mm", "Dr. Smith"

## Hanging punctuation

- Quotation marks at beginning of paragraph should hang outside the text block
- Hyphens at line-end should hang into the margin slightly
- This preserves the optical edge of the text block

## Typographic scale

Use a **progression**, not arbitrary sizes. Classical scales:

- **6 : 7 : 8 : 9 : 10 : 11 : 12 : 14 : 16 : 18 : 21 : 24 : 36 : 48 : 60 : 72**
- **Double-stranded** (modular): 6 8 10 12 14 16 21 32 48 72
- **Fibonacci**: 8 13 21 34 55

Pick 5–7 sizes for a project. Do not use all sizes everywhere — hierarchy = restraint.

## Widows and orphans

- **Widow**: short last line of paragraph at top of next column. Kill it.
- **Orphan**: first line of paragraph alone at bottom of column. Kill it.
- Fix by: adjust tracking slightly (±0.5%), rewrite, reset break.

## Rivers

White streams running vertically through justified body. Caused by coinciding word spaces across lines. Tighten / break differently.

## Italic, bold, emphasis

- Italic for: titles, foreign words, emphasis (not the same use; don't mix in one paragraph)
- Bold for: reference words, key terms, UI labels
- ALL CAPS: extremely sparingly, only with tracking added
- **Never fake italics or bold** — use actual italic/bold cuts of the font
- **Never fake small caps** — most fonts don't have them; don't bastardize

## Hyphenation

- Avoid hyphens at: end of paragraph, end of right page (book), start of left page
- Do not hyphenate: names, acronyms, < 6-letter words
- No more than two consecutive hyphenated lines
- In narrow columns, hyphenation is necessary evil — tune threshold

## Type classification (know what you're pairing)

- **Old-style / humanist**: Garamond, Jenson, Centaur — diagonal stress, moderate contrast
- **Transitional**: Baskerville, Caslon — vertical-ish stress, sharper contrast
- **Modern / didone**: Bodoni, Didot — extreme contrast, flat serifs
- **Slab**: Clarendon, Rockwell, Museo Slab — thick slab serifs
- **Grotesque / sans**: Helvetica, Akzidenz, Univers, Inter, Arial — no serifs, geometric
- **Humanist sans**: Gill Sans, Frutiger, Lato — sans with calligraphic DNA

**Pairing rule**: contrast ONE dimension at a time. Classical serif + grotesque sans (contrast era & shape). Old-style + modern (same family but different eras → too close, confusing).

## Headlines and display

- Tighter leading (0.95–1.05)
- Tighter tracking (often negative)
- Larger size contrast with body (display 3–5× body size)
- Optional color OR weight, not both for emphasis

## Captions and footnotes

- Smaller than body (65–85% of body size)
- Same font FAMILY as body (usually same face, smaller)
- Italic sometimes, but not required
- Leading proportionally tighter

## Quick validation checklist (apply to any typesetting)

1. Is measure 45–75 chars per line? If no → resize or re-column.
2. Is leading 120–145% of body size? Loosen/tighten.
3. Are you using real glyphs (em-dash, curly quotes, ellipsis)?
4. Is there fake italic/bold/small-caps anywhere? Replace.
5. Does the type scale feel intentional (5–7 sizes from a progression)?
6. Any widows/orphans? Kill them.
7. Any rivers in justified text? Re-break.
8. ALL CAPS without extra tracking? Fix.

## Sources

- Bringhurst, Robert. *The Elements of Typographic Style*, Version 4.3. Hartley & Marks, 2016.
- Companion: Butterick, Matthew. *Practical Typography*. practicaltypography.com (free online, heavily Bringhurst-informed)

## Last sync

2026-04-18 — summarised from 4th edition for LLM application.
