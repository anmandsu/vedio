# Continuity Review: VPipe v2

> "Will this cut feel like it belongs in the same film?"
> Reviewed: 2026-05-02 | 14 shots, 9 layers

## Blocking Issues

| # | Shot Pair | Layer | Problem | Fix |
|---|-----------|-------|---------|-----|
| — | — | — | **0 blocking issues found** | — |

## Warnings

| # | Shot Pair | Layer | Problem | Fix |
|---|-----------|-------|---------|-----|
| 1 | E1_S01→S02 | Screen Direction | 林素琴面朝左窗(绣架方向),绣儿从右门入。门在画面哪个方向？没有在 shot 中固定。当前 S01 camera 说"绣架左侧",但门的位置需要确保从 S02 能看到绣儿从哪个方向进入 | 明确门在画面右侧(南向)。林素琴绣架面朝左窗(东),门在右(南)。绣儿永远从右入画。全片锁定此空间关系 |
| 2 | E1_S06 | Character | 外婆是闪回初次登场。face structure 描述为"与林素琴相似(颧骨/鼻梁/盘发)",但无定量锚点。跨镜头 drift 风险高 | 生成外婆时,先出林素琴的 reference frame,再用"same face structure, 20 years older, softer expression"作 prompt。frame-linking 从林素琴→外婆 |
| 3 | E1_S08 | AI生成 | AIGC动画段为纯AI生成,6段流动画面之间无硬性 continuity anchor。风格跳跃风险高 | 锁定一个 visual style master prompt 贯穿全部6段。每段开始前用前一段最后一帧作 reference frame。统一 color palette: warm earth→golden red→cool blue→warm gold |
| 4 | E1_S09 | Space | 针散落地面后→S10清晨"针已捡回"。中间没有任何镜头交代谁捡的、什么时候捡的。观众可能困惑 | 在 S10 开场说明: 针盒已放回绣架旁桌,针整齐插回针插。不需拍捡针过程——"已经恢复了"就是叙事 |
| 5 | E1_S12 | Performance | 小女孩是"轮廓""象征",但跨镜头时她如果有任何正面,就需要 identity lock。description 只说"逆光剪影"——但如果 next project phase 需要她正面呢？ | 当前阶段保持轮廓即可。如果后续需要正面,须先建 identity lock。阶段标记: 暂不需要 |

## Strong Connections (worth preserving)

| Shot Pair | Layer | What Works |
|-----------|-------|------------|
| E1_S01↔S11 | Visual callback | 场1(针歪)↔场10(针稳)。同机位同角度同构图——全片最精心设计的视觉回文 |
| E1_S03→S04 | Emotion | 巴掌爆点→独坐空寂。从9/10强度骤降到5/10。正是是枝裕和式"灾难后的真空" |
| E1_S04→S05 | Sound bridge | 冷窗外风声混入台灯低频嗡鸣——"从孤独过渡到私密"的声学信号。灯光色温同时从6000K→2800K |
| E1_S05→S06 | Sound bridge (J-cut) | 外婆针线声提前0.5s进入闪回——全片最精妙的声桥设计。记忆在声音中"预先浮现" |
| E1_S06→S07 | Sound bridge | 外婆针线声变远变冷→被屏幕电流声覆盖。"被技术切断的记忆"的声音叙事 |
| E1_S08→S09 | Sound bridge | AIGC风声延续→被针盒掉地的"叮"切断。"被一声惊醒"——声音先于画面发生情感转折 |
| E1_S02→S03 | Light arc | 同场(傍晚)内光线持续褪去。林素琴从暖光中站起移入阴影——"温暖离开她"的视觉化 |
| E1_S09→S10 | Light arc | 崩溃夜→清晨天光。光线从冷暖混合(撕裂)回归统一(新生)。声桥:哭声→清晨空气 |
| E1_S01→S02 | Time code | 清晨→傍晚。光色从冷灰→暖金。拆牌通知(新道具)交代时间压力 |
| E1_S14 | Ending | 三段跳切模拟拉远→人群剪影→灯亮→字幕。不闭合但完整。是枝裕和式"生活在继续" |

## 9-Layer Continuity Map

### 1. Story Continuity — PASS with notes

观众能清晰跟踪: 日常裂痕(S01)→外部压力+冲突(S02-03)→独处空洞(S04)→记忆浮现(S05-06)→技术介入(S07-08)→崩溃+觉醒(S09)→新生+传播(S10-12)→生活继续(S13-14)。**无故事断层**。

### 2. Action Continuity — PASS

所有多人场景采用交叉剪辑单人镜头——无跨镜动作衔接需求。单人场景中动作在一个镜头内完成(如场1:五个子镜但都是同一空间内的静态观察)。**无动作断裂风险**。

### 3. Emotion Continuity — PASS

情绪曲线: 3→9→5→4→2→4→6→8→3→5→4→3→2。高峰在 S03(巴掌)和 S09(崩溃),低谷在 S04(独坐)和 S06(闪回)。曲线有充足呼吸空间。是枝裕和式:爆点之间留白够长。

### 4. Spatial Continuity — PASS with WARNING #1

绣坊空间关系: 绣架中央偏左,左窗(东),右窗(西),木牌后墙正中,门在右侧(南),丝线架北墙。所有14镜在此空间内。**需锁定:门在画面右侧,绣儿/小伟永远从右入画**(Warning #1)。

### 5. Screen Direction — PASS with WARNING #1

全片固定机位为主——无复杂方向变化。唯一点: 场13结尾,林素琴/绣儿/小伟三人"面朝右窗"(西,夕阳方向)——首次方向统一。之前林素琴面朝左窗(东)。方向变化=内心变化。**需确保左右在跨镜时一致**(Warning #1)。

### 6. Character Continuity — PASS with WARNING #2

核心anchor: 林素琴耳垂小洞(S01/S03/S09共3次)、绣儿右脸红印(S03→S05→S10褪)、小伟眼镜+电脑包(全片)。外婆初次登场需frame-linking(Warning #2)。

### 7. Scene Continuity — PASS

光线时间弧线完整: 清晨冷灰→傍晚暖金→夜冷蓝→深夜暖黄→油灯暖金(闪回)→深夜冷暖混合→清晨天光→傍晚暖金→夜暖黄。**每场光线色温与时间严格对应,无跳跃**。

### 8. Sound Continuity — PASS (最强层)

全部13对相邻镜有明确声桥标注。针线声心率表贯穿全片: 稳→停→缺席→外婆→缺席→变形→散落→回归→变形→延续。三沉默节点(S03后/S05后/S12后)均标注≥5秒。

### 9. Rhythm — PASS with notes

时长分配: 15/12/35/12/14/8/8/25/30/10/12/10/12/10 = 共约213秒(3.5分钟)。高峰(S03=35s, S09=30s)获最长时长,过渡场(S06=8s, S07=8s)极短。节奏符合是枝裕和"步行速度,遇爆点不加速"原则。Lint警告的5个"long duration"镜头(S01/S03/S05/S08/S09)均有内部子镜拆分——每个子镜≤5秒(AI边界),总时长合理。

## AI一致性专项检查

| 风险 | 镜头 | 策略 | 状态 |
|------|------|------|------|
| 林素琴跨镜身份漂移 | 全片 | 统一 identity lock phrase + 多角度参考图 | 就绪 |
| 绣儿红印褪色速度 | S03→S05→S10 | S05"可见", S10"已褪" | 需两次生成验证 |
| 外婆与林素琴面部遗传 | S06(外婆)+全片(林素琴) | frame-linking从林素琴→外婆: age +20yr, softer | 待生成时执行 |
| 针的状态连续性 | S01→S03→S09→S11 | 稳→扎穿→散落→稳。同针盒/同针型。 | 就绪 |
| 绣坊空间跨镜一致性 | 全片 | 统一 spatial map + 同 reference frame | 就绪 |
| 福袋外观跨镜 | S05→S09→S11 | 暗红绸缎/边缘磨损 | 就绪 |
| 木牌外观跨镜 | 全片 | 60×40cm/阴刻"蜀绣"/包浆 | 就绪 |
| 光线色温连续性 | 全片 | 逐镜标注色温,与叙事时间对应 | 就绪 |

## Suggested Rewrites

**无结构性重写需求。** 14镜框架完整,9层连续性全部检查通过。仅3条Warnings需在生成阶段执行,无需修改YAML:

1. 锁定门在画面右侧,绣儿/小伟从右入画(S01→S02→S03)
2. 外婆生成时用林素琴 reference frame + frame-linking
3. S10开场明确"针已捡回,针盒整齐"

---

**结论: 连续性审查通过。进入Prompt Writing阶段。**
