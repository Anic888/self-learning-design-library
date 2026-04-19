# Template 04 — Field-Over-Hero

*Atmospheric color field or data formation is the hero image. Sharp typography sits on top as information architecture. Anadol, aurora gradients, cyberpunk atmospheric, AI-era tech events.*

## When to use

- **Tech / AI conferences**
- **Data-visualization as art** presentations
- **Abstract-subject** posters (ideas, not things)
- **Rave / electronic music** events with immersive atmosphere
- **Art installations** that are themselves fields of color
- **Product launches** that are about experience, not artifact

Do NOT use when:
- Subject is a specific person / object / scene (use Template 01 or 03)
- Typography must be the star (use Template 02)
- Viewer needs to SEE a thing (this is abstract-only)

## Grid plan

```
viewBox: 612 × 888 (vertical poster) OR 1920 × 1080 (horizontal banner)
Outer frame: x=28→584, y=28→860 (thin white/neutral rule, stroke-opacity 0.5)
Safe content zone: x=56→556
Background: full-bleed (no paper base — field fills everything)
```

## Vertical zones

| y-anchor | Zone | Content |
|---|---|---|
| y=56 | Top meta line | Event name left, volume/catalog right (white on dark) |
| y=68 | Hairline (white, 0.4 opacity) | — |
| y=90–540 | **FIELD HERO** (450 tall) | Aurora / point cloud / particle field |
| y=594 | Title (massive grotesk, white) | Event name, font-size 64-72pt, font-weight 800 |
| y=638 | Year or secondary | Contrasting weight, often saturated accent color |
| y=654 | Rule (white, short, opacity 0.5) | — |
| y=676 | Subtitle | Clean grotesk, wider tracking |
| y=708 | Date line (saturated accent) | "11 · 12 · 13 JUNE 2026" in yellow or cyan |
| y=728 | Location | Lowercase grotesk, subtle |
| y=750 | Feature header | "SPEAKERS" or similar in accent color |
| y=776–836 | 3-col × 2-row grid | 6 names with affiliations |
| y=850 | Footer hairline | — |
| y=860 | Footer | URL / copyright / registration info |

## Field construction

### Variant A — Aurora Mesh (Anadol / 2026)

Multiple radial gradients with heavy Gaussian blur (stdDeviation=36), overlapping:
- Magenta bloom upper-left
- Cyan bloom upper-right
- Yellow bloom lower-center
- Violet unifier bloom (large, low opacity, covers all)
- Secondary smaller magenta for complexity

Deep-space base color: `#0E0428` or `#1A0A3A`
Saturated bloom colors: magenta `#F72585`, cyan `#00D9FF`, yellow `#FFEE00`, violet `#7B4AFF`

### Variant B — Point Cloud (Anadol canonical)

Over the aurora mesh, add hundreds of white dots (radius 0.5–2.2px, opacity 0.4–1):
- Dense center cluster (~20 dots)
- Outer flowing arcs (~20 dots forming curves)
- Scattered ambient particles (~40 dots across field)
- 4-6 bright anchor points with glow filter
- Optional: thin white filament lines at 0.25 opacity connecting clusters

### Variant C — Scanline / Glitch Field (cyberpunk)

- Deep purple-black with pink/cyan neon patches
- Scanline pattern overlay (4×4 pattern with 2px fill)
- RGB-split title text
- Datamosh smear bands across upper area
- CRT vignette radial darkening

### Variant D — Risograph / Print Grain Field

- 2-3 spot color blooms (fluorescent pink, teal)
- Halftone dot pattern overlay
- Registration misalignment between color plates
- Paper-feel base with grain

## Typography on field

- Font family: clean grotesk (SF Pro Display / Helvetica Neue / Inter)
- Title: font-weight 800-900, size 60-72pt, color pure white
- Year / secondary: font-weight 200-300, saturated accent color (cyan or yellow)
- Body text: white with fill-opacity 0.6-0.85 for hierarchy
- All text crisp and anti-aliased — NO drop shadow, NO texture
- Contrast against field must be enforced — field should stay darker where text sits

## Required content blocks

1. **Field hero** (atmospheric, 40-60% canvas)
2. **Title** in large grotesk, centered (or strongly anchored)
3. **Date / location / context line**
4. **Feature list** (speakers / artists / participants) 3-col grid
5. **URL / CTA footer**

## Optional content blocks

- Thin white bounding hairlines at top/bottom of hero zone
- Small wordmark duplicated top-left
- Saturated accent rule under title
- "+ N MORE" indicator on feature list
- Footer URL + copyright

## Compatible style profiles

- **Refik Anadol** — native fit (Mode 1 Neon Data)
- **Beeple** — darker variant with garbage-aesthetic
- **Ash Thorp** — cold atmospheric variant (less saturated, more monochrome)
- **James White / Signalnoise** — sunset gradient variant of the field
- **Josan Gonzalez** — dense neon-chaos field variant

## Compatible trend layers

- **Aurora Mesh Gradient** — native
- **Neo-Futurism / Spatial UI** — glassy elements over field
- **Glitch / Datamosh** — scanline / RGB-split variant
- **Acid Graphics / Liquid Chrome** — chrome title over sunset field
- **Risograph Print** — spot-color grain variant

## Example reference posters

- [`05-hitech-compose.svg`](../../../my-works/showcase-themed-2026/05-hitech-compose.svg) — Anadol × Aurora Mesh Gradient (Variant A + B combined)

## Anti-patterns for this template

- Small field with large margins (field should fill hero zone edge-to-edge)
- Recognizable imagery in the field (defeats the abstract purpose)
- Warm paper base (this template is dark-mode / field-mode — paper goes against the grain)
- Tiny title text (title needs to punch through the atmosphere)
- More than 2 accent colors in typography (keep info layer disciplined)

## Typography contrast rules

To keep text readable over a blurry saturated field:
1. Never place body text over the brightest bloom zone — place it over a darker area
2. If field is very saturated, add a subtle dark rectangle behind text at 20% opacity
3. Use only pure `#FFFFFF` for primary title (not off-white, not gray)
4. Secondary text at fill-opacity 0.6-0.75 keeps hierarchy without adding colors

## Sources

- Refik Anadol's "Unsupervised" MoMA installation (2022-2023)
- Apple Vision Pro keynote visuals (2024)
- WWDC conference poster archive
- Awwwards Site of the Day AI-era winners
- Serpentine Pavilion digital-art commissions

## Last sync

2026-04-19
