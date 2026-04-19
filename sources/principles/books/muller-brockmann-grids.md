# Müller-Brockmann — Grid Systems in Graphic Design

*Josef Müller-Brockmann, 1981. The Swiss-school grid bible. These are the LLM-actionable rules for grid construction — not the manifesto.*

## Grid types — pick ONE before drawing anything

- **Manuscript grid**: single text block, one column. Use for: novels, long-form essay, single-image poster. Simplest possible.
- **Column grid**: 2–6 vertical columns. Use for: magazines, newsletters, editorial spreads, multi-column posters.
- **Modular grid**: columns × horizontal rows = cells ("modules"). Use for: catalogs, data-heavy layouts, complex posters with image + text blocks.
- **Hierarchical grid**: irregular, optically-balanced, no uniform module. Use for: web pages, landing pages, single-use layouts where content dictates structure.

**Rule:** Never invent a grid per element. Fix the grid first, populate second.

## Column grid — construction math

- **Margins**: outer margins larger than inner (asymmetric book spreads). For posters: 1:1 margin all sides or top < bottom (caption foot heavier).
- **Gutter width**: minimum = leading of body text (so baselines align across columns). Typical: **12–24pt** for print, **16–32px** for screen.
- **Column count for A-series / posters**:
  - A4, A3, A2 portrait: **6 or 8 columns** (6 for editorial, 8 for denser)
  - A2, A1 landscape posters: **8 or 12 columns**
  - A0 wall posters: **12 or 16 columns**
- **Column count for web**: **12 columns** is canonical (divisible by 1, 2, 3, 4, 6).
- Columns must be of equal width. Unequal columns = hierarchical grid, not column grid.

## Baseline grid — the invisible skeleton

- **Rule:** Every line of body text sits on a baseline. Every baseline sits on the grid.
- Baseline spacing = body leading (e.g., 12pt type, 14pt leading → 14pt baseline grid).
- Images, captions, headings all snap to baseline multiples (not arbitrary positions).
- Multi-column text: baselines must ALIGN across columns — reader's eye tracks horizontally.
- Break baseline only for display type / titles / image captions if optically required.

## Module — the atomic unit

- **Module = one cell of the grid** (one column width × one baseline-grid row subset).
- A column is a vertical stack of modules. A field is N × M modules grouped for content.
- Field sizes available: **1×1, 1×2, 2×2, 2×3, 3×3, …** — always integer multiples.
- **Rule:** Image sizes, text block heights, and captions all conform to module multiples.

## Grid vs. paper format

- **A-series (ISO 216)**: ratio 1:√2 ≈ 1:1.414. Halving folds preserve proportion. Use for: European editorial, books, posters.
- **US letter (8.5×11)**: ratio ≈ 1:1.294. Slightly squarer. Use for: US corporate.
- **Poster standards**:
  - B1 (707×1000mm), A1 (594×841mm): 8 or 12 columns
  - US 24×36": 12 columns standard
- **Rule:** Choose grid columns so margin + (columns × column width) + ((columns-1) × gutter) = page width exactly. No leftover fractions.

## Typographic grid vs. image grid

- **Typographic grid**: baseline + column — governs text. Strict.
- **Image grid**: module-based — images occupy integer module counts (1×1, 2×3, etc.).
- **Rule:** Both grids share the same column and gutter structure. Only baseline-row subdivision differs per use.
- Images that bleed to edge: break the margin deliberately for emphasis, never accidentally.

## When to break the grid (almost never)

- **Rule:** Break the grid ONLY for hierarchy — to flag the single most important element.
- One broken element per layout maximum. Two = chaos, zero = rigid.
- Acceptable breaks: oversized display number, full-bleed hero image, angled title.
- **Forbidden:** breaking the grid because "it looks better" — that means your grid is wrong. Redesign the grid.

## Swiss-school conventions (the house style)

- **Sans-serif only** for headings and body (Akzidenz Grotesk, Helvetica, Univers, Neue Haas Grotesk).
- **Left-alignment (ragged right)**; justified only for long-form or specific editorial use.
- **Asymmetric balance**: off-center composition, weight distributed via tension, not mirroring.
- No decorative ornament. No drop-shadows. No gradients. Solid colors, flat shapes.
- **Black, white, red, one accent** — the classic Swiss palette. Expand only with reason.
- Numbers and dates align on decimal / baseline — tabular figures preferred.

## Common grid ratios and canons

- **8-column grid**: poster / editorial workhorse. Divisible into 2, 4, 8.
- **12-column grid**: most flexible; supports 2, 3, 4, 6-column fields. Web standard.
- **16-column grid**: data-dense layouts, infographic posters.
- **Golden section (1 : 1.618)**: apply to page proportions, image crops, column/sidebar ratio.
- **Van de Graaf canon**: medieval book canon. Text block = 2:3 of page. Inner margin : top : outer : bottom = **2 : 3 : 4 : 6**.
- **Rule of thirds**: cheap approximation of golden section — acceptable but less elegant.

## Hierarchy within the grid

- Hierarchy via **size, weight, space** — in that order of preference.
- Body text: 9–11pt. Subheadings: 12–14pt. Headings: 24–48pt. Display: 72pt+.
- White space is a hierarchy tool. More space around an element = more importance.
- **Rule:** Never use more than 3 hierarchy levels per layout (H1, H2, body). Four = clutter.

## Color and the grid

- Grid is invisible. Color reveals structure only when deliberate.
- Block of color = module or field multiple. No half-modules of color fill.
- Red accent on Swiss grid: 1 element only, 5–15% of total area.

## Images on the grid

- Crop to module boundaries. Edges hit column or baseline-row lines.
- Image width = N columns exactly (never 3.5 columns).
- Image height = M baseline units exactly.
- Whitespace above/below image = minimum 1 baseline unit.
- **Rule:** If the image doesn't fit the grid at the right size, either resize the grid or recrop the image. Never "almost" snap.

## Quick validation checklist (apply to any grid layout)

1. Is the grid type named (manuscript / column / modular / hierarchical)? If not → pick one.
2. Do all baselines align across columns? If no → fix leading or gutter.
3. Do images/blocks occupy integer module counts (no fractional widths)? Fix crops.
4. Are there more than 3 hierarchy levels? Simplify.
5. Is text left-aligned (or justified with tight rivers)? Reconsider.
6. Is there exactly 0 or 1 deliberate grid break? Two+ = redesign.
7. Do margins sum + gutters + columns = full page width exactly? No leftover mm.
8. Is color restricted to 2–4 hues, with accent ≤ 15% area?

## Sources

- Müller-Brockmann, Josef. *Grid Systems in Graphic Design / Raster Systeme für die visuelle Gestaltung*. Niggli, 1981 (reprinted 2020).
- Companion: Hurlburt, Allen. *The Grid*. Van Nostrand Reinhold, 1978.
- Companion: Samara, Timothy. *Making and Breaking the Grid*, 2nd ed. Rockport, 2017.

## Last sync

2026-04-19 — summarised for LLM application.
