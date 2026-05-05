---
name: video-memory-evolution
description: Distill feedback and project results into evolving AI-video memory. Use after user feedback, accepted images/clips, failed generations, continuity reviews, prompt experiments, or repeated preferences to update project memory and promote stable rules.
---

# Video Memory Evolution

## Goal

Make the system improve without pretending the model itself learned. Persistent memory is files, rules, prompt formulas, source registers, and accepted visual assets.

## Memory Levels

1. **Shot memory**: specific prompt/result notes for one shot.
2. **Project memory**: rules for one film or episode.
3. **User memory**: user taste and language translation.
4. **Global craft memory**: durable film/video workflow rules.

Never promote a local preference directly to global memory.

## Promotion Rule

- 1 occurrence: log as observation.
- 2 occurrences: mark as candidate.
- 3 occurrences across similar contexts: propose promotion.
- User confirmation required before global promotion.

## Files

Update:

- `projects/<id>/memory/project-lessons.md`
- `projects/<id>/memory/prompt-formulas.md`
- `projects/<id>/memory/failed-patterns.md`
- `memory/user-aesthetic.md`
- `memory/global-lessons.md`
- `memory/source-register.md`

## Feedback Capture Format

```markdown
## <date> | <project> | <asset_or_shot>

- User said:
- System changed:
- Result:
- Lesson:
- Scope: shot / project / user / global-candidate
- Evidence count:
- Promote? no / candidate / requires user confirmation
```

## Rules

- Record why the user chose an output, not just which output they chose.
- Record rejected directions so future sessions do not repeat them.
- Keep aesthetic memory descriptive and operational: "lower saturation, softer window light" is better than "more premium."
- Source-derived craft rules must cite the source register.

