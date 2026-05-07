---
name: video-script-intake
description: First-pass script and episode intake for AI video production. Use when Codex needs to read a script, outline, treatment, existing VPipe YAML, or episode material and produce story understanding, scene map, emotional arc, production risks, and next-step questions before research or shot planning.
---

# Video Script Intake

## Goal

Turn raw story material into a stable project brief. Do not write final shots yet. First understand what the piece wants to be.

## Inputs

Accept any of:

- `script/script.md`, PDF transcript, outline, treatment, dialogue draft.
- Existing shot YAML such as `episode_1_vpipe_v2.yaml`.
- User-provided summary.

## Workflow

1. Create or locate `projects/<project_id>/`.
2. Read the source material once without department assumptions.
3. Write these files:
   - `script/story-brief.md`
   - `script/scene-map.md`
   - `script/emotion-map.md`
   - `script/production-risks.md`
   - `script/questions.md`
4. If the source is existing shot YAML, also summarize its schema, recurring characters, locations, beat types, and style rules.
5. Stop for user confirmation if major genre, tone, or audience assumptions are uncertain.

## Output Schema

`story-brief.md`:

```markdown
# Story Brief

## Logline

## Genre And Format

## Core Promise

## Audience Emotion

## World Rules

## Main Conflict

## What Must Not Be Lost
```

`emotion-map.md`:

```markdown
# Emotion Map

| Scene | Starting Emotion | Turn | Ending Emotion | Audience Should Feel |
|---|---|---|---|---|
```

`production-risks.md`:

```markdown
# Production Risks

| Risk | Why It Matters | Later Department Owner |
|---|---|---|
| Character consistency | Recurs across scenes | visual bible / continuity |
| Scene continuity | Same space appears across shots | production design / editor |
```

## Rules

- Separate what the script says from what you infer.
- Preserve exact script anchors for later use.
- Do not over-research during first read.
- Do not generate final prompts before the visual bible exists.

