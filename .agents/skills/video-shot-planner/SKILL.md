---
name: video-shot-planner
description: Write detailed AI-video shot plans, VPipe YAML, nine-grid storyboard frame plans, image/video prompts, and generation handoff files from a script, crew brief, and visual bible.
---

# Video Shot Planner

## Goal

Turn the approved script understanding, crew brief, and visual bible into detailed shot plans that can survive image/video generation.

## Required References

Read `.Codex/references/shot-schema-vpipe.md` before writing or editing VPipe YAML.

Read `awesome-gpt-image-2-prompts-main/cases/` to study prompt patterns before writing generation prompts. Match the shot category to the right case file:

| Shot Type | Reference Case File |
|-----------|-------------------|
| Character closeup, emotional beat, reaction | `cases/portrait.md` |
| Establishing shot, key art, wide scene | `cases/poster.md` |
| Character sheet, turnaround, reference | `cases/character.md` |
| UI/screen interface in shot | `cases/ui.md` |

For each reference case, read the output image (`images/<category>_case<N>/output.jpg`) with Codex's Read tool to understand what the prompt actually produces.

## Inputs

- `script/story-brief.md`
- `script/scene-map.md`
- `script/emotion-map.md`
- `crew/creative-brief.md`
- `bible/characters/*`
- `bible/scenes/*`
- `bible/props/*`
- `awesome-gpt-image-2-prompts-main/cases/` — prompt pattern library (mandatory reference)

## Outputs

- `shots/<episode>_vpipe.yaml`
- `boards/<shot_id>_nine_grid.md`
- `prompts/<shot_id>_image_prompt.md`
- `prompts/<shot_id>_video_prompt.md`

## VPipe Required Fields

Each shot must include:

- `shot_id`
- `scene_id`
- `character`
- `location`
- `plot`
- `performance`
- `lighting`
- `camera`
- `blocking`
- `sound`
- `dialogue`
- `duration_sec`
- `beat_type`
- `style_notes`

Recommended extra fields:

- `continuity_from`
- `continuity_to`
- `visual_anchors`
- `negative_prompt`
- `generation_notes`

## Nine-Grid Frame Plan

For each important shot, create nine frames:

1. setup
2. attention hook
3. first action
4. emotional turn
5. spatial reveal
6. peak gesture or impact
7. reaction
8. exit motion
9. tail frame for next-shot connection

Use nine-grid for temporal evolution, not nine random composition ideas.

## Prompt Writing Workflow

For each shot that needs a generation prompt, follow this sequence:

1. **Match the category** — determine the closest prompt library category (portrait / poster / character / ui).
2. **Study 2-3 reference cases** — read the case prompts AND the output images in `awesome-gpt-image-2-prompts-main/images/`. Note the prompt vocabulary, level of physical detail, and structure.
3. **Bridge VPipe dimensions to prompt terms**:

| VPipe Dimension | Prompt Equivalent |
|----------------|-------------------|
| `lighting` | Light source, direction, color temp, film stock, flash/no flash |
| `camera` | Shot size, lens (35mm/85mm/etc.), angle, depth of field |
| `blocking` | Spatial arrangement, foreground/midground/background elements |
| `performance` | Pose, expression, gaze direction, body position |
| `style_notes` | Color palette, texture, atmosphere, film grain, negative prompts |
| `character` (from bible) | Face structure, hair, body type, costume, signature prop |

4. **Embed visual fingerprints** — every character/scene prompt must include the compact fingerprint fragment from `bible/fingerprints/<asset_id>.prompt.txt`.
5. **Add negative prompts** — based on the visual bible anti-patterns and the shot's `style_notes`.
6. **Write the prompt file** — save to `prompts/<shot_id>_image_prompt.md`:
   ```markdown
   # Image Prompt: <shot_id>
   ## Reference Cases
   - <case_link> — adopted <what specifically>
   ## Prompt
   <the prompt text>
   ## Negative Prompt
   <negative constraints>
   ## Visual Anchors Embedded
   - <fingerprint references used>
   ```

## Rules

- The camera decision must serve the beat, not decorate the shot.
- Every repeated character must cite a character bible or fingerprint.
- Every repeated scene must cite a scene bible.
- Every cut should have an intended handoff: action, emotion, sound, gaze, object, or contrast.
- Do not generate videos from a shot until `video-continuity-review` has passed.
- Never write a prompt from scratch when matching library cases exist — study and adapt.
- Prompt vocabulary must be concrete (film stock, lens, light direction, fabric, pose) — not abstract adjectives.

