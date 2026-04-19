# Structural Variance — 12 Compositional Archetypes

*When the design-creator agent picks a layout, it must choose from these archetypes AND rotate — no two consecutive posters should share an archetype. Extracted from Pinterest design-poster boards, typographicposters.com archive, my-works/ references, and the catalog at sources/research/poster-catalog/.*

---

## Why this file exists

User feedback after 3 consecutive posters (Digital Loneliness / Burn the Night / LAST SIGNAL v1): structurally identical despite palette/subject variation. Each used:
- Thin hairline outer frame (28/28/556/832)
- Top-meta line split L/R with catalog number
- Hero zone → divider rule → typography block → footer
- "Brutalist research annotations" (SUBJECT/01, SPEED 247 km/h, SIGNAL 4%)
- Footer split L/R with catalog date + studio

That is ONE archetype. Real posters span many more. This file defines 12, with explicit rotation rules.

## The 12 archetypes

### 1. Classical Centered Hero
**Skeleton:** outer frame rule (thin) + top meta + hero image/scene above + type below (title-subtitle-credits) + footer split.
**When:** cinema, theater, book covers, museum shows — institutional / formal.
**Reference in catalog:** Kilian Eng "Blade Runner 2049" (illustration-posters.md), ARRAKIS: THE SILENT SUN (my-works/01-cinema-arrakis.svg).
**Avoid:** anything casual, punk, or anti-design.

### 2. Full-Bleed Atmospheric (no frame, no margins)
**Skeleton:** edge-to-edge atmosphere/color field + minimal elements placed in asymmetric negative space + 1-2 text elements only, no HUD, no frame.
**When:** silence, mystery, contemplative, cosmic, emotional singularity.
**Reference:** LAST SIGNAL v2 (my-works/2026-04-19-last-signal/), Saville "Closer" Joy Division (photo-based-posters.md).
**Avoid:** don't add frame, don't add meta, don't add catalog split — the whole point is removal of frame-type decoration.

### 3. Type-as-Image Monumental
**Skeleton:** single word or numeral at 300-550pt dominates 60%+ of canvas; everything else vestigial. Could be cropped off edge (Paula Scher Public Theater) or symmetrically monumental (Kompakt 25).
**When:** anniversaries, label identity, concept posters, event posters with strong verbal punchline.
**Reference:** Vignelli NYC Subway (type-only-posters.md), Paula Scher Public Theater (1994-present), Kompakt 25 (my-works/06-music-kompakt-25.svg).
**Avoid:** don't dilute with hero image — the type IS the image.

### 4. Object-Bleed Hybrid
**Skeleton:** single iconic object cropped off one edge (usually right) + text column in the clear quadrant + tracklist / feature list below.
**When:** album covers featuring physical artifact (vinyl, cassette), product launch posters, museum object features, symbolic-artifact posters.
**Reference:** Blue Nothing vinyl (my-works/03-music-blue-nothing.svg), Eiko Ishioka "Dracula" (1992).
**Avoid:** centering the object. The asymmetry IS the point.

### 5. Constructivist Diagonal
**Skeleton:** angular / diagonal composition with asymmetric energetic elements; type interacts with image at angles (not horizontal-above / horizontal-below); primary axis is 20-45° from horizontal.
**When:** propaganda-heavy / manifesto / rebellion / sports / motion subjects.
**Reference:** Rodchenko "Kino-Glaz" (1924, 1920s-constructivism.md), Stenbergs film posters, Lissitzky "Beat the Whites with the Red Wedge" (1919).
**Avoid:** trying to center anything. No symmetric layouts.

### 6. Figure + Vast Negative Space
**Skeleton:** subject placed in extreme corner or third (10-15% area) + 70%+ negative space + minimal type in opposite quadrant.
**When:** isolation, contemplation, solo subjects, stillness.
**Reference:** Tomaszewski "Henry Moore" (1960s-polish-school.md), Shinkawa ink figures (illustration-posters.md).
**Avoid:** filling the negative space. It IS the point.

### 7. Typography-Centered Chaos (Scher / Carson lineage)
**Skeleton:** multiple type elements overlapping, different sizes + colors + angles, layered composition. NOT grid-aligned.
**When:** editorial covers, anti-corporate events, youth-culture, music that's loud/confrontational.
**Reference:** Carson Ray Gun spreads (1990s-grunge-digital.md), Scher Public Theater Noise/Funk, 1990s The Face Brody.
**Avoid:** cleanliness. If it reads polite, it's failed.

### 8. Minimalist Landscape Reduction
**Skeleton:** tiny scene (small cabin, single tree, horizon line) positioned in upper or lower third; rest is flat color; minimal type (often 1 element).
**When:** travel, outdoor gear, conservation, wellness.
**Reference:** James Cropper, Stanley Donwood (Radiohead), Swiss modernism simplified variants.
**Avoid:** adding complexity. The scene must be reducible to 3-5 shapes.

### 9. Badge / Cluster Grid
**Skeleton:** multiple contained units arranged in grid (3x3, 2x4, asymmetric clusters); each unit is a badge/circle/square with contained text.
**When:** identity systems, event programs, catalog covers, collection overviews.
**Reference:** AIGA 50/50 covers, Pentagram identity work, Kontrapunkt FC København season guide (2024-2026-contemporary.md).
**Avoid:** one big hero — this is about modular repetition.

### 10. Wrapping / Flowing Type
**Skeleton:** type flows around an image silhouette, follows curve of object, or wraps a shape. Not rectangular type blocks.
**When:** fashion, poetry, book covers, art-magazine spreads.
**Reference:** Neville Brody The Face typography treatments (1990s-grunge-digital.md), Balenciaga campaigns 2024-2026, Rick Owens Temple of Love (2024-2026-contemporary.md).
**Avoid:** rigid horizontal baselines.

### 11. Vertical Stack / Rotated
**Skeleton:** type runs vertically along one edge of canvas (left or right); image or secondary type fills rest. Often with Japanese / East-Asian composition influence.
**When:** Japanese theater, martial arts, meditation, traditional-meets-modern subjects.
**Reference:** Yokoo Koshimaki-Osen (MoMA, 1970s-japanese.md), Tanaka Nihon Buyo (1981), Kazumasa Nagai work.
**Avoid:** using vertical type as decoration — it must be the primary read-direction.

### 12. Anti-Design Raw / Web Brutalism
**Skeleton:** default system fonts (Times New Roman, Arial, Courier); underlined blue links; default button styles; no frame refinement; intentionally unpolished; raw HTML look.
**When:** art collectives, rebellious brands, anti-establishment campaigns, intentionally counter-cultural events.
**Reference:** Balenciaga 2024 raw-HTML promotional, Rick Owens stark campaign posters, contemporary brutalist web inspirations from Awwwards SOTD (awwwards-sotd-2024-2026.md).
**Avoid:** polishing it. If it looks "designed," it's failed.

---

## Rotation rules (MANDATORY for design-creator)

Before rendering any new poster, consult `memory/winning-concepts.json`:

1. **Read the last 3 winning-concept entries** — note their archetype.
2. **Do NOT reuse any of those 3 archetypes** unless the brief explicitly demands classical-centered hero (e.g. "traditional cinema poster").
3. **Pick an archetype that opposes the previous** — if last 3 were all 2/6 (atmospheric/negative-space), next must be 3/5/7 (type-monumental / constructivist / chaos).
4. **Justify the archetype choice in the concept JSON** under `structural_archetype` field with 1 sentence grounding in brief.

## Forbidden recurring signatures (my own crutches)

These are patterns I (Claude) tend to add regardless of brief. NOT USE unless brief SPECIFICALLY demands research-poster / HUD / technical-manual aesthetic:

- ❌ "SUBJECT / 01" style labels with tiny text
- ❌ Mission-telemetry annotations (SPEED, SIGNAL, O₂, D/EARTH, etc.)
- ❌ Coordinate rings circling the subject
- ❌ "CAT · XXX-001 / DATE" split footer
- ❌ "A POSTER STUDY" / "FIG. I" research-paper annotations
- ❌ Thin hairline outer frame at exactly 28,28,556,832
- ❌ Top-meta line split L/R with studio-left + catalog-right
- ❌ Hero-zone → divider rule → type-block → split-footer sequence
- ❌ Letter-spacing over 8 for body text
- ❌ Multiple italic elements stacked (over-title italic + subtitle italic + tagline italic)

**Use ONLY if the brief contains keywords like: "research poster", "manifesto", "scientific", "technical manual", "data-dense", "infographic", "specification sheet", "medical chart".** For all other subjects, OMIT these crutches.

## How to diverge: concrete escape hatches

If you catch yourself defaulting to archetype #1 Classical Centered Hero:
- **Drop the frame** — go full-bleed → archetype #2
- **Drop the hero image** — use type-only → archetype #3
- **Drop the centering** — shift subject to corner → archetype #6 or #10
- **Drop the top-meta** — start with image or type → all non-classical archetypes
- **Drop the footer split** — single centered credit or no footer → archetype #2 / #8 / #12
- **Add angle** — rotate composition → archetype #5
- **Add chaos** — overlap type layers → archetype #7

## Cross-reference

- Previous layout templates: [`sources/principles/layout-templates/`](../layout-templates/) (4 files — now treat as archetypes 1-4 here, expanded with 8 more)
- Poster catalog by era: [`sources/research/poster-catalog/by-era/`](../../research/poster-catalog/by-era/)
- Poster catalog by technique: [`sources/research/poster-catalog/by-technique/`](../../research/poster-catalog/by-technique/)
- Design-creator skill: `~/.claude/skills/design-creator/SKILL.md`

## Last sync

2026-04-19 — created after user feedback that 3 consecutive posters were structurally identical. Baseline of 12 archetypes derived from Pinterest graphic-design-posters board, design-library catalog entries, and Paul Rand / Müller-Brockmann / Hara composition principles.
