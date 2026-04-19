# Layout Templates

*Reusable composition schemas extracted from the 6 reference posters in `my-works/showcase-themed-2026/`. Each template defines a grid plan and typographic zones that the `concept-explorer` subagent can pick as a starting point, then customize.*

## How this folder works

Templates are not visual styles — they're **composition schemas**. A template is a skeleton: where the hero lives, where title goes, where credits go. Visual style (colors, typography choices) comes from the style-profile. Trend layer (bento, aurora, acid graphics) adds finishing language.

```
TEMPLATE  ←  picks WHERE things sit
STYLE-PROFILE  ←  picks HOW each element looks
TREND  ←  picks FINISHING language (gradients, textures, effects)
```

## The four templates

| # | Name | Best for | Example poster |
|---|---|---|---|
| 01 | **Hero-Image-Center** | Cinema, games, book covers, theater — single strong central image | Arrakis, Ashfall, After-the-Machine |
| 02 | **Type-as-Image** | Editorial, music events, anniversaries, concept posters — where typography IS the visual | Kompakt 25, type-forward Blue Nothing |
| 03 | **Object-Bleed** | Album covers, product features, single iconic object — object dominates and bleeds off edge | Blue Nothing vinyl variant |
| 04 | **Field-Over-Hero** | Tech conferences, AI events, abstract subjects — atmospheric field with sharp typography overlay | Compose 2026 |

## How the agent chooses

`concept-explorer` picks template based on:
- Subject type (cinema/art/music/games/tech/commercial)
- Designer chosen (some designers favor certain templates: Saville = 02, Anadol = 04)
- Trend layer (some trends pair natively: Aurora = 04, Variable Bold = 02)

Full template-selection logic lives in `~/.claude/skills/design-creator/SKILL.md` §Select template.

## How to extend

When you find a new composition that works, codify it as `05-<name>.md` following the template file structure:
1. When to use
2. Grid plan (viewbox, margins, safe zone)
3. Vertical zones (y-anchors for each content block)
4. Required content blocks
5. Optional content blocks
6. Compatible style profiles
7. Compatible trends
8. Example reference posters

## Sources

These templates were extracted by reverse-engineering the 6 reference posters made in April 2026. They generalize the specific layouts those posters used into reusable skeletons.

## Last sync

2026-04-19
