---
name: video-continuity-review
description: Review AI-video shot lists, nine-grid storyboards, generated images, or clips for continuity. Use to check whether shots connect in story logic, action, emotion, space, screen direction, character identity, wardrobe, props, lighting, sound, and editing rhythm.
---

# Video Continuity Review

## Goal

Answer the production question: "Will this cut feel like it belongs in the same film?"

## Inputs

- VPipe YAML in `shots/` or root.
- Nine-grid plans in `boards/`.
- Visual bibles and fingerprints.
- Generated images/clips if available.

## Review Layers

Check in this order:

1. Story continuity: does the audience understand why the next shot follows?
2. Action continuity: does movement direction and body position connect?
3. Emotion continuity: does emotional intensity rise, fall, or hold intentionally?
4. Spatial continuity: is geography understandable?
5. Screen direction and gaze: are left/right and eyelines coherent?
6. Character continuity: face, wardrobe, prop, injury, posture, age, identity.
7. Scene continuity: light, time, set dressing, weather, damage state.
8. Sound continuity: sound bridge, silence, music, impact peaks.
9. Rhythm: shot duration, beat density, contrast, breath.

## Output

Write `reviews/continuity_<date_or_version>.md`:

```markdown
# Continuity Review

## Blocking Issues
| Shot Pair | Layer | Problem | Fix |
|---|---|---|---|

## Warnings

## Strong Connections

## Suggested Rewrites
```

## CLI Assist

Run `.claude/scripts/continuity_lint.py <vpipe.yaml>` for a structural pass. Treat it as a lint pass only; the real review is cinematic judgment.

## Rules

- Do not reduce continuity to "same character looks similar." Emotional and spatial continuity matter just as much.
- When flagging a problem, propose a concrete fix: insert reaction shot, change screen direction, add sound bridge, adjust duration, or rewrite blocking.
- Separate intentional discontinuity from accidental discontinuity.

