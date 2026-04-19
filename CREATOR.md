# design-creator — the autonomous poster agent

*Give it a brief. It picks the designer voice, applies the trend layer, renders the SVG, self-verifies the layout, and opens the preview in Safari. You review the output — not the coordinates.*

---

## Quick start

Open a Claude Code session in any directory (doesn't have to be this repo — the skill uses absolute paths) and type:

```
Create a cinema poster for a fictional arthouse sci-fi film called "ARRAKIS: THE SILENT SUN"
```

Or in Russian:

```
Сделай постер для AI-конференции FEEDBACK в Берлине
```

Or specify a designer:

```
Design a jazz album poster in the style of Peter Saville
```

The `design-creator` skill auto-invokes on these phrases. It orchestrates the full pipeline and returns a finished SVG in `my-works/YYYY-MM-DD-<slug>/`.

---

## What happens under the hood

```
You:  "Create a cinema poster for ARRAKIS"
   │
   ▼
┌──────────────────────────────────────────────────────┐
│  design-creator skill (orchestrator)                 │
└──┬───────────────────────────────────────────────────┘
   │  1. Prompt compilation — extracts theme, picks designer + trend
   │
   ├─→ 2. Parallel dispatch (3 concept-explorer subagents)
   │     • type-forward angle
   │     • image-forward angle
   │     • trend-aggressive angle
   │
   ├─→ 3. design-critic subagent
   │     Two-pass evaluation (constructive + adversarial)
   │     Scores each on 5 dimensions
   │     Picks winner + names pre-render fixes
   │
   │  4. Render SVG (orchestrator writes file directly)
   │
   ├─→ 5. layout-verifier subagent
   │     Runs tools/check-layout.py
   │     If FAIL → loop back, fix, re-verify (max 3 tries)
   │
   │  6. Open in Safari
   │
   │  7. Update memory + logs + commit to git
   │
   ▼
Finished SVG in my-works/YYYY-MM-DD-arrakis/arrakis.svg
```

## The skill's knowledge base

It reads on demand:

| Knowledge | Where | What it provides |
|---|---|---|
| 14 contemporary designer profiles | `style-profiles/` | Palettes, composition rules, signature moves per designer |
| 8 historical eras (1870–present) | `sources/history/eras/` | Era-specific visual vocabularies |
| 5 canonical design books | `sources/principles/books/` | Bringhurst typography, Müller-Brockmann grids, Hara emptiness, Tschichold modernism, Rand design thinking |
| Art fundamentals | `sources/principles/drawing/`, `sources/principles/photography/` | Perspective, composition, light, exposure, lighting setups |
| Style locks | `sources/principles/style-locks.md` | Hard-stop constraints per designer (prevents AI-mush) |
| Layout templates | `sources/principles/layout-templates/` | 4 reusable composition schemas extracted from reference posters |
| 2026 trends | `docs/trends-2026.md`, `docs/trends-by-decade.md` | Current and historical trend vocabulary |
| Competition winners | `sources/research/awards/` | Real Brno / Warsaw / Chaumont / Lahti / Tokyo TDC / Mexico / AIGA / D&AD winners |
| Live trending palettes | `sources/research/palettes/colorhunt-trending-2026.md` + live color-research subagent | 60+ curated Colorhunt palettes + on-demand live fetch |
| 6 reference posters | `my-works/showcase-themed-2026/` | Structural templates the agent uses as gold standard |
| Memory | `memory/winning-concepts.json`, `rejected-patterns.json`, `layout-patterns.json` | Patterns that worked, patterns that didn't — the agent biases toward proven choices |

## Quality guarantees

The skill enforces these automatically — you stop being the QA:

- **No text overflow** — `check-layout.py` estimates each text element's bounding box via font metrics and rejects any text extending past the frame
- **No element overlap** — same checker detects overlapping text bboxes and loops back for fixes
- **No too-small fonts** — anything below 6pt flagged
- **Bringhurst compliance** — line-length ≤ 85 chars, real glyphs (em-dash, curly quotes), no fake small-caps
- **Style-lock respect** — if the chosen designer forbids an element (Hara + neon, for example), the trend gets substituted before render
- **Up to 3 auto-fix iterations** — if the first render fails verification, the agent fixes and re-checks; if still failing after 3 tries, it escalates to you

## Monthly research refresh

A scheduled task runs on the 1st of each month at 9:00 AM local. It:

1. Dispatches `color-research` to refresh Colorhunt palettes (all tags)
2. Dispatches `research-agent` to scan for new competition announcements and trending work
3. Writes dated snapshot files: `sources/research/palettes/colorhunt-YYYY-MM.md`, `sources/research/observations/behance-YYYY-MM.md`, etc.
4. Updates the synthesis file `sources/research/trends-verified-2026.md`
5. Commits + pushes to GitHub

Over a year, you accumulate a chronicle of 2026's visual design trends, evidence-based.

## Usage tips

**Specific is better than vague.**
"A poster" gets you generic work. "A poster for a 3-day contemplative soulslike game set in a fallen Japanese kingdom, called ASHFALL: Kingdom of Ruin" gets you something specific.

**Name a designer if you care about voice.**
"In the style of Yoji Shinkawa" is much stronger than letting the agent pick from 14 profiles blindly.

**Or don't — let the agent choose.**
If you only describe the subject, the agent picks a designer based on theme (cinema → Kilian Eng, hi-tech → Refik Anadol, jazz → Sagmeister, etc.). You'll see the choice explained in the summary.

**You can override during rendering.**
After the critic picks a winner, if you don't like the direction, say "pick one of the other concepts instead" or "re-explore with different angles."

**Reference a specific competition for grounding.**
"Like the posters that won Brno 2018" will bias the agent toward verified competition-caliber work from that edition.

**Print vs screen.**
All output is SVG. For print, open in Illustrator and export PDF with proper CMYK conversion. For screen, use `scripts/svg-to-png.sh <path>` for PNG.

## Troubleshooting

**"The agent generated the same look twice."**
- The explorer subagents converged. Re-run with different phrasing. Or manually specify different designer + trend combination.
- Check `memory/winning-concepts.json` for recent outputs — the agent biases toward patterns that worked, so it may reuse recent structure.

**"Text is tiny / unreadable on my screen."**
- That's `too_small` warning — check the layout-verifier's final report. Should have been fixed automatically.
- If it shipped anyway, run `python3 tools/check-layout.py <svg>` manually to see the actual issues.

**"I want to override the style-lock for a specific poster."**
- Add `"override style-locks for this run"` to your brief. The agent will note the override in the concept statement and render anyway.

**"Monthly research didn't run."**
- Check the scheduled task: `claude scheduled-tasks list`
- Run manually: invoke the `periodic-research` subagent directly.

## File layout

```
design-library/
├── CREATOR.md                    ← you are here
├── PLAN.md                       ← the blueprint this was built from
├── README.md                     ← repo overview
├── QUICKSTART.md                 ← manual workflow (without agent)
│
├── tools/
│   ├── check-layout.py          ← SVG layout verifier (Python)
│   └── generate.py              ← Image Studio CLI (older pipeline)
│
├── scripts/
│   ├── svg-to-png.sh            ← PNG export helper
│   └── monthly-research.sh      ← manual trigger for research refresh
│
├── memory/                       ← persistent learning state
│   ├── winning-concepts.json
│   ├── rejected-patterns.json
│   └── layout-patterns.json
│
├── logs/
│   └── runs.jsonl               ← every render logged (gitignored)
│
├── style-profiles/              ← 14 contemporary designer profiles
├── sources/
│   ├── designers/
│   ├── history/                 ← eras / movements / masters
│   ├── principles/              ← books / drawing / photography / craft / layout-templates
│   └── research/                ← awards / palettes / observations
├── docs/                        ← trends-2026.md, trends-by-decade.md
└── my-works/                    ← output folder (posters land here)
```

## External skill / agent files (in ~/.claude/)

```
~/.claude/
├── skills/design-creator/SKILL.md    ← main orchestrator
└── agents/
    ├── concept-explorer.md           ← generates ONE concept angle
    ├── design-critic.md              ← ranks 3 concepts (two-pass)
    ├── layout-verifier.md            ← runs check-layout.py, translates issues
    ├── color-research.md             ← live-fetches Colorhunt
    ├── research-agent.md             ← live-fetches competitions / curated sources
    └── periodic-research.md          ← monthly orchestrator (scheduled)
```

## What this replaces

Before: you had a library of reference files and had to manually compose SVG brief by brief, catching overflow errors yourself.

Now: you describe the subject in one sentence. Everything else is automated.

## What this doesn't do yet (v2 candidates)

- **Mutation loop** — iterate on the winner by tweaking palette / scale / composition. Currently commented-out; will enable with `--mutate` flag if v1 baseline quality calls for it.
- **Quant scoring full** — current critic uses qualitative-to-numeric scoring. A fully deterministic scoring formula with contrast / whitespace-ratio / alignment-deviation metrics is planned for v2.
- **Multi-format output** (IG story 9:16, print-ready CMYK with bleed/trap) — only SVG + PNG in v1.
- **Taste profile** (user preferences learned over time) — single-user only for now.

## Credits

Built April 2026 as a self-learning design library. All canonical references (Bringhurst, Müller-Brockmann, Hara, Tschichold, Rand) summarized with care. All competition data (Brno, Warsaw, Chaumont, etc.) fetched from primary sources with explicit sync notes. No fabricated winners, URLs, or hex codes — where live data was unavailable, gaps are documented in each file's "Last sync" section.

---

**Last updated:** 2026-04-19
