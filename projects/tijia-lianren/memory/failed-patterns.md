# Failed Patterns

## 2026-05-05 | Text-Only Multi-Panel Character Boards

### What Failed

Text-only three-view and four-state boards produced consistent styling but inconsistent identity. Each panel became a nearby different person.

### Evidence

- `renders/images/_CHAR_lu_zhichen_states_liuxiaoxu_direction_v2.png`
- `renders/images/_CHAR_shen_wanqiu_states_korean_v1.png`

### Do Not Repeat

- Do not ask the image model to invent four states of the same person in one image as a final continuity asset.
- Do not rely on celebrity-style verbal direction to preserve identity.
- Do not accept a visually pretty board unless the face passes crop comparison.

### Replacement

Use local anchor image generation:

- master image → face crop → single-state generation → visual review → local board assembly
