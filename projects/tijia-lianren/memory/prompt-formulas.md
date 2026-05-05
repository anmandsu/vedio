# Prompt Formulas

## 2026-05-05 | Identity-Preserve Character Variant

Use when a recurring character needs a new state, outfit, pose, or three-view asset.

### Formula

1. Save the accepted master image under `renders/images/`.
2. Create a face crop under `bible/fingerprints/`.
3. Open the face crop with Codex vision before generation.
4. If needed, open a body/pose reference as a second image.
5. Prompt with explicit reference priority:
   - Image 1: primary identity reference
   - Image 2: body/pose/framing reference only
6. Generate one state per image.
7. Crop face and compare against the master anchor before accepting.
8. Assemble boards locally only after single states pass review.

### Prompt Skeleton

```text
Use the previously displayed local images as references.

Input image roles:
- Image 1: close-up face crop — PRIMARY identity reference.
- Image 2: full-body pose image — body pose, framing, suit, and lighting reference only.

Reference priority:
1. Face identity from Image 1 overrides everything.
2. Body pose and framing from Image 2.
3. Style polish comes last.

Preserve the exact face: brow spacing, eye shape, eye distance, nose bridge, mouth shape, cheekbone line, jaw angle, chin width, ears, hairline, and hairstyle.

Negative: no face redesign, no different actor, no younger idol face, no rounder face, no longer narrower face, no changed mouth, no changed jaw, no multi-panel layout.
```

### Current Best Example

- Prompt: `prompts/lu-zhichen_dual_reference_face_anchor_v5.md`
- Output: `renders/images/_CHAR_lu_zhichen_dual_reference_face_anchor_v5_candidate.png`
- Face compare: `reviews/lu_zhichen_identity_ref_v5_face_compare.png`
