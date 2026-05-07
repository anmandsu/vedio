# Prompt Knowledge Base — extracted from awesome-gpt-image-2-prompts (312 cases)

## 1. Photorealism / Documentary Style (本片主力)
Source: portrait/case1,3,4,5 | Use: 人物中景/近景, 写实场景

**Structure**: `[film stock] + [lighting detail] + [subject description] + [texture detail] + [negative constraints]`

**Reusable phrases**:
- `35mm film photography` — 开篇定调
- `authentic film grain, subtle color shift` — 胶片质感
- `natural diffused light, no fill light, deep shadows` — 是枝裕和式自然光
- `documentary naturalism, not glamorized` — 写实基调
- `worn textures on every surface` — 被住过的空间
- `no plastic skin, no digital over-sharpening, no airbrushing` — 皮肤质感标配
- `subtle skin texture and micro pores` — 真实皮肤
- `photorealism` — 写实风格强化词(用户指定)

**Negative prompt 标配**:
```
no theatricality, no exaggerated expressions, no cartoonish emotions,
no plastic skin, no digital over-sharpening, no airbrushing,
no watermark, no text, no music visualization
```

## 2. Chinese Aesthetic / Interior (本片绣坊)
Source: poster/case3(成都美食地图), poster/case4(极简新中式) | Use: 场景空镜/氛围图

**Reusable phrases**:
- `极简新中式美学风格` — 中式克制
- `淡雅的灰白色为底，纸艺剪影般的立体感` — 空间质感
- `手绘感，水彩+彩铅混合` — 非写实时可用
- `画面以鸟瞰视角的手绘简化地图为底` — 空间交代
- `整体画风为水彩+彩铅混合的手绘质感，颜色以暖色系为主` — 中式暖色

**色彩词汇**:
- 暖色系: `warm earth tones, golden red, amber`
- 冷色系: `cool gray, muted blue, teal`
- 中式特有: `辣椒红(#C41E3A), 姜黄, 翠绿, 木褐(#6B3A2E)`
- 墙面: `暖白微黄(#E8E0D5), whitewashed with yellowing`

**材质词汇**:
- `gray brick floor with worn patches` — 老青砖地面
- `dark wooden beams` — 深色木梁
- `whitewashed walls, slightly yellowed` — 老墙
- `bamboo chair with worn seat` — 老竹椅

## 3. Character Portrait (人物)
Source: portrait/case1,3,4,5 | Use: 人物参考图/角色圣经

**亚洲女性面容** (提炼自portrait cases,去除性感化):
- `ultra-realistic natural Chinese features` — 替代 "sexy idol" 等
- `natural double eyelids, defined cheekbones` — 面部结构
- `porcelain skin with warm ivory undertone` — 皮肤色调
- `visible subtle skin texture and micro pores` — 真实皮肤
- `natural makeup-free face` — 素颜
- `hair in a simple low bun, naturally graying` — 中年/老年发型

**年龄描述** (本项目角色):
- 56岁: `thin face, prominent cheekbones, wrinkles at eye corners from decades of close work, graying hair (~40%)`
- 26岁: `young face, natural expression, mid-length hair`
- 24岁: `thin-frame glasses, neutral expression, short clean hair`
- 60岁: `same bone structure as [character], older, softer expression, more wrinkles`

**服装** (中国语境):
- `simple cotton-linen Chinese duijin shirt (中式对襟衫), dark navy, slightly worn cuffs`
- `jeans and simple shirt` — 现代日常
- `gray hoodie, thin-frame glasses` — 理工男

## 4. Lighting Vocabulary (光线)
Source: all portrait/poster cases + Kore-eda cinematography rules

**自然光**:
- `cold gray morning light through window, ~5500K, no fill`
- `warm golden sunset light through west window, ~3200K, fading`
- `cool blue streetlamp glow, single source, ~6000K, deep shadows`
- `warm amber desk lamp, ~2800K, small pool of light, 1.5m diameter`
- `oil lamp, ~2200K, warmest light, steady flame, minimal flicker`
- `dawn light, ~4500K, neutral-warm, new beginning`
- `mixed lighting: warm lamp ~2800K + cool screen glow ~6500K`

**光比与质感**:
- `light ratio 1:2 to 1:3` — 是枝裕和标准
- `natural falloff, bright near window fading to shadow`
- `no fill light, let shadows be shadows`
- `dust motes floating in window beam` — 日常诗意
- `Rembrandt lighting: half face illuminated, half in shadow`

## 5. Camera Vocabulary (摄影)
Source: Kore-eda + cinematography rules

```
fixed camera position, no movement — 固定机位
seated eye level, ~90cm height — 坐姿眼平
50mm lens, natural perspective — 标准焦段
35mm lens, environmental context — 环境焦段
macro lens, 40cm working distance — 微距(针+手)
frame-within-frame composition — 框中框(门框/绣架边缘)
obstructed-view composition — 遮挡构图(透过绣布/丝线)
no push-in during emotional peaks — 情绪高点不推近
```

## 6. AI-Specific Negative Prompt (本片定制)
Source: AI video research + 项目AI边界

```
no Japanese room, no tatami, no shoji, no kimono, no yukata
no qipao, no jewelry, no makeup, no dyed hair (for Lin Suqin)
no theatrical acting, no exaggerated expressions, no crying face
no brand new furniture, no museum-clean surfaces, no IKEA aesthetic
no warm cozy atmosphere when it should be cold
no three-person wide shot (cross-cut single shots instead)
no dramatic lighting, no unmotivated backlight, no Hollywood rim light
no neon lights, no LED signs
no AI-generated text on screens (post-production composite)
no plastic skin, no digital over-sharpening, no airbrushing
no watermark, no text overlays, no music visualization
```

## 7. Aspect Ratio & Format
- `21:9 ultra-wide cinematic aspect ratio` — 本片标准
- `9:16 vertical smartphone` — 手机屏幕UI
- `1:1 square` — 海报/卡片

## 8. Quick Template: Workshop Interior
```
21:9 ultra-wide cinematic. 35mm film photography, photorealism, [TIME] light through [WINDOW] window ~[K]色温. [LIGHTING DETAIL]. Old Chengdu embroidery workshop, [CAMERA POSITION]. Gray brick floor, whitewashed walls, dark beams, wooden sign '蜀绣', silk thread shelves [COLORS]. Embroidery frame center-left, [PROP DETAILS]. Lived-in for three generations — [WEAR DETAILS]. No people. No Japanese elements. Subtle film grain.
```

## 9. Quick Template: Character at Frame
```
21:9 ultra-wide cinematic. 35mm film photography, photorealism, [LIGHT] light ~[K]色温. [CHARACTER DESCRIPTION: age, face, hair, clothing, hands]. Sitting at embroidery frame in old Chengdu workshop. [EXPRESSION DETAIL]. Behind: workshop interior — wooden sign '蜀绣', silk thread wall. No Japanese elements, no qipao, no makeup, no theatrical expression. Subtle film grain, worn textures.
```
