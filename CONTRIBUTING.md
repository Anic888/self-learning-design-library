# Contributing to Design Library

Thanks for considering a contribution. The library grows through additions (new designers, principles, collections) and refinements (updated profiles, corrected details, better examples).

## Ways to contribute

1. **Add a designer** — new style profile + source file
2. **Refine an existing designer** — better palette extraction, new signature moves, corrections
3. **Add a principle** — universal design knowledge useful across styles
4. **Add a collection** — curated resource library (stock asset service favorites, Pinterest boards, Behance galleries)
5. **Fix inaccuracies** — link rot, factual errors in bios
6. **Add an analysis** — detailed breakdown of a specific work
7. **Translate** — bilingual profiles (currently EN; Russian/Japanese/Spanish welcome)

## Adding a designer

### Files required
Two files per designer:

```
sources/designers/<slug>.md       # portfolio links, key works, reason why included
style-profiles/<slug>.md          # distilled tactical profile (main work)
```

### Slug convention
- Lowercase kebab-case: `ash-thorp`, `josan-gonzalez`, `james-white-signalnoise`
- For collectives / studios: append identifier: `pentagram-paula-scher` or `sagmeister-and-walsh`

### Use the templates
```bash
cp templates/source-designer-template.md sources/designers/<slug>.md
cp templates/style-profile-template.md style-profiles/<slug>.md
# fill in
```

### Quality bar for style profiles

A great style profile has:

- [ ] **Palette with hex codes** (5-6 colors max with role % estimate)
- [ ] **Typography spec** — genre, weight tendencies, letter-spacing behavior
- [ ] **Composition tactics** — grid discipline, focal point, negative space
- [ ] **Signature moves** — 7-12 bullet specifics someone can identify
- [ ] **Tools** — what the designer actually uses
- [ ] **Mood/register** — emotional positioning
- [ ] **When to apply** — 3-5 positive scenarios + 3-5 anti-scenarios (NOT lists)
- [ ] **Tactical instructions** — 8-12 numbered imperatives an LLM can follow literally
- [ ] **At least 3 key references** with dates
- [ ] **Portfolio sources linked** to source file
- [ ] **Dated last sync** for freshness tracking

### Quality bar for source files

- [ ] **Identity** — full name, location, active period, role
- [ ] **Portfolio URLs** — minimum 2 sources, ideally website + one social
- [ ] **Focus areas** — what they specialize in (3-5 bullets)
- [ ] **Why this designer** — 1 paragraph on what problem space they solve for you
- [ ] **Key works queue** — 4-6 specific pieces worth analyzing in depth
- [ ] **Adjacent/collaborators** — other designers with similar or complementary style
- [ ] **Last profile sync** — date

## Adding a principle

Principles go in `sources/principles/`. They should be:

- Universal (not style-specific)
- Actionable (LLM can apply, not just read)
- Bounded (2-4 pages of markdown max)
- Backed by examples (reference designers in the library who demonstrate)

Examples: `color-theory.md`, `typography-hierarchy.md`, `composition-grids.md`.

Good additions: grid systems, readability, visual weight, motion principles, responsive design, print vs digital.

## Adding a collection

Collections in `sources/collections/`. These index **external resources** like stock platforms, reference sites, moodboards. Format:

```markdown
# [Platform Name] — Curated Resources

## Access
- Platform URL
- Auth required? How to access (MCP tool, WebFetch, etc)
- Search/filter tips

## Saved items / favorites
Structured list of item names + URLs + use cases

## Patterns that work
Search queries, filters, categories that yield good results

## Notes
Anything specific to this platform
```

## Submitting a pull request

```bash
# Fork via GitHub UI, then:
git clone https://github.com/<your-username>/design-library.git
cd design-library
git checkout -b add-<designer-slug>

# Make changes
# ...

git add sources/designers/<slug>.md style-profiles/<slug>.md
git commit -m "Add [Designer Name]: [one-line why notable]"
git push origin add-<designer-slug>

# Open PR on GitHub
```

### PR checklist

- [ ] Files follow the structure and templates
- [ ] Style profile meets quality bar (see above)
- [ ] All links work at time of submission
- [ ] `SETUP.md` inventory table updated
- [ ] No copyrighted content reproduced (descriptions only, links to originals)
- [ ] Commit message describes what was added

## Style of writing

- **Terse but specific.** "Horizon line at ~60% from top" is better than "compositions often use horizon elements."
- **Negative rules matter.** "NOT neon gradients" helps LLMs avoid defaults.
- **Hex codes, not color names.** `#FF6A00` reproducible, "burnt orange" isn't.
- **Tactics over taste.** This is a rulebook, not an art criticism essay.

## Respecting designers

This library **describes public design work**; it does not reproduce or reimplement it. We link to originals. If a designer asks to be removed, we remove.

- Never upload copyrighted images
- Never reproduce full artworks (small thumbnails for profile identification are OK with attribution)
- Always link to the designer's own site/social as primary source

## Questions, issues

Open an issue in the repo. Tag with:

- `new-designer` — proposing addition
- `profile-refinement` — fixing existing
- `principle` — universal knowledge addition
- `meta` — library structure / tooling

Thanks for contributing.
