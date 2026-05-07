# Workflow Parallelization Notes

## Summary

The current AI video workflow is written as a safe linear pipeline, but several parts can run in parallel without weakening the quality gates. The main rule is:

- Keep decision gates serial: story lock, crew brief synthesis, visual bible lock, continuity gate, visual approval.
- Parallelize evidence gathering, department drafts, scene-local assets, prompt pattern study, batch generation, downloads, and first-pass reviews.
- Give every parallel worker a disjoint output file or asset scope, then merge at explicit checkpoints.

## Dependency Map

```text
script intake
  -> parallel research lanes
       director / narrative
       cinematography / lighting
       production design / spatial
       character / costume
       sound
       editing / continuity
       prompt pattern library study
  -> crew brief synthesis
  -> second read + visual bible lock
  -> parallel scene/character/prop bibles
  -> shot planning by sequence or scene
  -> validation + continuity review
  -> prompt writing by shot or asset group
  -> batch image generation + concurrent download
  -> visual review batches
  -> accepted fingerprints + next generation wave
```

## Safe Parallel Areas

### 1. After Script Intake: Research Lanes

Once `script/story-brief.md`, `script/scene-map.md`, and `script/emotion-map.md` exist, research can split by department:

| Lane | Output | Can Run With |
|---|---|---|
| Director / narrative | `research/director.md` | all other research lanes |
| Cinematography | `research/cinematography.md` | production design, sound, editing |
| Production design / spatial | `research/production-design.md` | cinematography, character |
| Character / costume | `bible/characters/*` drafts or research notes | scene/prop research |
| Sound | `research/sound.md` | all visual research |
| Editing / continuity | `research/editing.md` | camera/design research |
| Source register | `research/source-register.md` fragments, then merge | all lanes |

Best practice: each lane writes its own file and source cards. Merge only after all high-risk departments have Tier A/B anchors or logged gaps.

### 2. Nuwa Distillation

Nuwa itself is already designed for parallel research dimensions. Use it for director/cinematographer/designer methodology distillation while normal visual/source research continues.

Parallelizable:

- creator writings
- long interviews
- external analysis
- decision records
- timeline
- expression or craft DNA

Serial gate:

- final extraction into reusable craft rules
- quality verification

### 3. Visual Bible Drafting

After the crew brief exists, bible work can split by recurring element:

| Work Unit | Output |
|---|---|
| Main character A | `bible/characters/<name>.md` |
| Main character B | `bible/characters/<name>.md` |
| Main location | `bible/scenes/<scene_id>.md` |
| Recurring props | `bible/props/<prop_name>.md` |
| Moodboard / references | `bible/moodboard/INDEX.md`, `research/atmosphere_refs/*` |

Serial gate:

- lock the final identity anchors, scene geography, palette, and anti-patterns before generation.

### 4. Shot Planning By Sequence

After the crew brief and visual bible are stable, shot planning can split by scene or sequence.

Safe split examples:

- Scene 1-3 writer
- Scene 4-6 writer
- Scene 7-9 writer
- Dedicated storyboard/nine-grid reviewer
- Dedicated cinematography pass
- Dedicated editor-continuity pass

Merge requirements:

- one owner normalizes shot ids, style, duration rhythm, and continuity handoffs
- run `.codex/scripts/validate_vpipe_yaml.py`
- run `.codex/scripts/continuity_lint.py`
- complete cinematic continuity review

### 5. Prompt Writing

Prompt writing can run in parallel after the shot plan and bible anchors are available.

Safe split:

- character prompts
- scene establishing prompts
- prop prompts
- shot image prompts
- video motion prompts
- prompt library case study

Important constraint:

- every prompt must cite the same approved bible/fingerprint anchors to avoid style drift.

### 6. Generation And Downloads

The strongest existing speed win is already implemented in `.codex/scripts/gen_api.py`:

```bash
python .codex/scripts/gen_api.py batch "<manifest.json>" --output-dir="<renders_dir>" --concurrency=10 --download --download-concurrency=10
```

Use this for independent images:

- character sheets
- props
- first-pass scene variations
- non-dependent shot stills

Use smaller batches when:

- prompts are very large
- provider rate-limits
- one output depends on a previous accepted reference

### 7. Visual Review

Visual review can be batched by asset group:

- character identity review
- scene/location review
- prop review
- shot sequence review

Do not review all assets as one giant batch. Review by continuity risk, then extract fingerprints from approved frames immediately.

## Must Stay Serial

| Gate | Why |
|---|---|
| First script read | All departments need the same story premise |
| Crew brief synthesis | Parallel research must collapse into one shared doctrine |
| Visual bible lock | Generation needs stable anchors |
| First image per recurring location/character | Later variations depend on the accepted reference |
| Fingerprint extraction | Must use approved images only |
| Final continuity approval | Adjacent shot relationships are sequence-level, not isolated |
| Final visual approval | Drift can accumulate across a batch |

## Recommended Fast Schedule

### Wave 0: Setup

1. Create project structure.
2. Finish script intake.
3. Write scene map, emotion map, production risks.

### Wave 1: Parallel Research

Run 5-7 lanes at once:

- narrative/director
- cinematography/light/lens
- production design/material/space
- character/costume
- sound
- editing/continuity
- physical and atmosphere image references

Checkpoint: `research/INDEX.md`, `research/source-register.md`, and `research/research-gaps.md` are complete enough.

### Wave 2: Parallel Drafts

While the crew brief is being synthesized:

- study prompt pattern cases
- draft scene bibles
- draft character bibles
- collect atmosphere refs
- prepare generation manifests, but do not launch final generation yet

Checkpoint: crew brief and bible anchors are locked.

### Wave 3: Shot And Prompt Production

Split by sequence:

- write VPipe segments
- write nine-grid plans for key shots
- write prompt files
- run validation and continuity lint as soon as each segment lands

Checkpoint: full YAML validates and has no BLOCK continuity issues.

### Wave 4: Batched Generation

Use batch generation in dependency order:

1. master characters / master locations / key props
2. visual review and fingerprint extraction
3. dependent shot stills and time variations using references
4. visual review again
5. video generation only for approved stills

## Practical Speed Rules

- Do not let two workers write the same file. Use separate department files or scene-specific files, then merge.
- Start slow tasks early: visual references, downloads, image generation, and source extraction.
- Treat `source-register.md` as a merge product, not a live file everyone edits at once.
- Use batch generation only for independent prompts. For reference-dependent work, batch by dependency layer.
- Keep batch sizes moderate: start with `--concurrency=6`, raise to `10` if stable, drop to `3-4` if rate-limited.
- Review early samples before launching a large dependent batch. One bad anchor can poison many variations.

## Expected Speedup

Conservative estimate:

- Research: 2-4x faster with department lanes.
- Prompt writing: 2-3x faster with shot/asset splits.
- Image generation/download: up to 5-10x faster when provider accepts concurrency.
- End-to-end project: usually 35-60% faster, because serial gates still remain.

The biggest avoidable slowdown is late discovery of bad anchors. Parallelism should accelerate evidence and production, but the anchor-locking gates should stay deliberate.
