# Identity Reference Generation Protocol

## Problem Found

Text-only multi-view and multi-state boards caused face drift. The model produced a coherent style sheet, but each panel became a nearby different person.

## New Rule

Use local anchor images as identity references before every recurring character generation:

1. Open the accepted local anchor image with Codex vision.
2. Treat the anchor image as the identity reference, not just style reference.
3. Load the matching `bible/fingerprints/*.prompt.txt` fragment.
4. Generate one state per image.
5. Run visual review against the anchor.
6. Only after approval, assemble approved single-state images into three-view or state boards.

## Why

AI image models are much better at preserving one face across one requested transformation than preserving the same face across four independent panels in one prompt.

## Blocking Rule

Do not accept text-only multi-panel character boards as final continuity assets for 陆之琛 or 沈婉秋.
