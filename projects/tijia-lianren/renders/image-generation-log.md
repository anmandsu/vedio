# Image Generation Log

## 2026-05-05: Master Candidate v0

Generation tool: image-2 via Codex native image generation.

| Asset | Prompt File | Output |
|---|---|---|
| 沈婉秋 master candidate v0 | `prompts/shen-wanqiu_master_image_prompt.md` | `renders/images/_MASTER_shen_wanqiu_candidate_v0.png` |
| 陆之琛 master candidate v0 | `prompts/lu-zhichen_master_image_prompt.md` | `renders/images/_MASTER_lu_zhichen_candidate_v0.png` |
| EP01 wedding entrance master candidate v0 | `prompts/ep01_wedding_entrance_master_image_prompt.md` | `renders/images/_MASTER_ep01_wedding_entrance_candidate_v0.png` |

## Next Review

- Review against `bible/characters/shen-wanqiu.md`, `bible/characters/lu-zhichen.md`, `bible/scenes/ep01-wedding-entrance.md`, and `research/visual-observations.md`.
- If accepted or only minor warnings, extract visual fingerprints into `bible/fingerprints/`.
- If blocked, revise prompt and regenerate v1.

## 2026-05-05: Korean Premium Character Sheets v1

Generation tool: image-2 via Codex native image generation.

| Asset | Prompt File | Output |
|---|---|---|
| 沈婉秋 three-view Korean v1 | `prompts/shen-wanqiu_three_view_korean_v1.md` | `renders/images/_CHAR_shen_wanqiu_three_view_korean_v1.png` |
| 沈婉秋 state board Korean v1 | `prompts/shen-wanqiu_states_korean_v1.md` | `renders/images/_CHAR_shen_wanqiu_states_korean_v1.png` |
| 陆之琛 three-view Korean v1 | `prompts/lu-zhichen_three_view_korean_v1.md` | `renders/images/_CHAR_lu_zhichen_three_view_korean_v1.png` |
| 陆之琛 state board Korean v1 | `prompts/lu-zhichen_states_korean_v1.md` | `renders/images/_CHAR_lu_zhichen_states_korean_v1.png` |

## 2026-05-05: 陆之琛 Liu Xiaoxu Direction v2

Generation tool: image-2 via Codex native image generation.

User direction: 男主形象可以像短剧男主刘萧旭. Interpreted as temperament and feature direction, not exact celebrity likeness.

| Asset | Prompt File | Output |
|---|---|---|
| 陆之琛 three-view Liu Xiaoxu direction v2 | `prompts/lu-zhichen_three_view_liuxiaoxu_direction_v2.md` | `renders/images/_CHAR_lu_zhichen_three_view_liuxiaoxu_direction_v2.png` |
| 陆之琛 state board Liu Xiaoxu direction v2 | `prompts/lu-zhichen_states_liuxiaoxu_direction_v2.md` | `renders/images/_CHAR_lu_zhichen_states_liuxiaoxu_direction_v2.png` |

## 2026-05-05: 陆之琛 Identity-Reference v3-v5

Generation tool: image-2 via Codex native image generation with local images opened as references through Codex vision.

User feedback: text-only state boards and three-view boards caused face drift. New method: master image → face crop → local reference generation → face crop comparison.

| Asset | Prompt File | Output |
|---|---|---|
| 陆之琛 identity-reference formal state v3 | `prompts/lu-zhichen_identity_ref_single_state_v3.md` | `renders/images/_CHAR_lu_zhichen_identity_ref_formal_state_v3_candidate.png` |
| 陆之琛 full-body extension v4 | `prompts/lu-zhichen_identity_ref_full_body_extension_v4.md` | `renders/images/_CHAR_lu_zhichen_identity_ref_full_body_extension_v4_candidate.png` |
| 陆之琛 dual-reference face anchor v5 | `prompts/lu-zhichen_dual_reference_face_anchor_v5.md` | `renders/images/_CHAR_lu_zhichen_dual_reference_face_anchor_v5_candidate.png` |

Review artifacts:

- `reviews/lu_zhichen_identity_ref_v3_face_compare.png`
- `reviews/lu_zhichen_identity_ref_v4_face_compare.png`
- `reviews/lu_zhichen_identity_ref_v5_face_compare.png`
- `reviews/lu_zhichen_v5_visual_review.md`
