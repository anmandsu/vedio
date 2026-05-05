# AI影视项目可复用工作流

## 管线总览

```
剧本消化 → 参考研究(OpenCLI+女娲蒸馏) → 剧组简报 → 视觉圣经 → 分镜规划
→ 连续性审查 → 场景+角色参考图(母版+三视图) → 光变(图生图) → 道具 → 分镜图片
```

## 图像生成四层审查

```
生成 → Opus-4-6初评(带剧本上下文) → 剧组审查(摄影/美术/导演,逐条checklist) → 人把控 → 用户终审
```

### 每层职责
| 层 | 查什么 |
|----|--------|
| Opus | 基础技术(曝光/白平衡/色温/光逻辑) + AI特有问题(文字/手/空间/皮肤) + 剧本匹配度 |
| 摄影 | 机位/焦段/光线/构图/电影质感 |
| 美术 | 空间一致性/道具状态/色彩体系/使用痕迹/文字 |
| 导演 | 情绪节拍/光线时间/人物状态/叙事服务 |
| 人 | 综合判断,确认低级失误已拦截 |
| 用户 | 最终审美和创作方向 |

## 角色设计流程
1. 先出三视图设计稿(front/side/back + 面容/手部/服装 detail insets)
2. Opus带剧本上下文审查(年龄/面容/体态/服装/手/一致性)
3. 逐项修,每次只修FAIL项,保留PASS项
4. 通过后锁定为母版

## 场景设计流程
1. 先出母版(text-to-image,最完整prompt,标注"MASTER REFERENCE")
2. Opus+剧组审查
3. 光变体全部图生图(img2img --ref=母版URL,只改光线)
4. 各变体独立审查

## AI生图常见坑
- 年龄偏老→写"皮肤仍紧致,70%黑发"
- 手缺茧→写"thumb calluses, needle prick scars"
- 发饰颜色→写"matte black metal, NOT wood/brown/gold"
- 全图偏黄→写"natural white balance, NOT yellow cast"
- 文字乱码→标注"AI text limitation, post-production composite"
- 死黑→写"shadow detail visible, no crushed blacks"
- 左暗右亮≠半白天半黑夜→ dusk物理上东窗本就暗于西窗

## 工具链(项目无关,通用)
- `gen_api.py`: image/video/batch, 支持--ar --quality --ref --output
- `vision_analyze.py`: 通用识图审查, --review=ROLE --context=SHOT_ID
- `picui_upload.py`: 图床上传供审查
- 通用prompt模板: `.claude/skills/gpt-image-prompt-patterns/SKILL.md`
