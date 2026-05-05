# Project Lessons

## 2026-05-05 | tijia-lianren | character boards

- User said: 状态图和三视图没有人物一致性，脸有变化，需要图生图。
- System changed: Use saved local master images as identity references through Codex vision before generating recurring character variants.
- Result: Text-only multi-panel boards are marked as non-final continuity assets; future character variants must be single-state identity-reference generations.
- Lesson: For recurring short-drama leads, generate one state per image from an accepted anchor, review it, then assemble boards locally.
- Scope: project
- Evidence count: 1
- Promote? no

## 2026-05-05 | tijia-lianren | local-reference image generation

- User said: 可以把生成图保存到本地再截屏给自己参考就实现图生图。
- System changed: Codex now treats project-local images opened through vision as reference inputs for native image generation.
- Result: 陆之琛 v3/v4/v5 were generated from saved local anchor images; v5 was accepted as good enough for current progress.
- Lesson: The reliable Codex-native workaround is `save image locally → view_image/open it → generate with explicit reference roles → copy result into project → crop/compare face`.
- Scope: project
- Evidence count: 1
- Promote? candidate
