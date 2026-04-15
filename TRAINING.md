# Training Notes

> Honest thoughts on "training a model with this library" — what works, what doesn't, what's overkill.

## Short version

**This library is not for training machine learning models.** It's for **retrieval** — LLMs read it at runtime to ground their output.

If you want a model that truly "learns" a design style (at the pixel level), you need to train an image generation model on images, not markdown descriptions. This library complements that, but doesn't replace it.

## Options, in order of practicality

### 1. Retrieval-augmented use (default — what this library is for)

**How it works:** Your LLM (Claude, GPT, Llama-variants) reads the library files at prompt time.

**Setup cost:** $0. Just clone the repo and point the LLM at it.

**Quality ceiling:** LLM's general capability + the quality of your profiles. Will not exceed the LLM's training data + your prompts. But it **dramatically raises the floor** by preventing generic defaults.

**Best for:** Layout composition, typography decisions, palette selection, conceptual direction. Text-to-SVG, text-to-code generation guided by style constraints.

**Worst for:** Producing raster imagery "in the style of" a specific artist at pixel-fidelity.

**This is what 95% of users should do.** Start here.

### 2. Long-context / system prompting

**How it works:** Load all style profiles into your LLM's system prompt or long-context window. The LLM has full library in memory for the session.

**Setup cost:** $0 (just prompt engineering). Requires 100K+ context LLM (Claude Opus, GPT-4, Gemini).

**Quality:** Same as retrieval, slightly more coherent because model sees all options simultaneously.

**Best for:** Interactive design sessions where you may jump between designers mid-conversation.

**Implementation:**
```python
# Pseudo-code
profiles = read_all("style-profiles/*.md")
principles = read_all("sources/principles/*.md")
system_prompt = f"You are a design assistant. Reference these when relevant:\n\n{profiles}\n\n{principles}"
# ... use in chat
```

### 3. Fine-tuning small LLMs (intermediate effort)

**How it works:** Use the library as a training corpus for a small open LLM (Llama 3, Mistral 7B, Gemma). The model "internalizes" the profiles.

**Setup cost:** $20-150 compute for fine-tune on Replicate/Modal. 1-2 days work.

**Quality:** Slightly faster inference, no context overhead, model has profiles in its weights. But marginal over retrieval for this use case.

**Not worth it** for most users. Retrieval is easier and equally good.

### 4. LoRA training on image generation models (the real "style learning")

**How it works:** Fine-tune Flux/SDXL/Stable Diffusion on reference images of a designer's work. The LoRA learns visual patterns at pixel level.

**Setup cost:** 15-30 reference images per designer, $20-60 compute on Replicate/fal.ai/Modal.

**Quality:** Produces raster imagery that genuinely resembles the designer's style. Not editable vector. Use as input for compositing.

**Workflow:**
1. Collect 15-30 reference images from the designer's portfolio (respect copyright — use for personal/research only)
2. Train LoRA on Flux.1 [dev] or SDXL via Replicate / Civitai tools / Kohya
3. Use the LoRA to generate imagery
4. Import into your design tool (Illustrator, Figma) as inspiration / background plates
5. Claude helps you compose the vector layout on top

**Combining with this library:** Use LoRA for raster imagery + this library for composition direction + Claude for SVG code output. That's the full stack.

### 5. Full model training from scratch

**Don't.** Not worth it for any realistic user. Flux/SDXL are state of the art and open. Fine-tune or LoRA them. Do not train your own image model.

## What a "self-improving" workflow looks like

The library getting better over time:

1. **Week 1:** Start with seeded profiles (general-knowledge-based, not fresh-analyzed)
2. **As you work:** For each project, Claude reads profiles. If output is off, you correct → Claude offers profile refinement → merge update
3. **Monthly:** Run "refresh" commands on top-used designers (Claude pulls latest from their sites)
4. **New work enters my-works/:** Acts as continuity corpus — future work references past style choices
5. **Analyses folder fills:** Deep-dive analyses of specific works accumulate as targeted references

Over 6-12 months, a well-maintained library has 30+ designers, 60-100 detailed analyses, tracked evolution of your own work. At that scale, the retrieval context becomes genuinely powerful.

## Practical advice

- **Don't try to "teach" the LLM by chatting.** LLMs forget between sessions. Write to files.
- **Use the `analyses/` folder for specific project references.** When you discover a work that's perfectly aligned with a project you're working on, analyze it and save it. Future Claude will find it.
- **Update `last sync` dates** when you refresh profiles. Stale data is worse than no data.
- **Keep style profiles short + tactical.** 200-400 lines is ideal. If a profile grows past 500 lines, you're writing an essay; split into analyses.
- **Write "don'ts".** LLMs default to generic. "Don't use RGB split on Thorp" prevents recurring mistakes.

## Measuring improvement

If you want to track whether your library is actually helping:

1. **Baseline:** Ask LLM to "design X" without any library context. Save output.
2. **With library:** Ask LLM to "design X in style of [designer]" with library loaded. Save output.
3. **Compare over time:** Take screenshots, stash in `my-works/<date>-comparisons/`.
4. **User study (optional):** Show unbranded outputs to design-savvy friends, ask "which looks more like [designer]?" See if library-versions win.

## Frequently asked about training

**"Can I train Claude / GPT specifically?"**
No. Commercial API models aren't user-fine-tunable at the weight level. Closest is giving them the library as context — what this project is for.

**"What about RLHF / DPO on designer preferences?"**
Possible for small open models (Llama, Mistral), not for commercial APIs. Overkill for 99% of users.

**"Can I share my LoRA weights?"**
Depends on licensing. Training a LoRA on a designer's copyrighted work and redistributing the weights is **legally murky** at best. Keep LoRAs personal. This library of descriptions is fine because descriptions are fair use; weights derived from copyrighted images are not.

**"Should I use RAG with a vector DB?"**
For this library size (~10 MB), no. Just load the whole thing into context, or use simple file reads. Vector DBs are worth it at 1000+ documents. We're at ~30.

## The honest take

**Style profiles + LLM ≠ professional designer.** A style profile captures 60-70% of what makes a designer recognizable — enough for the LLM to stop producing default-cyberpunk and actually feel like Kilian Eng instead of Ash Thorp. The remaining 30-40% is technique, craft, judgment calls, and years of practice that no library can substitute.

The library's purpose is not to replace designers. It's to make the LLM's design output **legibly distinct** — someone should be able to look at two pieces and say "this one's Thorp, this one's Josan." That's achievable with a good library. Mastery isn't.

Use accordingly.
