# Poster Catalog — Real-World References

*158 canonical posters across 13 markdown files, each with verified URL + visual analysis + designer-pairing + teaching notes. Built as Phase 8.1 to give the design-creator agent grounded, diverse, real-world anchors instead of synthesized reference posters.*

## Why this exists

The 6 reference posters in `my-works/showcase-themed-2026/` are useful starting points but they're all by one hand, so the agent was converging on a single aesthetic. This catalog broadens the reference set to 158 real posters from 13+ eras / techniques / curators.

When `concept-explorer` picks a concept angle, it now reads from THIS catalog in priority over `my-works/`. Three selection axes:

1. **By era** — what period does the brief call for?
2. **By technique** — type-only, photo-based, or illustration-led?
3. **By 2024-2026 source** — what's current?

## Structure

```
poster-catalog/
├── by-era/
│   ├── 1890s-chromolithograph.md     — 8 posters (Lautrec, Chéret, Mucha, Steinlen)
│   ├── 1920s-constructivism.md       — 8 (Rodchenko, Lissitzky, Stenbergs, Bauhaus)
│   ├── 1930s-art-deco.md             — 7 (Cassandre, Hohlwein, McKnight Kauffer)
│   ├── 1950s-swiss.md                — 8 (Müller-Brockmann, Hofmann, Bill, Ruder, Gerstner)
│   ├── 1960s-polish-school.md        — 8 (Tomaszewski, Lenica, Cieślewicz, Świerzy)
│   ├── 1960s-psychedelic.md          — 7 (Wes Wilson, Moscoso, Griffin, Mouse & Kelley)
│   ├── 1970s-japanese.md             — 8 (Kamekura, Fukuda, Yokoo, Tanaka, Nagai)
│   ├── 1990s-grunge-digital.md       — 7 (Carson, Brody, Sagmeister, Kalman, Kruger, Emigre)
│   ├── 2020-2023-ai-era-dawn.md      — 10 (Anadol MoMA, Beeple, pandemic posters, Squid Game)
│   └── 2024-2026-contemporary.md     — 21 (D&AD 2024 Black Pencils, TDC 2025, Pentagram, Studio Dumbar, Porto Rocha, Sagmeister)
│
├── by-technique/
│   ├── type-only-posters.md          — 10 (Vignelli, Scher, Saville, Jetset, Lars Müller)
│   ├── photo-based-posters.md        — 10 (Saville, Ishioka, Sagmeister, Benetton, Tillmans, Wall)
│   └── illustration-posters.md       — 10 (Kilian Eng ×4, Josan, Shinkawa, Yokoo, Hanuka)
│
└── by-2024-2026-source/
    ├── its-nice-that-2024-2026.md    — 10 featured works
    ├── awwwards-sotd-2024-2026.md    — 8 SOTD with poster-applicable heros
    ├── behance-trending-2025-2026.md — 10 trending graphic design
    └── arena-curated-2024-2026.md    — 8 under-the-radar contemporary
```

## Entry format (uniform across all files)

Every poster entry has:
- Designer name + work title + year
- Verified URL (museum / archive / press / studio site)
- Country, medium, format, approximate dimensions
- Palette (named colors + hex)
- Composition (2-3 sentences)
- Typography (typefaces + placement)
- Signature move (the ONE canonical thing)
- What it teaches (2-3 bullets for the AI agent)
- Pair with designer profiles from `style-profiles/`
- Pair with brief types (cinema / music / editorial / etc.)

## Integrity

- **Zero fabrication.** Every entry was verified via WebFetch / WebSearch against primary sources (MoMA, V&A, Cooper Hewitt, sagmeister.com, pentagram.com, mondotees.com, behance.net project pages, itsnicethat.com articles, are.na channels/blocks, bienalebrno.org, centrenationaldugraphisme.fr, tokyotypedirectorsclub.org, etc.).
- Where direct image fetches returned 403, the fetch agents worked around by using WebSearch to surface catalog IDs, then constructing museum URLs from those IDs (e.g. `moma.org/collection/works/[id]`).
- 3 entries in `2024-2026-contemporary.md` are marked `[verified by press coverage, image not directly fetched]` — the works exist, but the image URLs returned 403 so we cite the press article as proof-of-existence.
- Each file's `## Last sync` section documents what was fetched vs what returned errors.

## How the design-creator agent uses this

In `~/.claude/skills/design-creator/SKILL.md` Step 2 (concept-exploration), each concept-explorer subagent reads:

1. The matching style-profile (`style-profiles/<designer>.md`)
2. The matching trend from `docs/trends-2026.md`
3. **2-3 relevant poster entries from THIS catalog** based on era, technique, or current-source axis
4. The reference posters in `my-works/showcase-themed-2026/` (secondary reference now, not primary)

This gives each concept a real-world anchor point instead of converging on the agent's synthesized defaults.

## Keeping the catalog fresh

The `periodic-research` subagent (scheduled monthly on the 1st) adds new entries to `by-2024-2026-source/` as new work is featured. Over a year, the 2024-2026 subfolder becomes a chronicle of the period's visual design.

## Cross-reference

- Competition archives: [`sources/research/awards/`](../awards/) — describes competitions as a whole; catalog describes individual posters.
- Palette snapshot: [`sources/research/palettes/colorhunt-trending-2026.md`](../palettes/colorhunt-trending-2026.md)
- Trend synthesis: [`sources/research/trends-verified-2026.md`](../trends-verified-2026.md)

## Stats

- **17 files**
- **~4,013 lines of curated analysis**
- **158 verified poster entries**
- **13 eras / 3 techniques / 4 tastemaker sources**
- **Designers represented**: ~90+ individual designers + 25+ studios / collectives
- **Geographic coverage**: USA, UK, France, Germany, Switzerland, Poland, Japan, Russia, Netherlands, Brazil, Mexico, Taiwan, Korea, Ukraine, Belgium, Denmark, Finland, Italy, Spain, Ireland, Vietnam, Israel

## Last sync

2026-04-19 — initial build via 5 parallel subagents over ~90 minutes.
