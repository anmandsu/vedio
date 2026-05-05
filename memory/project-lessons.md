# 针锋·针心 项目记忆

## 项目信息
- 启动: 2026-05-02
- 类型: AI微短剧,3集,蜀绣非遗传承
- 导演锚点: 是枝裕和(静态凝视/沉默叙事/物件载情)
- 识图模型: claude-opus-4-6 (via linkapi.org)
- 生图模型: gpt-image-2 (via linkapi.org, quality=high)
- 图床: picui.cn

## 已锁定资产 (15张)
- 5个角色三视图 + 绣坊母版 + 3光变 + 2场景 + 4道具
- 绣坊母版URL: https://oss.filenest.top/uploads/58fb61a0-1149-4260-97ad-72ca64c6e2c4.png

## 关键教训

### 图像生成
1. 图生图保一致性: 先出母版(text-to-image),变体全部img2img --ref=母版URL
2. 审查必须带上下文: --context=SHOT_ID 加载VPipe数据
3. 年龄控制: AI偏老,需显式写"70%黑发30%灰白"而非"灰白",写"皮肤仍有弹性"而非"皱纹"
4. 手部茧痕: 需要明确描述"thumb and index finger calluses, needle prick scars"才出现
5. 发夹颜色: "plain black"不够,需写"matte black metal, NOT wood, NOT brown, NOT ornamental"
6. 光线: 色温具体到K值,光源方向明确(左窗/右窗),光比1:2-1:3

### 审查流程
7. Opus初评→剧组(摄影/美术/导演)审→人把控→用户终审
8. 审查要有逐条checklist,不能笼统
9. 文字检查是AI图像首要审查项(中文笔画/乱码/镜像)
10. 曝光和白平衡必须在审查清单前列

### 工具链
11. gen_api.py: /v1/images/generations (gpt-image-2), aspect_ratio, quality=high
12. vision_analyze.py: 通用识图审查,支持--review=cinematographer|production-designer|director|all, --context=SHOT_ID
13. picui_upload.py: 图床上传供审查
