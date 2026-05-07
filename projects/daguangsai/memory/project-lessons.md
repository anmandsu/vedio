# Project Lessons

## Scene Image Generation (2026-05-03)

### Lesson 1: 氛围参考图是必需的，不是可选的

**问题**: 生成同场景不同时间的图时，只用文字描述lighting变化，结果要么太dramatic（末日感），要么太flat（无氛围感）。

**原因**: AI模型对"golden hour"等词有强烈的cinematic bias，无法从文字描述中理解"克制的氛围感"。

**解决方案**: 
- 搜索真实世界的氛围参考图（Pexels, 小红书, Pinterest等）
- 将氛围参考图作为img2img的第二个reference输入
- 不能只在prompt中描述，必须用图片anchor aesthetic

### Lesson 2: 双参考图img2img工作流

生成同场景不同时间的图时：

```bash
# 1. 上传空间布局参考（保持空间一致）
PICUI_API_TOKEN="<token>" python .claude/scripts/picui_upload.py upload SC01.png --public

# 2. 上传氛围参考图（anchor aesthetic）
PICUI_API_TOKEN="<token>" python .claude/scripts/picui_upload.py upload atmosphere_ref.jpg --public

# 3. 使用双参考生成
LINKAPI_KEY="<key>" python .claude/scripts/gen_api.py image \
  "Same space as first reference. Change only: <time> lighting. Match atmosphere of second reference." \
  --ref="<spatial_ref_url>" \
  --ref="<atmosphere_ref_url>" \
  --output=output.json
```

### Lesson 3: 用具体参考表达想要的感觉

**表达越清晰越好**。可以用：

1. **电影参考**: "像《XXX》电影里的XX场景的光线感觉"
2. **导演风格**: "王家卫式的暖色调", "侯孝贤式的自然光"
3. **清晰的情绪描述**: "明媚的黄昏", "温柔的傍晚", "宁静的清晨"
4. **具体的视觉特征**: "3500K奶油色温", "3:1柔和光比", "透明的阴影"

**避免模糊的形容词**: "好看的", "有感觉的", "氛围感" - 这些词AI无法理解。

### Lesson 4: "克制"不等于"平淡"

**错误理解**: 克制 = documentary flat lighting = 无氛围感

**正确理解**: 克制 = 在"有氛围"和"过度戏剧化"之间找平衡点

- 要有氛围感（温暖、柔和、nostalgic）
- 但不要过度戏剧化（末日感、cinematic、theatrical）
- 用氛围参考图anchor这个平衡点

### Lesson 5: SC02生成完整案例分析（2026-05-03）

**问题根源**: AI模型对lighting有系统性bias，倾向生成过大光比和过度戏剧化效果。

**尝试历程**:

| 版本 | 方法 | 结果 | 问题 |
|------|------|------|------|
| v8/v9/v10 | 单参考img2img，文字描述"golden hour" | ❌ | 光比8:1-10:1，色温2700-3000K太橙，太dramatic像末日 |
| v11 | 单参考img2img，"overcast evening"避免dramatic | ⚠️ | 光比2.5-3:1达标，但失去氛围感，太flat |
| v12 | **双参考img2img**（spatial + atmosphere） | ⚠️ | 氛围对了，但场景主体变了（不是绣坊） |
| v13 | 双参考img2img，强调保持绣坊内容 | ❌ | 场景对了，但光比大、亮部太黄、不通透、光太硬 |
| v14 | 双参考img2img，多光源soft diffused，降色温 | ✅ | **效果最好**：通透、柔和、有氛围、克制 |
| v15 | v14基础上修正21:9比例 | ❌ | 太柔了，失去阴影方向性和立体感 |

**最终方案（v14）**:
- 双参考img2img（spatial + atmosphere）
- 多光源描述：主光（窗户soft diffused）+ 填充光（环境反射）+ 天空光（冷色调）
- 色温：亮部3200-3300K，暗部3500-3600K
- 光比：2.5:1-3:1（但实际生成可能还是偏大）
- 强调：HIGH KEY illumination, bright airy transparent
- 强调：SOFT DIFFUSED NOT hard direct sun
- 强调：SOFT EDGES gradual falloff（但不要过度，要保持阴影方向性）

**关键教训**:

1. **AI模型系统性问题**：所有生成的图光比都偏大，需要在prompt中**过度强调小光比**（说2:1才能得到3:1）

2. **平衡的艺术**：
   - 太硬 → 失去柔和感，不通透
   - 太柔 → 失去方向性，没有立体感
   - 正确：柔和但有方向性的阴影

3. **阴影的正确描述**：
   - ✅ "SOFT EDGES gradual falloff" - 柔和边缘
   - ✅ "transparent luminous shadows with detail" - 透明有细节
   - ❌ "NO shadows" - 会失去立体感
   - ❌ "NO geometric shadow edges" - 过度强调会失去方向性

4. **多光源是关键**：
   - 单一光源 → 高光比，dramatic
   - 多光源（主光+填充光+天空光）→ 低光比，通透

5. **色温要克制**：
   - 3400K+ → 太黄
   - 3200-3300K → 温暖但不过分

## 蜀绣工艺研究 (Earlier)

### 针法特征
- 蜀绣以细腻著称，针脚细密
- 常用针法：晕针（渐变色过渡）、纱针（透明效果）、掺针（色彩融合）
- 丝线光泽感强，需要在lighting中体现

### 场景细节
- 传统绣坊：木质绣架、线轴架、布料卷、工具台
- 自然光为主，窗户是主要光源
- lived-in atmosphere：使用痕迹、岁月感、温暖的生活气息
