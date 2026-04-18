# Quickstart — Make your first piece in 3 minutes

**For people who just want to create something cool, not read docs.**

This library lets an AI assistant (Claude, GPT) produce design work in the voice of a specific designer instead of generic AI slop. You describe what you want. The AI reads the matching style profile. You get a piece that looks like it was done by that designer — not by an LLM trying to please everyone.

---

## The 30-second mental model

```
YOU say:     "Make me a festival poster."
AI thinks:   "Which designer style? Which visual trend?"
AI reads:    style-profiles/<designer>.md  +  docs/trends-2026.md
AI produces: an SVG / PNG that looks like that designer working in that trend
```

Two knobs you turn:
1. **Designer style** — whose visual voice? (14 available — see [style-profiles/](style-profiles/))
2. **Visual trend** — what era/aesthetic? (see [docs/trends-2026.md](docs/trends-2026.md))

Everything else (palette, typography, composition rules) is already encoded in the profile.

---

## Path A — Ask Claude / GPT directly (no install, no code)

Open Claude or ChatGPT, paste this template, fill in the blanks:

```
I'm using the design library at github.com/Anic888/self-learning-design-library.

Read style-profiles/<DESIGNER-SLUG>.md and produce an SVG for:
  <WHAT YOU WANT>

Trend flavor: <TREND FROM docs/trends-2026.md>
Format: <poster / landing hero / book cover / album art / etc.>
Size: <e.g. 1200x1600 for poster>
```

### Five ready-to-paste recipes

**1. Clean product landing hero (Apple-clean, bento-grid, 2026)**
```
Read style-profiles/kenya-hara.md.
Produce an SVG 1440x900 — hero section for a wellness app called "Stilla".
Trend: bento grid (see docs/trends-2026.md). Generous white, kraft accents,
one near-black headline, three cards, subtle texture.
```

**2. Synthwave festival poster with acid-graphics twist**
```
Read style-profiles/james-white-signalnoise.md.
Produce an SVG 612x792 — poster for a music festival called "Neon Horizon".
Trend: acid graphics — liquid chrome type, iridescent gradient, 80s sunset.
Chrome serif masthead, perspective grid floor, sun circle top.
```

**3. Editorial magazine spread with maximalist typography**
```
Read style-profiles/paula-scher.md.
Produce an SVG 2000x1333 — magazine spread opener for an article on AI art.
Trend: editorial maximalism. Cropped type bleeds off page, hot orange + black,
four type sizes clashing on purpose, no centered blocks.
```

**4. Meditative ink piece (Japanese restraint, minimal accent)**
```
Read style-profiles/yoji-shinkawa.md.
Produce an SVG 1400x2000 — cover for a novella called "River of Ash".
Trend: minimalism + analog texture. Bone-white paper, single wet-brush figure,
one oxblood red kanji seal bottom-right. 60% negative space.
```

**5. Dense cyberpunk key art with dreamcore glitch**
```
Read style-profiles/josan-gonzalez.md.
Produce an SVG 1920x1080 — key art for a cyberpunk game called "Neo-Kyoto 2089".
Trend: dreamcore + glitch. Packed illustration, neon pink + cyan + yellow,
RGB split chromatic aberration, signage everywhere, zero negative space.
```

**Tip:** The more specific you are about the subject, the better. "A poster" is vague. "A poster for a 3-day synthwave festival headlined by Carpenter Brut and The Midnight, held in an abandoned Tokyo shopping mall" is a brief.

---

## Path B — Use the CLI (for repeatability)

If you want prompts / images at the command line:

```bash
# Install once
uv sync --directory tools/

# See what styles you have
uv run tools/generate.py --list-styles

# Build a prompt (no API key needed)
uv run tools/generate.py "festival poster" --style james-white-signalnoise --prompt-only

# Generate with HuggingFace (needs HF_TOKEN)
uv run tools/generate.py "dark alley at night" \
  --style ash-thorp --camera arri-alexa --lighting chiaroscuro \
  --film-stock cinestill-800t --filter "grain,vignette"

# Combine two styles
uv run tools/generate.py "book cover" --style "kenya-hara+yoji-shinkawa" --size 2K
```

Full tool reference: `uv run tools/generate.py --help`
Cinematography options: `uv run tools/generate.py --list-cinema`

---

## How to pick a designer for the job you have

| You're making… | Try one of these |
|---|---|
| Festival / gig poster | james-white-signalnoise, kilian-eng, josan-gonzalez |
| Book / album cover, minimalist | kenya-hara, yoji-shinkawa, massimo-vignelli |
| Magazine / editorial spread | paula-scher, david-carson, stefan-sagmeister |
| Product landing / SaaS hero | kenya-hara, massimo-vignelli, peter-saville |
| Game / film key art | ash-thorp, syd-mead, josan-gonzalez, kilian-eng |
| AI-era / data-driven visuals | refik-anadol, beeple |
| Anti-corporate / rebellious | david-carson, stefan-sagmeister |
| Industrial / sci-fi realism | syd-mead, ash-thorp |

Combine two when you want a hybrid (`--style ash-thorp+david-carson`). Profiles are designed to mix without turning to mush — see [my-works/showcase-2026-04/08-combination-test.svg](my-works/showcase-2026-04/08-combination-test.svg).

---

## How to pick a visual trend

Short cheatsheet — full breakdown in [docs/trends-2026.md](docs/trends-2026.md):

| Trend | One-liner | Good on |
|---|---|---|
| **Bento grid** | Modular card layouts, Apple-clean | Product pages, dashboards |
| **Aurora / mesh gradient** | Soft blurred color clouds | AI tools, landing heroes |
| **Editorial maximalism** | Cropped type, asymmetric, magazine-feel | Articles, posters, covers |
| **Acid graphics** | Liquid chrome, iridescent, Y2K-adjacent | Music posters, fashion |
| **Anti-design / brutalism** | Raw HTML, intentionally unpolished | Rebellious brands, art |
| **Dreamcore / liminal** | Eerie, nostalgic, AI-era uncanny | Art, speculative fiction |
| **Solarpunk** | Optimistic nature + tech, warm greens | Sustainability, indie |
| **Bold variable type** | Oversized, morphing, kinetic | Editorial, tech brands |
| **Risograph print** | Grainy 2-color, tactile | Indie, music, zines |
| **Neo-futurism / spatial** | Glass, depth, Vision-Pro feel | Premium tech |

---

## What to do with the output

The AI gives you SVG (vector, editable) or PNG (raster, final). Both land in `my-works/<date>-<slug>/`.

- **SVG** opens in any browser, editable in Illustrator / Figma / Inkscape. Great for print — infinite resolution.
- **PNG** is the final export — share-ready, but fixed size.

Browse [my-works/showcase-2026-04/](my-works/showcase-2026-04/) for 8 reference pieces, and [my-works/showcase-2026-04-trends/](my-works/showcase-2026-04-trends/) for the trend-flavored examples.

---

## When output disappoints

If the first result feels generic:
1. **Add more specifics to the brief** — concrete subject, setting, props, mood adjectives
2. **Pick a more distinctive style** — Hara is restrained; if you want punch, try Josan or Scher
3. **Lock in a trend flavor** — AI defaults to mush; trends force a direction
4. **Ask for an SVG first, then refine** — editing vector is cheaper than regenerating PNG

The profiles exist to make LLMs *follow rules they'd otherwise ignore*. If output looks generic, the rules aren't being read — re-paste the profile path explicitly.

---

Next:
- Full style profiles → [style-profiles/](style-profiles/)
- Trend reference → [docs/trends-2026.md](docs/trends-2026.md)
- Reference works → [my-works/showcase-2026-04/](my-works/showcase-2026-04/)
- Tool details → [SETUP.md](SETUP.md)
