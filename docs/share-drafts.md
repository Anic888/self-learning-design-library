# Share Drafts — ready-to-post copy for announcing the library

> Copy-paste-ready text for various communities. Written to be honest (no breathless claims), specific (what's inside, not just vibes), and respectful of each platform's norms.
>
> User posts these manually. Each version is tuned to its audience.

---

## 1. Reddit — r/graphic_design

**Title (under 300 chars, no clickbait):**
```
I built an open-source reference library of 14 designer style profiles to guide AI-assisted design work — looking for feedback from the community
```

**Body:**
```
I've been using LLMs (Claude mostly) for design composition work and kept running
into the same problem: ask for "cyberpunk poster" and you get the AVERAGE of
everything cyberpunk in its training data — generic neon slop, no designer voice.

I built a library that tries to fix this. It's a collection of distilled style
profiles for specific designers (Ash Thorp, Josan Gonzalez, Signalnoise,
Kilian Eng, Syd Mead, Beeple, Paula Scher, Kenya Hara, Peter Saville,
Vignelli, Refik Anadol, Yoji Shinkawa, David Carson, Sagmeister — 14 total).

Each profile is markdown with:
- Extracted palette (hex codes with % role)
- Typography spec (family, weight, tracking)
- Composition rules
- Signature moves
- Explicit "do NOT use X" negative rules
- Tactical instructions an LLM can literally follow

The point is: when an AI reads `style-profiles/ash-thorp.md` and sees
"hairline strokes only (0.3-0.8px), NO neon gradients, NO scanlines as
decoration," it stops defaulting to generic cyberpunk and actually produces
work that feels like Thorp.

I stress-tested it with 8 SVG posters across 8 different styles. Showcase
README in the repo has a side-by-side comparison table across 9 parameters.
If you look at the Signalnoise synthwave poster next to the Shinkawa sumi-e
ink study next to the Carson chaos magazine spread — they're all the same
tool (Claude generating SVG), but you can tell them apart immediately.
That's the claim I'm trying to validate.

Honest limitations (written into the TRAINING.md):
- Style profiles are interpretations, not canonical truths
- LLM output won't match an actual designer's hand — library raises the
  floor, not the ceiling
- No ML training — this is retrieval context, not fine-tuning

Looking for:
- Designers to critique the profiles (are my palette extractions right?
  am I mischaracterizing anyone?)
- Contributors to add designers or refine existing ones (quality bar is
  documented in CONTRIBUTING.md)
- Honest "this is dumb because X" feedback

MIT licensed. Fork freely. Issues / PRs very welcome.

[github.com/Anic888/self-learning-design-library]
```

---

## 2. Hacker News — Show HN

**Title (under 80 chars):**
```
Show HN: Design style library for LLM-assisted design work (14 designers, MIT)
```

**First comment (context paragraph, posted after submission):**
```
Hi HN,

This started because I was using Claude to draft posters and kept getting
generic "cyberpunk" output — the mean of everything in its training data.

So I wrote 14 designer style profiles as markdown files (Ash Thorp, Signalnoise,
Kilian Eng, Josan Gonzalez, Syd Mead, Beeple, Sagmeister, Carson, Shinkawa,
Paula Scher, Kenya Hara, Peter Saville, Vignelli, Refik Anadol). Each profile
has extracted palettes (hex + %), typography specs, composition rules, signature
moves, AND explicit negative rules ("don't use RGB split on Thorp" etc.).

The LLM reads the profile and actually follows the constraints. Reference
works in my-works/ demonstrate this (NEO-GENESIS poster in Ash Thorp,
Shinkawa ink mecha, with more to come).

Architecture is deliberately boring: plain markdown, no tooling, works with
any LLM that can read files. The cleverness is in the tactical "do / don't"
instructions — they prevent the defaulting that makes AI design work feel
generic.

Explicit about limitations: this is retrieval, not training. It raises the
floor on AI-assisted design output, doesn't replace designers. TRAINING.md
has honest notes on what "training" means in this context.

Would love feedback on (1) quality of the profiles themselves (designers?
historians?) and (2) whether the architecture makes sense for other knowledge
domains.

Repo: github.com/Anic888/self-learning-design-library
```

---

## 3. Product Hunt — Coming Soon format

**Tagline (max 60 chars):**
```
Designer style profiles that actually teach AI to design
```

**Short description (max 260 chars):**
```
14 designer profiles as markdown (Ash Thorp to Sagmeister). Plain-text
rules with hex palettes, typography specs, and explicit "do NOT" lists
that prevent generic AI output. Retrieval-based, MIT licensed,
markdown-first. Works with any LLM.
```

**Long description:**
```
Claude, GPT, and local LLMs produce generic design work by default — the
average of everything they saw in training. Ask for "cyberpunk poster" and
you get neon-slop cliché.

This library is 14 distilled designer style profiles that fix that. Each
profile contains:

• Palette (hex codes with role percentages)
• Typography spec (family, weight, letter-spacing)
• Composition rules
• 7-12 signature moves
• Explicit "do NOT" negative rules
• Tactical instructions an LLM can follow

When the LLM reads the Ash Thorp profile and sees "hairline strokes only,
NO neon gradients, monochromatic + ONE accent," it produces cinematic-UI
work instead of default cyberpunk.

Includes:
• 14 style profiles (Thorp, Josan Gonzalez, Signalnoise, Kilian Eng,
  Syd Mead, Beeple, Sagmeister, Carson, Shinkawa, Paula Scher, Kenya Hara,
  Peter Saville, Vignelli, Refik Anadol)
• 3 universal design principles (color, typography, composition)
• 3 deep-dive analyses of iconic works
• 8 showcase SVGs demonstrating the library works across radically different
  styles (one generated per profile to validate outputs are legibly distinct)
• Honest TRAINING.md explaining the 5 paths from retrieval to LoRA training

Architecture is markdown-first. Works with any LLM. MIT licensed. Open to
contributions via GitHub (CONTRIBUTING.md has quality bar + templates).

This won't make AI produce professional-designer-level work. It stops AI
from producing generic defaults.
```

---

## 4. Twitter / X thread

**Tweet 1 (under 280 chars):**
```
Built an open-source library of designer style profiles that actually teach AI
to stop producing generic "cyberpunk" defaults.

14 designers distilled into markdown with hex palettes, typography specs,
composition rules, and explicit "do NOT" lists.

MIT. Link below.
```

**Tweet 2:**
```
The problem: ask Claude for "cyberpunk poster" and you get the mean of
all cyberpunk in its training data. Neon slop. No voice.

The fix: feed it a profile that says "hairline strokes only, NO neon
gradients, monochromatic + ONE accent" and it produces Thorp instead.
```

**Tweet 3:**
```
Library includes:
• 14 style profiles (Thorp, Josan, Signalnoise, Kilian Eng, Mead, Beeple,
  Sagmeister, Carson, Shinkawa, Paula Scher, Hara, Saville, Vignelli, Anadol)
• 3 universal principles
• 3 deep analyses
• 8 showcase SVGs proving the library produces legibly distinct outputs
```

**Tweet 4:**
```
Stress test: I generate SVG posters in radically different styles using
the same tool (Claude + SVG), changing only which profile is referenced.

Put a Thorp one next to a Shinkawa one — they're unmistakable. Reference
pieces live in my-works/.
```

**Tweet 5 (closing):**
```
Honest about limitations (in TRAINING.md):
• Not ML training — this is retrieval
• Won't match a real designer's hand
• Raises the floor, not the ceiling

MIT licensed. Fork freely. Contributions welcome.
Repo: github.com/Anic888/self-learning-design-library
```

---

## 5. Telegram design channels / Discord servers

**Short form (~500 chars):**
```
Shipped a little open-source thing: a library of 14 designer style profiles
for LLM-assisted design work.

Each profile is markdown — extracted palettes (hex + %), typography specs,
composition rules, signature moves, and explicit "do NOT" lists. An LLM reads
it and produces work that actually feels like the referenced designer, not
generic default.

14 designers (Thorp, Josan Gonzalez / Death Burger, Signalnoise, Kilian Eng,
Mead, Beeple, Sagmeister, Carson, Shinkawa, Paula Scher, Kenya Hara, Peter
Saville, Vignelli, Refik Anadol) + 8 showcase SVGs proving the approach works.

MIT. Feedback / PRs very welcome:
github.com/Anic888/self-learning-design-library
```

---

## Platform-specific tips when posting

**Reddit:**
- Post to r/graphic_design and r/design (not r/webdev — wrong audience)
- Engage with comments within first 2 hours for algorithm pickup
- Don't cross-post identically to multiple subs (Reddit flags duplicate titles)
- Expect some "AI slop" hostility — the honest-limitations framing helps
- r/typography might be receptive given the typographic rigor

**Hacker News:**
- Submit Tuesday-Thursday morning US time for best exposure
- Use "Show HN:" prefix (it's tracked separately)
- First-comment context within 1 minute of post (HN convention)
- Expect technical questions — be prepared to answer on architecture, not just design

**Product Hunt:**
- "Coming Soon" lets you gather followers before launch
- Schedule Tuesday launch (PH best-day convention)
- Include screenshots of showcase SVGs
- Engage with hunters' questions

**Twitter/X:**
- Post first tweet standalone, add thread as replies
- Tag: @pentagram, @signalnoise, etc. SPARINGLY — only if content legitimately relates
- Include at least one showcase SVG image (platform favors media posts)
- Engage replies, don't ignore

**Telegram / Discord:**
- Match channel tone — some are formal, some casual
- Link at end, not in first line (otherwise scanned as spam)
- Don't cross-post to multiple channels rapid-fire

## Honest caveats to include in all versions

- "Not ML training — retrieval context"
- "Won't match a designer's actual hand"
- "Library raises the floor, not the ceiling"
- "Profiles are interpretations, not canonical"
- "Looking for feedback / contributions, not promotion"

These aren't weaknesses to hide — they're differentiators from the
breathless "AI replaces designers" marketing that most AI-design tools lead
with. Being honest reads as legitimacy.

## Last updated
2026-04-15
