---
name: gpt-image-prompt-patterns
description: Proven GPT image generation prompt patterns distilled from 312 curated cases. Use when writing prompts for photorealism portraits, cinematic interiors, Chinese aesthetic posters, character design sheets, or when the image quality needs to meet professional film production standards.
---

# GPT Image Prompt Patterns

> Source: awesome-gpt-image-2-prompts (312 cases) by EvoLinkAI

## Core Principle

**Concrete > Abstract.** Describe film stock, lens type, light source direction, fabric texture, skin pore detail, color temperature in Kelvin — not "beautiful" or "cinematic."

## Category Patterns

### 1. Photorealism Portrait (source: portrait/case1,3,4,5)

**Template:**
```
35mm film photography, [LIGHT SOURCE detail], authentic film grain,
[SUBJECT: age/face/hair/clothing — concrete physical details],
[POSE: body position, hand placement, gaze direction],
[BACKGROUND: depth of field, environment context],
no plastic skin, no digital over-sharpening, no airbrushing,
no watermark, no text
```

**Key vocabulary:**
- Openings: `35mm film photography` / `documentary naturalism` / `photorealism`
- Light: `natural diffused window light ~5500K, no fill` / `harsh direct flash, specular highlights`
- Skin: `visible subtle skin texture and micro pores` / `natural dewy glow` / `fine delicate lines`
- Negative: `no plastic skin, no digital over-sharpening, no airbrushing, no theatrical expression`

### 2. Cinematic Interior (source: poster/case1,4; portrait interior shots)

**Template:**
```
[ASPECT RATIO], photorealism, cinematic still frame,
35mm Kodak film stock, subtle film grain, anamorphic lens edge falloff.
Camera: [HEIGHT/ANGLE], [LENS], [MOVEMENT].
[LIGHT: source/direction/color temp/falloff].
[SPACE: layout/materials/wear/atmosphere].
Color palette: [DOMINANT + ACCENTS]. [TIME OF DAY] atmosphere.
No people. No [CULTURAL RED FLAGS].
```

**Key vocabulary:**
- Camera: `seated eye level ~90cm` / `50mm natural perspective` / `fixed tripod, no movement`
- Light: `ONLY light source` / `natural falloff: bright near window, fading to shadow` / `dust motes in beam`
- Space wear: `worn footpath on brick floor` / `patched walls from different decades` / `polished smooth from decades of hands`

### 3. Chinese Aesthetic (source: poster/case3 成都美食地图, case4 极简新中式)

**Template:**
```
极简新中式美学风格, [PAPER/SILK texture base],
[S-shaped/flowing COMPOSITION],
[INK WASH or WATERCOLOR technique],
[WARM COLOR dominance: 辣椒红/姜黄/翠绿],
手绘感, [NEGATIVE SPACE], 图片比例 1:1
```

### 4. Character Design Sheet (source: character/case2,3,5)

**Template:**
```
Character reference sheet for film production.
THREE VIEWS: front / side (profile) / back.
Full body standing, [AGE/GENDER/ETHNICITY].
[FACE detail: bone structure, eyes, hair, expression].
[COSTUME detail: fabric, color, cut, wear].
[DETAIL INSETS: face close-up, hands, costume texture].
Clean white/light gray background, even studio lighting.
```

### 5. Negative Prompt (Universal)

```
no Japanese elements (when doing Chinese),
no theatricality, no exaggerated expressions,
no plastic skin, no airbrushing, no digital over-sharpening,
no AI gibberish text, no alien scripts,
no floating objects, no missing contact shadows,
no brand new surfaces (everything has wear),
no watermark, no text overlays, no music visualization
```

## Quality Checklist (Before Generating)

- [ ] Light source explicitly stated (direction + color temp in K)
- [ ] Camera position/lens specified (not just "wide" or "close")
- [ ] Materials have wear descriptors (scratched/worn/patched/faded)
- [ ] Skin has texture description (pores/lines/natural)
- [ ] Negative prompt includes: no plastic skin, no theatricality, no AI text
- [ ] Cultural context correct (Chinese ≠ Japanese, era-appropriate)
- [ ] Text expectations managed (AI text will likely be garbled — note if post-production needed)
