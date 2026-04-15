# 2026-04 — Cyber Art Expo Poster

> Example project demonstrating the library workflow. A vertical 8.5×11 poster built by asking Claude to reference specific style profiles from this library.

## Brief
Create an 8.5×11 vertical poster for a fictional cyberpunk art exhibition. Requirements: readable colored type, pattern element, limited color palette, demonstrate Illustrator typography functions (point type, area type, type on path, type mask).

## Concept
"NEO//GENESIS" — fictional Cyber Art Exhibition 2077. Minimalist cinematic UI aesthetic.

## Style references applied
- **Ash Thorp** (see `style-profiles/ash-thorp.md`) — HUD corners, thin linework, horizon-anchored composition, quiet monochrome + one warm accent
- Composition principles from `sources/principles/composition-grids.md`
- Color discipline from `sources/principles/color-theory.md`

## Palette (strictly 3 colors)
- `#06090D` — deep near-black base
- `#E8E8E8` — off-white linework
- `#FF6A00` — amber accent (5% of area)

## Typography
- **Headlines:** condensed light sans (Helvetica Neue Condensed with Impact/Arial Narrow fallback)
- **Details:** Courier New (mono readouts)

## Files
- `NEO-GENESIS-poster-v2-thorp.svg` — Illustrator-ready SVG with 13 named layers

## Envato assets used (not redistributed)
- **222 Cyber Y2K Elements** by Studio_Dusk (via Envato Elements) — shapes embedded via inline path data for portability. See `sources/collections/envato-saved.md` for the asset catalog format.

## Illustrator techniques demonstrated
| Requirement | Layer / location in SVG |
|---|---|
| Point type | `Layer_MainTitle` (NEO // GENESIS) |
| Area type | `Layer_EventDetails` (two-column block) |
| Type on path | `Layer_TypeOnPath` (curved "A POST-DIGITAL ARTIFACT OBSERVATION") |
| Type mask | `Layer_TypeMask` (number 047 filled with techGrid pattern) |
| Simple pattern | `Layer_DotPattern` + `Layer_TechGrid` |
| Limited palette | 3 colors strictly |
| Layered structure | 13 named `<g id="...">` groups → Illustrator layers |

## Lessons / notes
- SVG with explicit `<g id="...">` layer structure opens natively in Illustrator and preserves named layers in the Layers panel.
- Strict 3-color palette + thin 0.4-1px strokes forces discipline characteristic of Thorp's aesthetic — significantly different tone from default "cyberpunk = neon everything" output.
- Type-on-path is flattened on SVG import into Illustrator (known behavior). Visual stays correct but text becomes outlined paths. Recreate with Type Tool on path if editable curved text is needed.
- Avoid exotic Unicode glyphs (box-drawing chars, rare symbols) when targeting common fonts like Courier New — Illustrator will warn about missing alternate glyphs.

## Workflow
1. Reading `style-profiles/ash-thorp.md` gave Claude tactical rules (palette, composition, negative space ratios, explicit "don't use" list)
2. SVG generated with those rules applied, using inline path data from vector asset library
3. Output opens in Adobe Illustrator → can be saved as `.ai` for final delivery

## Date
2026-04-15
