# Design-Creator Agent — Master Plan v1

*Consolidated blueprint from all brainstorm turns. Everything we've agreed on, everything you've added, everything left to build.*

---

## 1. What we're building — one paragraph

An **autonomous design agent** that, given a brief ("make a cinema poster for X in the style of Y"), independently:

1. Generates **3 concept variants** (parallel sub-agents, three different angles)
2. **Ranks them** via a critic sub-agent against typography + composition + conceptual criteria
3. **Builds the winning SVG** grounded in designer style profiles + current trends + real competition data + trending palettes
4. **Self-verifies layout** automatically (no text overflow, no overlaps, no floating elements, typography per Bringhurst)
5. **Loops fixes** if verification fails (up to 3 attempts)
6. **Presents final** in Safari

You stop being the QA. The agent ships work that's already been checked.

---

## 2. What's already done (on GitHub)

### Posters — 6 themed reference works
[`my-works/showcase-themed-2026/`](my-works/showcase-themed-2026/) — cinema / art / music / games / hi-tech / electronic music, across 3 palette registers.

### Phase 1 — Core knowledge base (18 files, ~3,500 lines)
- **Books** (4): Bringhurst, Müller-Brockmann, Hara, Tschichold, Rand (5 actually, counting Bringhurst as kickoff)
- **History eras** (8): 1870→present poster history
- **Drawing** (3): perspective, composition-fine-art, light-and-shadow
- **Photography** (2): exposure-triangle, lighting-setups
- **Synthesis** (1): trends-by-decade

### Existing library (unchanged)
- 14 contemporary designer style profiles
- 3 universal principles (color-theory, composition-grids, typography-hierarchy)
- Image Studio CLI (tools/generate.py)
- Trends-2026.md
- QUICKSTART.md

---

## 3. Full scope (your brainstorms + my additions, merged)

### Knowledge base additions you requested

| What | Where | Status |
|---|---|---|
| Design book principles (Bringhurst, MB, Hara, Tschichold, Rand) | `sources/principles/books/` | ✅ Phase 1 |
| History of posters from beginning of time | `sources/history/eras/` | ✅ Phase 1 (8 eras) |
| Top artists by era | `sources/history/masters/` | ⏳ Phase 2 (15 files) |
| Art fundamentals (perspective, composition, light, color, anatomy) | `sources/principles/drawing/` | ✅ partial (3 of 8 done) |
| Photography fundamentals | `sources/principles/photography/` | ✅ partial (2 of 5 done) |
| Print & craft (screen, litho, riso, paper) | `sources/principles/craft/` | ⏳ Phase 3 (4 files) |
| Exposition / format conventions | `sources/principles/exposition/` | ⏳ Phase 3 (3 files) |
| Movement deep-dives (Bauhaus, Swiss, Psychedelic, etc.) | `sources/history/movements/` | ⏳ Phase 4 (10 files) |
| Trends by decade | `docs/trends-by-decade.md` | ✅ Phase 1 |
| **Competition winners research** (Brno, Warsaw, Tokyo TDC, Chaumont, Lahti, Mexico, AIGA 50-50, D&AD Pencils) | `sources/research/awards/` | ⏳ **Phase 8** |
| **Colorhunt.co trending palettes** | `sources/research/palettes/` | ⏳ **Phase 8** |
| **Verified trends** (synthesis of competition data) | `sources/research/trends-verified-2026.md` | ⏳ Phase 8 |

### Agent behaviour you requested

| Requirement | How | Status |
|---|---|---|
| Creates, not checks | Main skill orchestrates | ⏳ Phase 5 |
| Plans 3 variants before building | 3 parallel concept-explorer sub-agents | ⏳ Phase 6 |
| Self-selects top (or uses another agent) | design-critic sub-agent with criteria | ⏳ Phase 6 |
| **Checks composition & typography without me pointing out overflow** | `tools/check-layout.py` + layout-verifier sub-agent | ⏳ **Phase 7** |
| Grounded in real competition winners | sources/research/awards/ corpus | ⏳ Phase 8 |
| Knows current Colorhunt trends | Static snapshot + color-research sub-agent for live fetch | ⏳ Phase 8 |
| Auto-fixes issues and re-verifies | Loop up to 3 iterations | ⏳ built into skill |

---

## 4. Architecture (the shape of the thing)

```
User: "Create a cinema poster for X in the style of Y"
   │
   ▼
┌──────────────────────────────────────────────────────┐
│  design-creator SKILL (the orchestrator)             │
│  ~/.claude/skills/design-creator/SKILL.md            │
└──┬───────────────────────────────────────────────────┘
   │
   │  1. Parse brief → identify theme/era/designer/trend
   │
   ├─→ PARALLEL: 3 concept-explorer subagents
   │     each generates ONE concept from different angle:
   │     • type-forward angle
   │     • image-forward angle  
   │     • trend-aggressive angle
   │
   ├─→ design-critic subagent
   │     scores all 3 on: concept strength, Bringhurst compliance,
   │     composition, palette coherence, distinctness
   │
   │  2. Pick winner, state reasoning
   │
   │  3. BUILD SVG (main skill writes file)
   │
   ├─→ layout-verifier subagent
   │     runs tools/check-layout.py
   │     returns JSON: {passed: bool, issues: [...]}
   │
   │  4. If issues: fix → re-verify → loop (max 3 attempts)
   │
   │  5. Open in Safari, show to user
   │
   └─→ [optional] color-research subagent if brief needs fresh palette
         WebFetches colorhunt.co by tag/mood, returns 5 candidate palettes


KNOWLEDGE BASE it reads on demand:
   ├── style-profiles/*        (14 contemporary designers)
   ├── sources/history/
   │   ├── eras/*             (8 eras)
   │   ├── movements/*        (10 movements — Phase 4)
   │   └── masters/*          (15 historical — Phase 2)
   ├── sources/principles/
   │   ├── books/*            (5 canonical books)
   │   ├── drawing/*          (fine-art fundamentals)
   │   ├── photography/*      (exposure, lighting)
   │   ├── craft/*            (print, paper — Phase 3)
   │   └── exposition/*       (format conventions — Phase 3)
   ├── sources/research/
   │   ├── awards/*           (competition winners — Phase 8)
   │   ├── palettes/*         (Colorhunt snapshots — Phase 8)
   │   └── trends-verified-2026.md
   ├── docs/trends-2026.md
   ├── docs/trends-by-decade.md
   └── my-works/showcase-themed-2026/* (6 reference posters)


TOOLS:
   └── tools/check-layout.py  (Python SVG overflow/overlap checker)
```

---

## 5. Execution phases — full list

Every phase adds working value. Not all required for v1 agent.

| Phase | Purpose | Files | Status |
|---|---|---|---|
| 1 — CORE | Books + history + drawing + photo | 18 | ✅ DONE |
| 2 — MASTERS | 15 historical designer profiles (Mucha, Cassandre, Tschichold, Rand, Bass, Hofmann, MB, Glaser, Yokoo, Brody, Lustig, Fukuda, Chwast, Lissitzky, Toulouse-Lautrec) | 15 | ⏳ |
| 3 — DEEP ART | Color/anatomy/line/depth/value + craft + exposition | 12 | ⏳ |
| 4 — MOVEMENTS | Bauhaus, Constructivism, Swiss, Psychedelic, Punk, Memphis, Mondo, Polish, Art Deco, Art Nouveau | 10 | ⏳ |
| **5 — AGENT** | design-creator SKILL + CREATOR docs | 2 | ⏳ |
| **6 — MULTI-AGENT** | concept-explorer + design-critic sub-agents | 2 | ⏳ |
| **7 — LAYOUT QA** | check-layout.py + layout-verifier sub-agent | 2 | ⏳ |
| **8 — RESEARCH** | 8-12 competition archives + Colorhunt snapshot + research sub-agents + trends-verified | 14-16 | ⏳ |

**Bold phases = minimum for working agent**. Non-bold = extra depth (can add any time later).

### For a fully working agent: Phase 5 + 6 + 7 + 8 = ~20 files

Phases 2, 3, 4 add breadth but agent already works without them (Phase 1 + core modern profiles cover most cases).

---

## 6. File-by-file manifest for remaining work

### Phase 5 — Agent (2 files)
- `~/.claude/skills/design-creator/SKILL.md` — main orchestrator
- `CREATOR.md` — user docs in repo root

### Phase 6 — Multi-agent (2 files)
- `~/.claude/agents/concept-explorer.md` — generates one concept angle
- `~/.claude/agents/design-critic.md` — ranks concepts by criteria

### Phase 7 — Layout QA (2 files)
- `tools/check-layout.py` — Python SVG parser + font-metrics checker
- `~/.claude/agents/layout-verifier.md` — wraps the script

### Phase 8 — Research (~14 files)
Competition archives (each file = top 10-20 winners + visual analysis):
- `sources/research/awards/brno-biennial-2024.md`
- `sources/research/awards/brno-biennial-2022.md`
- `sources/research/awards/warsaw-biennale-2024.md`
- `sources/research/awards/warsaw-biennale-2022.md`
- `sources/research/awards/chaumont-2024.md`
- `sources/research/awards/tokyo-tdc-2025.md`
- `sources/research/awards/tokyo-tdc-2024.md`
- `sources/research/awards/lahti-2023.md`
- `sources/research/awards/mexico-biennial-2023.md`
- `sources/research/awards/aiga-50-50-2024.md`
- `sources/research/awards/dandad-2024-pencils.md`

Palettes:
- `sources/research/palettes/colorhunt-trending-2026.md` — snapshot of 30-50 Colorhunt palettes tagged by mood/era

Synthesis:
- `sources/research/trends-verified-2026.md` — which trends appear across multiple award catalogs

Research subagents:
- `~/.claude/agents/research-agent.md` — live-fetch from competition sites when needed
- `~/.claude/agents/color-research.md` — live-fetch Colorhunt by tag

---

## 7. How the agent will work — step-by-step

Concrete example flow:

> **Brief:** "Create a music poster for a techno festival in Berlin called 'FEEDBACK'"

1. **design-creator** parses brief:
   - Theme: music / electronic
   - Format: poster
   - Name: FEEDBACK
   - Location: Berlin (hint: Kompakt Records tradition? Berghain?)

2. **Pre-research dispatch** (parallel):
   - `color-research`: "show me electronic/acid/rave trending palettes on Colorhunt"
   - `research-agent`: "what won Brno 2024 in music/event posters?"

3. **Dispatch 3 concept-explorers** (parallel):
   - A: type-forward (Sagmeister × Variable Bold Typography angle)
   - B: image-forward (Saville × Aurora Gradient angle)
   - C: trend-aggressive (anti-design Brutalism × neo-brutal typography)

4. Each returns: concept description + palette + composition sketch + SVG draft

5. **design-critic** ranks all 3 on:
   - Concept strength (does it earn 'FEEDBACK' as a name?)
   - Bringhurst compliance (line-length, leading, real glyphs)
   - Composition (grid, hierarchy, Müller-Brockmann)
   - Palette coherence (not muddy, one saturated accent max)
   - Distinctness (does it look like anything else?)
   - Historical awareness (doesn't accidentally repeat a famous poster)

6. Winner selected, reasoning logged. design-creator builds full SVG.

7. **layout-verifier** runs:
   - `python tools/check-layout.py [path]`
   - Returns: `{"passed": false, "issues": [{"type": "overflow", ...}]}`

8. If issues: main agent reads report, fixes specific coordinates, re-runs layout-verifier. Loop max 3 times.

9. Only when `passed: true` → opens in Safari, explains choices in summary.

---

## 8. Your improvements list (all captured)

These are the things you explicitly added to the plan over our conversation:

- [x] Plan 3 variants, pick top via another agent (Phase 6)
- [x] Self-check so you don't have to catch overflow/dancing text (Phase 7)
- [x] Art fundamentals not just graphic design — perspective, light, anatomy, etc. (Phase 1 partial + Phase 3)
- [x] History of posters from beginning of time (Phase 1 eras + Phase 2 masters + Phase 4 movements)
- [x] Top artists by era (Phase 2)
- [x] Trends by decade (Phase 1 trends-by-decade)
- [x] Research of top competition winners (Phase 8)
- [x] Colorhunt.co for trending palettes (Phase 8)
- [x] Book-knowledge base (Phase 1 books)
- [x] Verifies fonts don't overflow or overlap (Phase 7)
- [x] Keep posters in one folder like samples (✅ done)
- [x] Do it fully ("суппер"), not minimum (thorough mode as default)

---

## 9. Open questions (none remaining critical)

- ~~One repo or two?~~ → **one** (confirmed)
- ~~Minimum or full?~~ → **full** ("суппер")
- ~~Thorough multi-agent?~~ → **yes, default**
- WebFetch stability for competition data — assume yes; if some sites block, agent uses alternate sources
- How many competitions — aim for **8–10** initial corpus (not all on day one if some data unavailable)

---

## 10. Proposed execution order

**Session 1 (now): Phase 5 + 6 + 7 + 8 = ~20 files → agent works**
1. Write `tools/check-layout.py` (Python layout checker)
2. Write 4 sub-agent definitions (concept-explorer, design-critic, layout-verifier, color-research)
3. Write `design-creator/SKILL.md` (the orchestrator)
4. Write `CREATOR.md` (user docs)
5. Fetch Colorhunt → write `colorhunt-trending-2026.md`
6. Fetch 8-10 competition archives
7. Write `trends-verified-2026.md` synthesis
8. Update main README with agent section
9. Commit + push
10. Smoke test: "create a music poster for a techno festival" → verify end-to-end

**Session 2 (later, optional): Phase 2 + 3 + 4 = +37 files → encyclopedic base**
- 15 historical master profiles
- 12 deep-art principles (color, anatomy, line, value, depth, craft, exposition)
- 10 movement deep-dives

---

## 11. Summary diff of what changes on GitHub in Session 1

New files (~20):
- `PLAN.md` (this file)
- `CREATOR.md`
- `tools/check-layout.py`
- `sources/research/palettes/colorhunt-trending-2026.md`
- `sources/research/awards/` × 8-10
- `sources/research/trends-verified-2026.md`

New outside repo (user `.claude` directory):
- `~/.claude/skills/design-creator/SKILL.md`
- `~/.claude/agents/concept-explorer.md`
- `~/.claude/agents/design-critic.md`
- `~/.claude/agents/layout-verifier.md`
- `~/.claude/agents/color-research.md`
- `~/.claude/agents/research-agent.md`

Updated:
- `README.md` — agent section
- `QUICKSTART.md` — reference to agent

---

## 12. FINAL v1 scope (locked 2026-04-19)

After triage, these phases are IN v1:

| Phase | Purpose | Files |
|---|---|---|
| ✅ 1 | Core knowledge (books, eras, drawing, photo, trends-by-decade) | 18 (done) |
| 5 | design-creator SKILL + CREATOR.md | 2 |
| 6 | concept-explorer + design-critic (two-pass constructive+adversarial) | 2 |
| 7 | tools/check-layout.py + layout-verifier subagent | 2 |
| 8 | 8-10 competition archives + Colorhunt snapshot + trends-verified + 2 research subagents | 14 |
| 9 | periodic-research subagent + monthly script + scheduled task | 2 |
| 10 | design memory (winning / rejected / layout patterns JSON) | 3 |
| 11 | prompt-compiler subagent | 1 |
| 13 | style-locks.md (constraint tables per style) | 1 |
| 15 | layout-templates/ extracted from 6 reference posters | 3-4 |
| 17 | telemetry (runs.jsonl auto-append, gitignored) | 0 initial |
| 18 | svg-to-png.sh helper | 1 |

**Total v1 = ~30 files + scheduled task registration.**

### Explicitly dropped from v1 (not v2, not at all for now)

- ~~12 Quant scoring full~~ (metrics too fuzzy; will get simple rule-based scoring inside critic)
- ~~14 Adversarial critic as separate agent~~ (merged into critic as two-pass)
- ~~16 Mutation loop~~ (waits until we see v1 quality baseline)
- ~~19 Speed optimization~~ (premature — optimize when we have latency data)
- ~~20 Taste profile~~ (single user, no need)

### Phases 2, 3, 4 — encyclopedic breadth (optional Session 2)

- Phase 2 — 15 historical masters (Mucha, Cassandre, Tschichold, Rand, etc.)
- Phase 3 — 12 deep art principles (color, anatomy, line, value, craft, exposition)
- Phase 4 — 10 movement deep-dives (Bauhaus, Constructivism, Swiss, etc.)

Not required for working agent. Adds breadth only.

## 13. Execution kickoff

Proceeding with v1 now. Commits at phase milestones.

---

## 14. Post-execution status (updated 2026-04-19)

### Shipped

**v1.5.0 — Agent stack** (commit 3c8df5c)
- design-creator SKILL + 6 subagents (concept-explorer, design-critic, layout-verifier, color-research, research-agent, periodic-research)
- Python layout-checker (615 lines, transform-aware + smart descender)
- CREATOR.md docs + launchd monthly refresh instructions
- 18-file core knowledge base (5 books, 8 eras, 3 drawing, 2 photo, trends synthesis)
- 4 layout templates + style-locks + memory system
- 8 competition archives (Brno/Warsaw/Chaumont/Lahti/TDC/Mexico/AIGA/D&AD)
- Colorhunt snapshot (64 verified palettes)

**v1.5.1** — layout-checker transform fix + smart descender + Kompakt footer patch

**v1.6.0 — Real-poster catalog** (commit 41f850a)
- 17 files under `sources/research/poster-catalog/`
- 158 verified posters with URLs + visual analysis
- 10 by-era files (1890s → 2024-2026, heavy 2024-2026 emphasis)
- 3 by-technique files (type-only / photo-based / illustration)
- 4 by-2024-2026-source files (It's Nice That / Awwwards / Behance / Are.na)

**v1.7.0 — Structural variance** (commit 884552f)
- `sources/principles/structural-variance.md` — 12 archetypes with mandatory rotation rule
- concept-explorer.md patched: Step 8 MANDATORY read of structural-variance + last 3 winning-concepts + pick archetype NOT in last 3
- memory/rejected-patterns.json expanded with 8 forbidden Claude-default signatures (outer frame, top-meta split, hero-divider-type-footer sequence, brutalist research annotations, coordinate rings, catalog footer splits, stacked italics, excessive letter-spacing)

### Posters generated by the agent

Seven posters across six structural archetypes, seven palette registers:

| # | Poster | Archetype | Palette family |
|---|---|---|---|
| 1 | Digital Loneliness | 1 Classical Centered Hero | black + cold blue + bone white |
| 2 | Burn the Night | 1 variant (motion) | deep purple + neon orange + black |
| 3 | LAST SIGNAL v2 | **2 Full-Bleed Atmospheric** | deep space navy + subtle white |
| 4 | You Are the Product | **12 Anti-Design Brutalism** | white + black + blood red |
| 5 | 404: Meaning Not Found | **6 Figure + Vast Negative Space** | pure white + near-black |
| 6 | Consent | **4 Object-Bleed Hybrid** | warm gray + skin tones + red |
| 7 | THE FINAL LOOP | 1 clean (no crutches) | desaturated grays + muted amber |

Rotation works: 6 distinct archetypes across 7 posters. No palette family repeated. Still unused: archetypes 3, 5, 7, 8, 9, 10, 11 — room for continued structural growth.

### Skipped from original plan (Session 2 candidates)

- Phase 2 — 15 historical designer master profiles (Mucha, Cassandre, Tschichold, Rand, Bass, Hofmann, MB, Glaser, Yokoo, Brody, Lustig, Fukuda, Chwast, Lissitzky, Toulouse-Lautrec). Partially covered via poster-catalog entries; dedicated master profiles not yet written.
- Phase 3 — 12 deep art principles (color/anatomy/line/value/depth/craft/exposition). Partially covered (drawing + photography exist); craft and exposition still todo.
- Phase 4 — 10 movement deep-dives (Bauhaus, Constructivism, Swiss, Psychedelic, Punk, Memphis, Mondo, Polish, Art Deco, Art Nouveau). Partially covered in poster-catalog by-era files; dedicated movement files still todo.

### Current size

- ~140 files in the library
- ~18,000 lines of curated analysis
- 158 real-world poster references + 7 agent-generated works
- Full agent stack with automated QA and monthly research refresh

**Last sync:** 2026-04-19

