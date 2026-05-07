---
name: video-visual-bible
description: "Create and maintain visual bibles for AI video: character bibles, scene bibles, prop bibles, moodboards, visual fingerprints, reference images, and consistency anchors. Use before image/video generation and whenever recurring visual continuity matters."
---

# Video Visual Bible

## Goal

Lock visual identity before generation. Consistency comes from anchors, reference images, and visual fingerprints, not from adjectives alone.

## Inputs

- `script/scene-map.md`
- `script/emotion-map.md`
- `crew/creative-brief.md`
- User reference images or moodboard links
- Existing generated images or frames

## Outputs

Write under `bible/`:

- `characters/<name>.md`
- `scenes/<scene_id>.md`
- `props/<prop_name>.md`
- `moodboard/INDEX.md`
- `fingerprints/<asset_id>.prompt.txt`
- `fingerprints/<asset_id>.json`

## Character Bible

```markdown
# Character: <Name>

## Script Anchors
Exact quotes or YAML shot anchors.

## Identity Lock
- Age:
- Body / face:
- Hair:
- Costume base:
- Signature prop:
- Behavior:

## Continuity Anchors
Must persist across shots:

## Variation Rules
Allowed changes by scene:

## Anti-Patterns
Never generate:

## Reference Images
| Path/URL | Role | Source | Confidence |
```

## Scene Bible

```markdown
# Scene: <Scene ID>

## Narrative Function

## Spatial Map

## Light And Time

## Color And Materials

## Recurring Props

## Camera-Friendly Anchors

## Sound Bed
```

## Visual Fingerprint Protocol

Claude Code can read images directly via the Read tool (PNG, JPG, etc.). Use this built-in vision capability instead of external vision APIs.

After a key image is accepted:

1. **Read the accepted image** with Claude Code's Read tool — this provides visual understanding directly.
2. **Describe only stable visual facts** — face structure, hair, body type, costume silhouette, color palette, lighting direction, spatial layout. Avoid interpreting mood or quality; stick to observable features that must persist.
3. **Save the full report** to `fingerprints/<asset_id>.json`:
   ```json
   {
     "asset_id": "character_name_or_scene_id",
     "source_image": "path/to/accepted/image.png",
     "review_date": "YYYY-MM-DD",
     "stable_facts": {
       "face_structure": "...",
       "hair": "...",
       "body_type": "...",
       "costume_silhouette": "...",
       "color_palette": "...",
       "signature_prop": "...",
       "lighting_direction": "...",
       "spatial_layout": "..."
     },
     "allowed_variation": "...",
     "known_drift_risks": "..."
   }
   ```
4. **Save a compact generation-ready prompt fragment** to `fingerprints/<asset_id>.prompt.txt`:
   ```text
   Same character identity: <face/body/hair/costume anchors>. Preserve <signature prop>. Avoid <known drift>.
   ```
5. **Future prompts reference both** the compact fragment and the accepted image path as a visual anchor.

### When to use the visual-reviewer agent

For multi-shot consistency checking or batch review of generated images, delegate to the `visual-reviewer` agent. This agent uses Claude Code's vision to:
- Compare a generated image against the visual bible
- Check character/scene/prop consistency
- Flag drift and propose corrections
- Produce structured review reports in `reviews/`

## Rules

- Ask for user confirmation before locking a character or scene bible.
- Keep global user taste in `memory/user-aesthetic.md`; keep project-specific taste in `projects/<id>/memory/`.
- Treat accepted reference images as stronger than verbal style adjectives.
- Claude Code's built-in vision is the primary image analysis tool — no external vision API required.
- For batch or automated review, use the `visual-reviewer` agent.
