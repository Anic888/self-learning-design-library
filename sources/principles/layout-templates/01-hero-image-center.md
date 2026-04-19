# Template 01 — Hero Image Center

*Single dominant central image carries the communication. Type frames it above and below. Classical movie-poster / art-gallery / book-cover lineage.*

## When to use

- **Cinema** — alternative movie posters (Mondo tradition)
- **Games** — key art posters
- **Art exhibitions** — museum posters
- **Book covers** for literary / genre fiction
- **Theater** productions
- **Music** when the artist portrait is the visual

Do NOT use when:
- Subject is abstract / conceptual (use Template 02 Type-as-Image or 04 Field)
- Product is the object itself (use Template 03 Object-Bleed)
- Tech conference / AI event (use Template 04 Field)

## Grid plan

```
viewBox: 612 × 888 (Mondo-adjacent vertical)
Outer frame: x=28→584, y=28→860 (stroked thin rule)
Safe content zone: x=56→556 (500 wide)
Top margin: 28 (frame) + 28 (internal) = 56
```

## Vertical zones

| y-anchor | Zone | Content |
|---|---|---|
| y=56 | Top meta line | Studio/publisher left, catalog/ID right |
| y=68 | Hairline | — |
| y=86–155 | Title block | Over-title (small italic), main title (large), subtitle |
| y=176–706 | **HERO IMAGE** (530 tall) | Central scene, clipped inside inner frame rect |
| y=728 | Mid-ornament divider | Decorative rule OR plain |
| y=748–784 | Tagline block | 3 italic lines with drop cap |
| y=814 | Cast / credits billing | One line, bold small caps |
| y=836 | Micro credits | Italic single line |
| y=862 | Studio edition marks | Small-caps, split left/right |
| y=876 | Frame bottom | Outer rule ends |

## Required content blocks

1. **Top meta line** (y=56): institution + catalog
2. **Main title** (y=140 or similar, size 60–72pt): the work's name
3. **Subtitle** (y=161): supporting descriptor
4. **Hero image** (y=176–706): the central scene
5. **Cast / primary credits** (y=814): performers / authors / key names
6. **Footer credits** (y=836+)

## Optional content blocks

- Over-title above main title (y=96): "A FILM BY X" / "AN EXHIBITION AT Y"
- Ornamental corner fleurons at frame corners
- Tagline with drop cap (y=748–784)
- Micro credits second line
- Oxblood seal (bottom-right, East-Asian style — Shinkawa DNA)

## Compatible style profiles

- **Kilian Eng** — Mondo Mode 1 (warm) or Mode 3 (dark fantasy) natively
- **Peter Saville** — when hero is appropriated classical image
- **Yoji Shinkawa** — single ink figure as hero
- **Ash Thorp** — cold atmospheric tech scene as hero
- **Syd Mead** — industrial / sci-fi vehicle as hero
- **Josan Gonzalez** — dense cyberpunk scene as hero (but push safe zones further — Josan = 95% coverage)

## Compatible trend layers

- **Dark Academia** — classical serif type, warm paper, oxblood drop cap
- **Dreamcore / Liminal** — muted pastel wash in hero, sparse figure
- **Neo-Futurism** — frosted glass card over image
- **Editorial Maximalism** — scale-extreme type block
- **Acid Graphics / Liquid Chrome** — chrome title over Mondo-style hero

## Example reference posters

- [`01-cinema-arrakis.svg`](../../../my-works/showcase-themed-2026/01-cinema-arrakis.svg) — Kilian Eng × Dark Academia applied to this template
- [`02-art-aftermachine.svg`](../../../my-works/showcase-themed-2026/02-art-aftermachine.svg) — Saville × Neo-Futurism (hero image + frosted card variant)
- [`04-games-ashfall.svg`](../../../my-works/showcase-themed-2026/04-games-ashfall.svg) — Shinkawa × Dreamcore

## Variant: with frosted card overlay

If using Neo-Futurism trend, add a floating frosted-glass panel partially overlapping the bottom third of the hero image, carrying the title and key metadata. See `02-art-aftermachine.svg` for full structure.

```
y=552–716: frosted glass card (160 tall, rounded 24px, rgba(252,250,245,0.92))
  contains: iridescent mark, title, subtitle, dates, curator info
```

This variant is especially strong for art exhibitions and premium cultural events.

## Anti-patterns for this template

- Multiple hero images competing (pick ONE)
- Hero image edge-to-edge (frame is load-bearing here)
- Tiny hero image with giant title (that's Template 02 Type-as-Image)
- Title BELOW hero image without a top anchor (makes it read bottom-heavy)

## Sources

- Mondo Tees 20-year catalog (2004–2024)
- Criterion Collection cover archive
- Penguin Classics cover conventions

## Last sync

2026-04-19
