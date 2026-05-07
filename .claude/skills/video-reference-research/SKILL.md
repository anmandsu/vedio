---
name: video-reference-research
description: Film and craft reference research for AI video projects. Use when collecting comparable works, director/cinematography/editing/production-design/sound/prop/history references, source-graded research packs, or when distilling external film knowledge into usable AI video rules.
---

# Video Reference Research

## Goal

Build the research pack a real crew would need before design and shot planning. Use OpenCLI, web search, local files, and user-provided materials. Distill sources into executable rules, not trivia.

## Required References

Read these as needed:

- `.claude/references/knowledge-source-policy.md`
- `.claude/references/prep-dimensions.md`
- `.claude/references/opencli-research-guide.md`

## Workflow

1. Read `script/story-brief.md`, `script/scene-map.md`, and `script/emotion-map.md`.
2. Decide the project needs by department:
   - director / genre / tone
   - cinematography / lens / light / movement
   - editing / continuity / rhythm
   - production design / color / material / space
   - character / costume / makeup / behavior
   - sound / silence / music / environment
   - historical or factual constraints
3. Collect sources. Prefer Tier A and Tier B sources.
4. For each source, write a source card with URL/path, tier, what it supports, and confidence.
5. Distill each department into conditional craft rules:
   - `When <situation>, do <decision>, because <purpose>.`
6. Write:
   - `research/INDEX.md`
   - `research/director.md`
   - `research/cinematography.md`
   - `research/editing.md`
   - `research/production-design.md`
   - `research/sound.md`
   - `research/source-register.md`

## Distillation Pattern

Use the Nuwa-style principle: capture **how they think**, not just what they said.

For directors, cinematographers, editors, and designers, extract:

- mental models
- decision heuristics
- anti-patterns
- source evidence
- limits and uncertainty

## OpenCLI Usage

Use deterministic OpenCLI adapters first. Use `opencli browser` only when no adapter exists or logged-in browsing is needed. Keep raw extraction out of the final context; summarize into research files.

## Source Grading

Every claim should carry one of:

- `Tier A`: primary source or film text.
- `Tier B`: professional secondary source.
- `Tier C`: social commentary.
- `Tier D`: model inference.

Tier C and D can inspire hypotheses but should not anchor the crew brief alone.

## Stop Condition

Stop research when:

- every high-risk department has at least one Tier A/B anchor, or
- missing sources are explicitly logged in `research/research-gaps.md`.

