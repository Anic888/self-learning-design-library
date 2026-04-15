# Showcase — April 2026: Legibility test across 8 styles + synthesis test

> The core claim of this library is that LLMs guided by distilled style profiles produce **legibly distinct** output — a viewer should look at two pieces and say "this is Thorp, this is Carson" without hesitation. This folder is the proof.
>
> Same underlying capability (Claude generating SVG). Same general brief ("make a design"). Only the **referenced style profile** changes. If the profiles work, the outputs must be visually unmistakable from each other.

## The eight pieces

| # | Work | Style profile applied |
|---|---|---|
| 00 | `../2026-04-cyber-art-expo/NEO-GENESIS-poster-v2-thorp.svg` | [ash-thorp.md](../../style-profiles/ash-thorp.md) |
| 01 | `01-signalnoise-synthwave.svg` | [james-white-signalnoise.md](../../style-profiles/james-white-signalnoise.md) |
| 02 | `02-shinkawa-ink-mecha.svg` | [yoji-shinkawa.md](../../style-profiles/yoji-shinkawa.md) |
| 03 | `03-carson-chaos-spread.svg` | [david-carson.md](../../style-profiles/david-carson.md) |
| 04 | `04-beeple-3d-satire.svg` | [beeple.md](../../style-profiles/beeple.md) |
| 05 | `05-josan-dense-cyberpunk.svg` | [josan-gonzalez.md](../../style-profiles/josan-gonzalez.md) |
| 06 | `06-sagmeister-concept-first.svg` | [stefan-sagmeister.md](../../style-profiles/stefan-sagmeister.md) |
| 07 | `07-mead-industrial-realism.svg` | [syd-mead.md](../../style-profiles/syd-mead.md) |
| 08 | `08-combination-test.svg` | **Synthesis:** Thorp composition × Carson typography × Shinkawa palette |

## Cross-style comparison (9 dimensions)

| Dimension | 00 Thorp | 01 Signalnoise | 02 Shinkawa | 03 Carson | 04 Beeple | 05 Josan | 06 Sagmeister | 07 Mead |
|---|---|---|---|---|---|---|---|---|
| **Base** | `#06090D` near-black | `#1E0B3A` deep violet | `#F5F0E0` bone white | `#F5F0E0` newsprint | `#3A1F0C` industrial brown | `#0A0015` deep purple | `#F7F1E3` warm paper | `#0F2744→#E89C4A` navy→amber |
| **Accent(s)** | amber `#FF6A00` (5%) | magenta + cyan + orange + yellow | oxblood red `#A33020` (one seal) | oxblood red accent | neon pink + cyan + yellow | pink + cyan + yellow (equal) | black + red dot | warm amber + red stripe |
| **Color count** | **3 strict** | **5 saturated** | **3 strict** | **3 monochrome+** | **4 with grime** | **5 loud** | **3 minimal** | **5 atmospheric** |
| **Typography** | light 14px-tracked sans | italic Impact + chrome | single kanji + micro caption | **5 fonts clashing** | satirical signs + stencil | bold comic-outline + RGB split | **3 typefaces per-word** | Courier tech labels only |
| **Composition** | horizon-anchored, 45% negative | triangle frame + grid + sun | 55% paper as environment | NO grid, overlapping, tilted | central subject + skyline | **zero negative space** | centered paper cuts | cinematic wide horizon |
| **Linework** | hairline 0.3–0.8px | chrome gradients + neon | wet brush varying width | xerox distressed | weathered metal + chrome | heavy 2-3pt black outlines | cut-paper with shadow | painterly gradients |
| **Pattern** | dot grid + tech grid | film grain | paper noise | halftone + paper noise | rust + grime multiply | window grid + wires | paper fiber + pencil marks | atmospheric haze + wet reflection |
| **Mood** | meditative cold-tech-sublime | nostalgic optimism | reverent martial restraint | rebellious anti-corporate | satirical cultural horror | energetic maximalist | witty handmade | grand contemplative |
| **What it rejects** | neon / glitch / scanlines | black bg, minimalism | color, gradients, digital shading | legibility, grid, balance | restraint, subtle palette | negative space, minimalism | digital slick, templates | flat shapes, neon palette |

## Proving legibility

Put any two pieces side by side — you can tell them apart from 10 feet away:

| Pair | What separates them |
|---|---|
| 00 vs 01 | Cold meditative monochrome vs warm maximalist gradient — opposite emotional registers |
| 00 vs 02 | Digital vector precision vs physical brush simulation — opposite execution philosophies |
| 00 vs 03 | Obsessive grid discipline vs grid-breaking rebellion — opposite relationships to structure |
| 01 vs 05 | Synthwave 80s-optimism vs overstimulated cyberpunk-dystopia — both neon-heavy but tonally opposite |
| 02 vs 06 | East-Asian ink gesture vs Western paper-craft concept — opposite cultural registers in restraint |
| 03 vs 07 | Chaos anti-design vs painterly industrial-realism — opposite relationships to the "designed" feel |
| 04 vs 06 | Loud satirical excess vs quiet conceptual restraint — opposite responses to "make a point" |
| 05 vs 07 | Packed illustration + kanji vs atmospheric hero vehicle — both cinematic, totally different |

## The combination test (showcase 08)

Showcase 08 is the **synthesis stress test**. It applies:
- **Composition** rules from Ash Thorp (horizon-anchored, HUD corners, concentric hero construct, massive negative space)
- **Typography** rules from David Carson (multiple fonts clashing, tilted, partial off-page, dingbats substitution)
- **Palette** rules from Yoji Shinkawa (ink black on bone-white paper with one oxblood red accent)

The result reads as: Thorp's polite structure disrupted by Carson chaos, rendered in Shinkawa's restraint. A **polite scream**. Traits from all three profiles remain identifiable simultaneously.

This validates that profiles encode **independent dimensions** of style — they can be mixed, producing recognizable hybrids rather than mush. Not every combination will be beautiful (this one is deliberately uncomfortable), but the technique works.

## How this was made

Each SVG was generated by Claude Opus 4.6 following the tactical rules in its corresponding style profile. Profiles contain:
- Exact hex palette assignments with role percentages
- Typography specs (family, weight, tracking)
- Composition rules (grid / no grid, focal point tactics)
- 7-12 signature moves
- Explicit **negative rules** ("do NOT use neon", "do NOT use balanced composition")

When Claude reads `style-profiles/david-carson.md` and sees `"NOT to use: clean sans-serif headline in center, balanced composition, modular grid"`, it deliberately breaks those defaults. That's how you get output that feels like Carson rather than "generic magazine design."

## Caveats / honest notes

- **These are SVG outputs.** Actual designer-hand production (Illustrator tweaking, real fonts, hand-drawn details) would refine these further. What's shown is LLM-reachable fidelity — the library's ceiling, not a designer's ceiling.
- **Style fidelity is relative.** Compared to the actual designers, these are "recognizable interpretations," not reproductions. The library produces work that clearly **references** a style — it does not replace the designer.
- **The 9 pieces share a tool (SVG).** Different executions (3D render, ink on paper, letterpress print) would make differences more dramatic, but require different tooling.
- **No ML training happened.** This is purely prompt-time retrieval. See [../../TRAINING.md](../../TRAINING.md) for discussion.

## What this demonstrates

1. **Legibility of distinction** — profiles produce recognizably different outputs (claim validated across 8 styles)
2. **Breadth of styles covered** — library handles genres as different as synthwave + sumi-e + chaos typography + cinematic UI + 3D satire + dense cyberpunk + concept-first handwork + industrial realism
3. **Tactical rules work** — explicit "do / don't" instructions in profiles prevent generic defaults
4. **Profiles are composable** — combination test shows synthesis produces coherent hybrids, not mush
5. **Consistency of tooling** — same tool (Claude + SVG), 9 different aesthetic outputs

## Files

```
showcase-2026-04/
├── README.md                            ← you are here
├── 01-signalnoise-synthwave.svg         ← synthwave concert poster
├── 02-shinkawa-ink-mecha.svg            ← ink character study
├── 03-carson-chaos-spread.svg           ← magazine spread
├── 04-beeple-3d-satire.svg              ← satirical 3D cultural commentary
├── 05-josan-dense-cyberpunk.svg         ← maximalist cyberpunk illustration
├── 06-sagmeister-concept-first.svg      ← concept-first paper-cut poster
├── 07-mead-industrial-realism.svg       ← painterly industrial sci-fi concept art
└── 08-combination-test.svg              ← profile synthesis stress test
```

Plus the original Thorp piece in [../2026-04-cyber-art-expo/](../2026-04-cyber-art-expo/).

## Date

2026-04-15
