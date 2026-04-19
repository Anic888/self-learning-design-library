# Style Locks — Constraint Tables per Style

*When a designer voice is chosen, these are the HARD STOPS that prevent the agent from mixing incompatible elements and producing AI-mush. Each lock says: "if you're working in style X, these elements are forbidden."*

## Why style locks exist

An LLM asked to "make a Hara-style poster with neon accents" will try to please both parts of the request. That produces incoherent work — Hara's restraint undone by accents that violate his entire philosophy. Style locks prevent this.

When the agent picks a primary style (from `style-profiles/`), it loads that style's lock table and HARD-REFUSES any trend / palette / technique from the incompatible list.

Locks are not about elimination of all trends — they allow compatible trends (see `## Compatible trend layers` in each lock) and only forbid combinations that destroy the style's identity.

---

## Kenya Hara

```yaml
FORBIDDEN:
  - neon colors (any saturated cyan, magenta, electric yellow)
  - gradients (except very subtle paper-to-paper)
  - drop shadows of any kind
  - bold display type in caps
  - more than 3 colors total in the composition
  - hard geometric ornamentation (stars, stripes, circles as decoration)
  - photography with dramatic chiaroscuro
  - any grunge / distress / noise texture
  - anti-design / brutalism
  - maximalist typography
  - dense information layouts
  - bento-grid with shadows (plain bento is OK)

REQUIRED:
  - 60%+ negative space (white or warm-white)
  - palette drawn from: warm whites, kraft, muted earth, near-black
  - type: quiet, widely tracked, never bold
  - silence-as-strategy — if in doubt, remove

COMPATIBLE trend layers:
  - Bento Grid (only flat, no shadows, kraft + near-black)
  - Dark Academia (classical serif, quiet)
  - Neo-Futurism / Spatial UI (only if monochrome base)
```

---

## Yoji Shinkawa

```yaml
FORBIDDEN:
  - color (except ONE oxblood red accent, < 5%)
  - gradients
  - digital-vector-clean lines
  - sans-serif modern grotesks (Helvetica etc)
  - neon / saturated palettes
  - bento grids
  - aurora / mesh gradients
  - acid graphics / iridescent
  - photographic realism

REQUIRED:
  - wet-brush aesthetic (visible strokes, varying width, ink bleed)
  - 60%+ rice-paper negative space
  - single subject dominance
  - if text present: small, classical serif OR absent entirely
  - red seal (kanji-style stamp) as signature

COMPATIBLE trend layers:
  - Dreamcore / Liminal (pastel wash in background only, figure stays ink)
  - Dark Academia (classical serif, muted palette)
  - Editorial Maximalism (type-forward with Shinkawa figure, only if figure stays mono)
```

---

## Peter Saville

```yaml
FORBIDDEN:
  - chaos typography / mixed-font-per-letter
  - hand-drawn / crafted feel
  - grunge / distress
  - loud commercial-sales typography
  - rainbow / hyper-saturated palettes
  - illustration-heavy compositions

REQUIRED:
  - classical or geometric typefaces (Baskerville, Bodoni, Garamond, Helvetica, Akzidenz)
  - generous margins
  - type minimal or absent
  - centered or off-center with discipline (never chaotic)
  - palette chosen from source artifact if appropriated
  - serial/catalog numbering (Factory FAC-### convention)
  - if photo present: appropriated / historical / scientific

COMPATIBLE trend layers:
  - Variable Bold Typography (Factory DNA)
  - Neo-Futurism / Spatial UI (frosted glass over classical image)
  - Aurora Mesh (only as background behind sharp white type)
  - Editorial Maximalism (restrained Saville variant)
```

---

## Paula Scher

```yaml
FORBIDDEN:
  - centered symmetric composition
  - uniform type size across the page
  - single typeface only
  - evenly distributed whitespace
  - quiet restraint as the primary strategy
  - palettes without one loud accent

REQUIRED:
  - asymmetric composition
  - type cropped aggressively (bleeds off edge)
  - 3+ typefaces clashing on purpose
  - scale-extreme (300pt next to 11pt on same comp)
  - ONE saturated accent (hot orange, electric blue, acid yellow)
  - cream / warm paper base preferred

COMPATIBLE trend layers:
  - Editorial Maximalism (natural fit)
  - Variable Bold Typography (type-as-image)
  - Anti-Design / Brutalism (when concept demands)
```

---

## David Carson

```yaml
FORBIDDEN:
  - grid-aligned composition
  - uniform, legible body text
  - classical serif body
  - "balanced" any meaning
  - corporate-clean finish
  - Swiss asymmetric (Carson's anti-Swiss)

REQUIRED:
  - intentional type disruption (overlap, partial crop, upside-down)
  - text-as-image (forget legibility sometimes)
  - grunge / collage / xerox texture
  - emotional not systematic
  - surface imperfections celebrated

COMPATIBLE trend layers:
  - Anti-Design / Brutalism
  - Editorial Maximalism (chaos variant)
  - Glitch / Datamosh
```

---

## Stefan Sagmeister

```yaml
FORBIDDEN:
  - template-driven look
  - absence of conceptual punchline
  - cold machine-slick finish
  - safe conventional layouts
  - design without ideology (beauty without meaning)

REQUIRED:
  - concept FIRST (idea precedes execution)
  - hand made / craft visible
  - humor or surprise
  - unusual material simulation (if SVG, imply texture through style)
  - typography from objects OR hand-drawn
  - big scale variation (huge vs tiny)

COMPATIBLE trend layers:
  - Editorial Maximalism
  - Risograph / Print Texture
  - Anti-Design (craft variant)
  - Dark Academia (classical meets craft)
```

---

## Refik Anadol

```yaml
FORBIDDEN:
  - warm paper backgrounds
  - classical serif typography
  - recognizable imagery (figures, landscapes, objects)
  - flat color fields
  - centered typographic posters
  - grunge / hand-made feel
  - craft aesthetics

REQUIRED:
  - deep-space base (#0E0428 / #1A0A3A)
  - neon saturation (cyan + magenta + yellow when in Mode 1)
  - point-cloud or flowing abstract forms
  - glow / bloom effects
  - sharp clean grotesk typography (SF Pro-esque)
  - architectural scale mindset

COMPATIBLE trend layers:
  - Aurora Mesh Gradient (native)
  - Neo-Futurism / Spatial UI
  - Glitch / Datamosh (abstract variant)
  - Variable Bold Typography (white on dark)
```

---

## James White / Signalnoise

```yaml
FORBIDDEN:
  - pure black backgrounds (use deep violet #1E0B3A instead)
  - minimalist palettes
  - classical serif typography
  - quiet / meditative mood
  - grunge / hand-made surfaces
  - flat-design vector
  - cool-only palettes (must have warm accent)

REQUIRED:
  - deep violet / indigo base
  - sunset gradient sky (magenta → purple → orange)
  - perspective grid floor
  - triangle framing device
  - 4-5 colors from synthwave canon
  - chrome or iridescent type treatment
  - grain / 80s tactility

COMPATIBLE trend layers:
  - Acid Graphics / Liquid Chrome (native)
  - Aurora Mesh (as sky field)
  - Variable Bold Typography (chrome titles)
```

---

## Josan Gonzalez

```yaml
FORBIDDEN:
  - negative space (zero — the whole point)
  - minimalist palettes
  - classical restraint
  - quiet typography
  - monochrome
  - polished corporate finish

REQUIRED:
  - 95%+ canvas coverage (everything packed)
  - deep purple-black base
  - neon pink + cyan + yellow triad
  - thick black outlines on everything
  - dense signage / writing / character details
  - cyberpunk subject matter

COMPATIBLE trend layers:
  - Glitch / Datamosh (native extension)
  - Maximalism (native)
  - Acid Graphics
```

---

## Ash Thorp

```yaml
FORBIDDEN:
  - saturated bright palettes
  - warm Mondo-ish colors
  - hand-drawn brushwork
  - cluttered maximalist layouts
  - chaos typography
  - neon / glitch
  - rainbow palettes

REQUIRED:
  - near-black deep base (#06090D)
  - off-white linework (#E8E8E8)
  - ONE warm accent (amber / orange, < 5% area)
  - hairline linework (0.3–0.8px)
  - massive negative space (40%+)
  - horizon-anchored composition
  - HUD-corners, tech-grid patterns
  - light tracked grotesk typography

COMPATIBLE trend layers:
  - Neo-Futurism / Spatial UI (native fit)
  - Dark Academia (quiet cold version)
  - Bento Grid (minimal variant only)
```

---

## Kilian Eng

```yaml
FORBIDDEN:
  - vector-flat aesthetics
  - pure digital slickness
  - minimalist modern
  - corporate clean
  - Helvetica-only typography
  - neon-only palettes

REQUIRED:
  - painterly rendering (never flat)
  - engraving / screen-print grain
  - 3 celestial bodies (Mode 1 signature)
  - ornamental border / frame
  - silhouetted tiny figure for scale
  - warm Mondo palette OR cold dark-fantasy palette OR monochrome engraving
  - horizon two-thirds down
  - CMYK-misregistration hint

COMPATIBLE trend layers:
  - Dark Academia (serif revival pairs natively)
  - Editorial Maximalism (Mondo-caliber layouts)
  - Dreamcore (darker cold-fantasy variant)
```

---

## Stefan Sagmeister (see above)

---

## Massimo Vignelli

```yaml
FORBIDDEN:
  - more than 6 typefaces (Vignelli's official 6: Akzidenz-Grotesk, Helvetica, Bodoni, Futura, Century, Garamond)
  - gradients
  - illustration flourishes
  - rainbow palettes
  - hand-drawn feel
  - asymmetric chaos (asymmetric yes, chaos no)
  - drop shadows
  - sans-serif body-text italics (rule: use italics in SERIF, oblique in sans)

REQUIRED:
  - strict grid discipline
  - 2-4 colors maximum
  - geometric precision
  - red Helvetica-bold accents (NYC subway DNA)
  - generous spatial hierarchy
  - black / red / cream / yellow palette family

COMPATIBLE trend layers:
  - Bento Grid (native — Vignelli basically invented modular layout)
  - Variable Bold Typography (Helvetica-forward variant)
  - Neo-Futurism (disciplined variant)
```

---

## Beeple

```yaml
FORBIDDEN:
  - minimalist palettes
  - vector-flat cleanliness
  - classical serif typography
  - quiet meditative mood
  - paper / tactile surfaces
  - pastel palettes

REQUIRED:
  - 3D-rendered feel (even as SVG simulation)
  - dystopian / satirical subject
  - garbage-aesthetic or corporate-horror mood
  - neon + grime combined
  - central subject in depressive environment
  - unsubtle cultural commentary

COMPATIBLE trend layers:
  - Glitch / Datamosh (native)
  - Dreamcore (darker variant)
  - Brutalism / Anti-Design
```

---

## Kenya Hara (see earlier entry)

---

## How the agent uses these locks

When `concept-explorer` subagent picks a designer + trend combo:

1. Load designer's lock table (this file, section for that designer)
2. Check: is the chosen trend in `COMPATIBLE trend layers`?
   - If YES → proceed, build concept
   - If NO → reject, pick different trend from compatible list
3. During SVG generation: validate no `FORBIDDEN` elements present
4. Validate all `REQUIRED` elements present

The `design-critic` uses the same table to score concepts. If a concept includes forbidden elements, the critic assigns -3 penalty per violation and likely rejects.

## How to extend

When adding a new designer to `style-profiles/`:
1. Build their lock table (FORBIDDEN / REQUIRED / COMPATIBLE)
2. Derive from their profile's "what to use" and "what to avoid" sections
3. Append here with the designer name as a `## Heading`

## Sources

- Each lock table derives from the designer's profile at `style-profiles/<slug>.md`
- Cross-referenced against the designer's known body of work
- Tested against the 6 reference posters in `my-works/showcase-themed-2026/`

## Last sync

2026-04-19
