# Showcase — April 2026: Designer style × 2026 visual trend

> Proof that designer profiles compose cleanly with contemporary visual trends. Each piece = one designer voice × one trend flavor. The designer profile fixes palette, composition, typographic voice. The trend adds the 2026 finish.

These four pieces are the reference for [docs/trends-2026.md](../../docs/trends-2026.md). Compare them against [showcase-2026-04/](../showcase-2026-04/) — same designer voices, different era.

## The four pieces

| # | Work | Designer profile | 2026 trend |
|---|---|---|---|
| 01 | `01-hara-bento.svg` | [kenya-hara.md](../../style-profiles/kenya-hara.md) | [Bento Grid](../../docs/trends-2026.md#1-bento-grid) |
| 02 | `02-signalnoise-acid.svg` | [james-white-signalnoise.md](../../style-profiles/james-white-signalnoise.md) | [Acid Graphics / Liquid Chrome](../../docs/trends-2026.md#4-acid-graphics--liquid-chrome) |
| 03 | `03-scher-maximalism.svg` | [paula-scher.md](../../style-profiles/paula-scher.md) | [Editorial Maximalism](../../docs/trends-2026.md#3-editorial-maximalism) |
| 04 | `04-josan-glitch.svg` | [josan-gonzalez.md](../../style-profiles/josan-gonzalez.md) | [Glitch / Datamosh Revival](../../docs/trends-2026.md#12-glitch--datamosh-revival) |

## What each one demonstrates

### 01 — Hara × Bento: quiet luxury for software

A wellness app landing hero. Hara's palette (warm white, kraft, near-black) is already the 2026 quiet-luxury direction. Bento grid shapes it into the current modular hero format without losing Hara's discipline: no shadows, hairline dividers, one kraft accent card, generous white around the grid. Type is Hara's — light grotesk, widely tracked, near-black.

**What would kill the look:** drop shadows on cards, saturated accent colors, bold type, centered hero image over the grid.

### 02 — Signalnoise × Acid Graphics: synthwave with liquid chrome

A festival poster. Signalnoise already has synthwave DNA: deep violet (never pure black), sunset gradient, perspective grid floor, triangle masthead framing. Acid graphics pushes the finish forward — warped iridescent chrome on the display type, floating iridescent orbs, plausible-impossible reflections — without touching the composition. The result reads as 2026 revival, not 1984 pastiche.

**What would kill the look:** flat solid-color type (chrome is mandatory), pastel backgrounds, matte finishes, centered symmetric horizon.

### 03 — Scher × Editorial Maximalism: magazine opener that screams

A 2-page magazine spread. Scher's rules are already maximalist: type-as-image, cropped aggressively, hot orange as the signature accent, multiple typefaces in a single comp. Editorial maximalism amplifies the cropping to bleed-off-page, pushes type-size contrast to extreme (300pt vs 11pt on the same page), and forces asymmetric spans. Body column is deliberately tiny so the display dominates.

**What would kill the look:** centered symmetric layout, uniform type size, single font family, evenly distributed whitespace, a single hero image.

### 04 — Josan × Glitch / Datamosh: cyberpunk key art for the AI era

Game key art. Josan is already zero-negative-space cyberpunk maximalism — buildings, signs, wires, neon. Glitch/datamosh adds the 2026 layer: RGB channel split on the masthead, CRT scanlines, HUD overlay with timestamp, a datamosh smear band across the upper-right. The mood shifts from "dense cyberpunk city" to "dense cyberpunk city as corrupted memory" — which is the contemporary read.

**What would kill the look:** clean vector, centered hero with negative space, minimalist palette, sans-serif modern display type in the title.

## How to use these as your own starting points

Each SVG is heavily commented. Open them in any text editor to see:
- Which hex codes are Hara/Signalnoise/Scher/Josan-native (palette lock)
- How the trend layer is structured (gradients, filters, overlays)
- Which composition rules are enforced (grid dimensions, crop lines, perspective)

To adapt: swap the subject-specific text, keep the structural decisions. Don't swap the palette — that's the designer voice.

Or ask Claude / GPT: *"Read `style-profiles/<designer>.md` and the trend section in `docs/trends-2026.md`. Produce an SVG for [your subject]. Use `my-works/showcase-2026-04-trends/<reference>.svg` as the structural template."*

## Why this compositional approach matters

> A designer profile alone gives you a voice. A trend alone gives you an era. You need both.
>
> - **Profile alone:** "just Hara" reads like 2018 Japanese minimalism — correct, but dated.
> - **Trend alone:** "just bento" reads like every 2024 SaaS hero — on-trend but anonymous.
> - **Both:** Hara voice × bento format = a 2026 piece with a recognizable author.

That's the whole argument of this library. These four pieces are the proof.
