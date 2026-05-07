# SC02 Generation Final Report

## Final Version: SC02_v20 ✅

**File**: `projects/daguangsai/renders/scenes/SC02_v20.png`
**Status**: APPROVED
**Date**: 2026-05-03

### Final Specifications
- **Scene**: 老绣坊·傍晚黄昏 (Traditional Shu embroidery workshop, evening golden hour)
- **Method**: Dual-reference img2img (spatial + atmosphere)
- **Color Temperature**: 3800K warm neutral
- **Lighting**: Soft diffused multi-source (window + ambient bounce + sky light)
- **Atmosphere**: Warm nostalgic restrained natural
- **Aspect Ratio**: Attempted 21:9 (may still be ~16:9 due to img2img limitation)

### Key Success Factors
1. **Dual-reference img2img**: SC01_v7.png (spatial) + atmosphere_ref_30173137.jpg (aesthetic)
2. **Correct color temperature**: 3800K (not 3200-3300K which was too warm/yellow)
3. **No explicit lighting ratio**: Let AI handle naturally instead of over-constraining
4. **Soft diffused multi-source lighting**: Avoided single hard light source
5. **Detailed scene description**: Explicitly listed embroidery workshop features to prevent scene drift

## Generation History Summary

**Total attempts**: 20 versions (v8-v20, excluding v1-v7 which were earlier experiments)

### Phase 1: Single-reference failures (v8-v11)
- **Problem**: Text descriptions alone couldn't balance "atmospheric" and "restrained"
- **v8-v10**: Too dramatic, cinematic, apocalyptic (8:1-10:1 ratio, 2700-3000K)
- **v11**: Achieved lighting ratio but lost atmosphere (too flat)

### Phase 2: Dual-reference breakthrough (v12-v13)
- **v12**: First use of dual-reference img2img - atmosphere SUCCESS but scene changed to industrial/cafe
- **v13**: Preserved embroidery workshop but lighting regressed (too hard, too yellow, not transparent)

### Phase 3: Lighting refinement (v14-v17)
- **v14**: BEST EFFECT - soft diffused multi-source, 3200-3300K, transparent, but wrong aspect ratio (16:9)
- **v15**: Corrected to 21:9 but over-softened, lost shadow directionality
- **v16**: Balanced soft + directional shadows, but still 16:9
- **v17**: Over-emphasized HIGH KEY, resulted in overexposure

### Phase 4: Color temperature correction (v18-v20)
- **v18**: Corrected to 3800K, removed explicit lighting ratio constraints, but scene drifted to modern studio
- **v19**: Re-emphasized traditional embroidery workshop features, good atmosphere, but aspect ratio issue persisted
- **v20**: Final version - explicitly stated 21:9 in prompt text, maintained v19's good atmosphere

## Critical Lessons Learned

### 1. Atmosphere References Are Mandatory
- Text descriptions alone produce either too dramatic or too flat results
- Must use atmosphere reference image as img2img input, not just describe in text

### 2. Color Temperature Discovery
- Started at 3500K → too warm
- Tried 3200-3300K → too yellow
- **Final: 3800K** → correct warm neutral tone

### 3. Lighting Ratio Paradox
- AI models systematically generate excessive lighting ratio
- Over-constraining (saying "2:1") doesn't help
- **Solution**: Don't specify ratio, describe multi-source lighting instead

### 4. Soft vs. Directional Balance
- Too hard → loses transparency
- Too soft → loses depth and 3D feeling
- **Correct**: "Directional shadows with soft feathered edges"

### 5. Scene Content Preservation
- Generic descriptions like "embroidery workshop" cause scene drift
- **Must explicitly list**: wooden frames, thread spools, fabric rolls, traditional tools, etc.

### 6. Aspect Ratio Limitation
- img2img preserves reference image aspect ratio
- SC01 is ~16:9 (1717x916), so img2img outputs are also ~16:9
- Stating "21:9" in prompt text may help but not guaranteed
- **Trade-off**: img2img preserves spatial layout but limits aspect ratio control

## Files Generated

### Approved
- `SC02_v20.png` - Final approved version
- `atmosphere_ref_30173137.jpg` - Atmosphere reference from Pexels

### Reference
- `SC01_v7.png` - Spatial reference (1717x916, ~16:9)
- Uploaded to picui: https://free.picui.cn/free/2026/05/03/69f655ed3f36a.png
- Atmosphere ref uploaded: https://free.picui.cn/free/2026/05/03/69f673a0261f9.jpg

### Intermediate Versions (for reference)
- `SC02_v14.png` - Best lighting effect (but 16:9)
- `SC02_v19.png` - Good atmosphere before final adjustments

## Next Steps

Use SC02_v20 as the approved evening golden hour version of the embroidery workshop. For future same-location time variations:

1. Use dual-reference img2img method
2. Search for appropriate atmosphere references first
3. Use 3800K as baseline for warm neutral tones
4. Describe multi-source lighting, don't constrain ratio
5. Explicitly list scene features to prevent drift
6. Accept aspect ratio limitation of img2img (~16:9 from SC01)
