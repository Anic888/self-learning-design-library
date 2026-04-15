# Design Library

> A structured reference library for working with LLM coding assistants on design tasks. Distilled designer style profiles, composition principles, and project history — organized so an AI assistant (Claude, GPT, local LLMs) can read relevant context on demand.

**Not a training dataset in the machine-learning sense.** It's a **retrieval library** — purpose-built markdown files that an LLM reads at runtime to produce grounded, style-aware design work. Think moodboard + style guide + tactical instructions, rendered as parseable text.

## Why this exists

Vanilla LLMs, asked to "design a cyberpunk poster," produce generic cyberpunk — the average of everything in their training data. To get work in the voice of **a specific designer** (Ash Thorp minimalist, Kilian Eng retrofuturist, David Carson chaos-typography), you need references the model can actually consult.

This library is the references, written in a format LLMs read well:
- **Source indexes** — portfolio URLs (single source of truth)
- **Style profiles** — distilled tactical rules for applying a style
- **Principles** — universal design knowledge (color, typography, composition)
- **Work history** — past projects for consistency and evolution

## How it works

```
User:   "Design a festival poster in the style of Kilian Eng."
Claude: reads style-profiles/kilian-eng.md
        → extracts palette, composition tactics, signature moves
        → generates work following those rules
        → saves to my-works/YYYY-MM-project-name/
```

The tactical rules in each style profile are written for an LLM to **actually follow**, not just read:
- Exact hex codes per role
- Typography specs (weight, tracking, size relative)
- Composition patterns ("horizon-anchored, 40% negative space")
- Things to use + things to avoid (explicit negative rules)

## Repository structure

```
design-library/
├── SETUP.md                   # how to use (detailed workflow)
├── README.md                  # you are here
├── CONTRIBUTING.md            # how to add designers / principles
├── TRAINING.md                # how to extend + thoughts on real ML training
├── LICENSE                    # MIT
│
├── sources/                   # source-of-truth: links + metadata
│   ├── designers/             # one .md per designer with portfolio URLs
│   ├── collections/           # curated resource libraries (Envato, Canva, Behance)
│   └── principles/            # universal design knowledge
│
├── style-profiles/            # MAIN WORK ZONE — distilled tactical profiles
│                              # this is what Claude reads at composition time
│
├── analyses/                  # breakdowns of specific works (filled on demand)
│
├── my-works/                  # projects built using the library
│
└── templates/                 # templates for new entries
```

## Current inventory (v1)

**9 designers** seeded across genres:

| Designer | Genre | Best for |
|---|---|---|
| Ash Thorp | Cinematic UI, minimalist sci-fi | Cold atmospheric tech, BR2049 vibes |
| Josan Gonzalez | Dense cyberpunk editorial | Maximalist packed cyberpunk illustration |
| James White / Signalnoise | 80s retrofuturism, synthwave | Nostalgic optimism, sunset gradients |
| Syd Mead | Legacy industrial concept art | Painterly gravitas, realistic futurism |
| Beeple | 3D satirical daily-art | Cultural commentary, absurd 3D |
| Kilian Eng | Retrofuturism screen-print | Warm nostalgic sci-fi posters (Mondo) |
| Yoji Shinkawa | Sumi-e ink + mecha | Traditional Japanese ink, high contrast |
| David Carson | Chaos typography, grunge | Anti-grid rebellion, emotional layouts |
| Stefan Sagmeister | Concept-first brand | Big ideas via unusual materials |

**3 collections:** Envato Elements index, Canva favorites, Behance cyberpunk
**3 principles:** color theory, typography hierarchy, composition & grids

## Getting started

### 1. Fork + clone
```bash
gh repo fork <this-repo> --clone
cd design-library
```

### 2. Point your LLM at it
With Claude Code, Cursor, or any LLM with filesystem access:

**Option A — Direct reference** (simplest)
```
"Read ~/path/to/design-library/style-profiles/ash-thorp.md and
 design a poster in that style for a [topic] event."
```

**Option B — Memory pointer** (for Claude Code users)
Add a reference memory entry pointing to the library so it's auto-loaded on design tasks:
```markdown
---
name: Design Library
type: reference
---
Location: ~/Documents/design-library/
Read style-profiles/*.md when user asks for design work in a designer's style.
```

**Option C — Agent skill** (advanced, Claude Code)
Create a custom skill that auto-triggers on design-related prompts and reads the library.

### 3. Request design work
```
"Design a synthwave concert poster in the style of James White (Signalnoise).
 Combine with Kilian Eng's screen-print texture sensibility.
 Save to my-works/."
```

The LLM reads both style profiles, synthesizes their tactical rules, generates output.

## Scaling the library

Scaling = adding designers, updating style profiles, growing collections.

**To add a designer:**
```
"Add [designer name] to the library."
```

Claude will:
1. Create `sources/designers/<slug>.md` with portfolio links
2. Fetch 3-5 representative works (WebFetch / browser MCP)
3. Write `analyses/<slug>/*.md` per work
4. Synthesize `style-profiles/<slug>.md`

**To refresh a profile:**
```
"Update [designer name] — check for recent work."
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for manual contribution workflow.

## Honest limitations

- **Style profiles are subjective interpretations**, not canonical truths. A designer's own words would beat my distillation.
- **LLMs still hit ceilings.** The library raises the floor of AI-generated design but does not produce a professional designer.
- **Link rot.** Designers delete work, rename sites, move hosts. Profiles need periodic refresh.
- **Visual output quality** depends on your LLM + tools (SVG-writing, image generation, etc). The library provides direction; execution still varies.
- **No image training.** This library is for context/retrieval, not for fine-tuning image generators. See [TRAINING.md](TRAINING.md) for actual model training approaches.

## Design philosophy

**Links-primary + profile-cached.**
Source URLs are truth (fresh, current). Style profiles are working layer (fast, distilled). This keeps the library small (markdown, ~150 KB) while enabling rich context per designer.

**Markdown-first.**
Every LLM parses markdown. No custom format, no tooling required. Plain files, git-native, diff-friendly.

**Explicit negative rules.**
Style profiles say both what to use AND what NOT to use. LLMs need explicit "don't" instructions to avoid defaulting to generic.

## Roadmap (potential)

- [ ] Add 10+ more designers across underrepresented genres (Swiss, brutalist, Asian)
- [ ] Add specific work analyses for top 3 per designer
- [ ] Create Claude skill package (`design-mentor.skill.md`)
- [ ] LoRA training companion guide for image models (see [TRAINING.md](TRAINING.md))
- [ ] Multi-language (Russian/Japanese profile translations)
- [ ] Collections for stock resources (Envato saved, Canva favorites, Behance galleries)

## License

MIT — see [LICENSE](LICENSE). Fork freely, contribute back optionally.

## Credits

Initiated April 2026 as a personal assistant library, open-sourced for community extension.

Designer profiles are **interpretations based on public work**. All designers retain rights to their actual work. Links point to official portfolios.

---

*Collaborate by forking and submitting pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md).*
