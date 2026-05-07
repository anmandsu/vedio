# VPipe Shot Schema

Use this schema for AI-video shot planning. It is compatible with `episode_1_vpipe_v2.yaml`.

## Top Level

```yaml
episode: 1
title: "..."
style: "..."
shots:
  - shot_id: "E1_S01"
```

## Required Shot Fields

```yaml
- shot_id: "E1_S01"
  scene_id: "SC01_LOCATION"
  character: "..."
  location: "INT./EXT. LOCATION - TIME"

  plot: >
    What story information or change this shot carries.

  performance: >
    Actor behavior, micro-expression, physical action, emotional state.

  lighting: >
    Time, direction, color temperature, contrast, motivated light, atmosphere.

  camera: >
    Shot size; angle; movement; lens; stabilization; special camera language.

  blocking: >
    Spatial arrangement, foreground/midground/background, movement paths.

  sound: >
    Environment, music, silence, effects, sound bridge, impact peak.

  dialogue: >
    Dialogue or explicit "no dialogue".

  duration_sec: 5
  beat_type: "establishing"

  style_notes: >
    Non-obvious generation and cinematic constraints.
```

## Recommended Extra Fields

```yaml
  continuity_from: "What must carry over from previous shot"
  continuity_to: "What prepares the next shot"
  visual_anchors:
    - "character fingerprint: ..."
    - "scene anchor: ..."
  negative_prompt: >
    What generation must avoid.
  generation_notes: >
    Tool-specific handoff notes.
```

## Beat Types

Use concrete beat labels:

- establishing
- inciting
- escalation
- reveal
- reaction
- decision
- transition
- action
- disaster
- aftermath
- intimacy
- suspense
- release

## Shot Rule

One shot equals one clear cinematic job. If a shot carries too many jobs, split it.

