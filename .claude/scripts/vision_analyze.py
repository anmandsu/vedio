#!/usr/bin/env python3
"""Vision analysis tool — analyze images using linkapi.org GPT-4o vision.
Usage:
  python vision_analyze.py <image_url> "<question>"
  python vision_analyze.py <image_url> --review=<role> [--context=<shot_id>]
  python vision_analyze.py <image_url> --review=all [--context=<shot_id>]
"""

from __future__ import annotations
import json, os, sys

BASE_URL = os.environ.get("LINKAPI_BASE_URL", "https://api.linkapi.org")
API_KEY = os.environ.get("LINKAPI_KEY", "")

def _load_shot_context(shot_id: str) -> str:
    """Load VPipe shot data for review context."""
    try:
        import yaml
        yaml_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            '..', 'projects', 'zhenfeng', 'shots', 'episode_1_vpipe.yaml'
        )
        with open(yaml_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        for shot in data.get('shots', []):
            if shot.get('shot_id') == shot_id:
                return f"""
【剧情上下文 - {shot_id}】
场次: {shot.get('scene_id', '')}
地点: {shot.get('location', '')}
人物: {shot.get('character', '')}
故事节拍: {shot.get('plot', '')[:300]}
表演方向: {shot.get('performance', '')[:300]}
光线方案: {shot.get('lighting', '')[:300]}
摄影方案: {shot.get('camera', '')[:300]}
声音方案: {shot.get('sound', '')[:200]}
风格备注: {shot.get('style_notes', '')[:300]}
负向约束: {shot.get('negative_prompt', '')[:200]}
"""
        return f"【{shot_id} 的VPipe数据未找到,请基于通用审查标准】"
    except Exception:
        return "【VPipe数据加载失败,请基于通用审查标准】"

def _make_review_prompt(role: str, shot_ctx: str) -> str:
    base = f"""你是电影级别的{role},正在审查一张AI生成的图片是否符合专业电影制作标准。
{shot_ctx}
请以电影工业标准审查这张图,逐项检查并回答:"""

    prompts = {
        'cinematographer': base + """
【电影摄影技术标准 — 逐项检查,每条必须回答具体发现】

一、基础技术(不合格则直接FAIL):
1. 曝光:直方图是否健康? 高光有没有死白(clipping)? 暗部有没有死黑(crushed blacks)? 还是细节都在?
2. 白平衡:全图有没有偏色? 偏黄? 偏蓝? 偏绿? 还是自然中性?
3. 色温一致性:实际画面光是冷是暖? 和方案要求一致吗?
4. 光源逻辑:光从哪里来? 能追溯到一个合理的光源(窗户/灯)吗? 有没有凭空出现的"无源光"?
5. 动态范围:亮部和暗部之间有平滑过渡吗? 还是突然截断(像手机拍的)?
6. 光比:有没有层次? 还是一团平(像监控画面)?

二、AI特有问题(每项必查):
7. 文字:画面里有没有任何文字/字符? 中文对不对? 笔画对不对? 有没有乱码/外星文/镜像字?
8. 手/肢体:有没有可见的手? 手指数量对吗? 关节弯曲方向对吗? 有没有"融化"的肢体?
9. 空间逻辑:物体都"落"在地面上吗(有接触阴影)? 有没有悬浮物? 透视关系对吗?
10. 皮肤质感:如果有人的皮肤——有没有毛孔/纹理? 还是像塑料/蜡像(over-smoothed)?
11. 边缘:人物/物体的边缘有没有奇怪的光晕(edge halos)?

三、电影质感:
12. 景深:焦点在哪里? 虚化自然吗? 还是全图一样锐(像手机)?
13. 纹理:布料/木头/砖墙——材质纹理对不对? 是自然的还是AI式的重复图案(pattern fractals)?
14. 胶片感:画面有没有有机的颗粒感/自然的边缘衰减? 还是"数字完美"(像CGI/手机)?
15. 整体判断:这个画面放在电影院里——观众会觉得"这是电影"还是"这是AI生成的"?

逐条回答,不允许跳过。最后单独一行写: PASS 或 FAIL (说明最关键的一个原因)""",

        'production-designer': base + """
【电影美术标准 — 逐项检查,每条必须回答具体发现】

一、AI特有问题(每项必查,不合格直接FAIL):
1. 文字检查(必须专门仔细看!):画面里所有文字/字符——门牌/招牌/通知/标签上的字,是正确的中文吗? 笔画对吗? 有没有乱码? 镜像字? 日文? 韩文? AI经常在文字上出错!
2. 空间逻辑:地板/墙面/天花板的关系对吗? 有没有楼梯通到天花板? 桌腿消失在地里?
3. 物体落位:所有物件都"放"在表面上吗? 有接触阴影吗? 有没有悬浮物?
4. 尺度关系:物体之间的比例对吗? 有没有椅子比门还大的?
5. 重复图案:布料/砖墙/地砖——有没有不自然的AI式重复(pattern fractals)?

二、美术质感:
6. 材质:木头是木头质感吗? 布是布质感吗? 砖是砖质感吗? 还是统一的光滑塑料感?
7. 使用痕迹:这个空间有没有人用过的痕迹? 磨损/包浆/修补/灰尘? 还是崭新的"展厅感"?
8. 色彩体系:色彩是有逻辑的(比如木色+白墙+少数艳色点缀)? 还是乱糟糟的各种颜色堆砌?
9. 年代感:这个空间能判断出年代吗? 还是模糊的"任何年代都行"?
10. 风格:能看到明确的风格吗? 还是各种风格的大杂烩?

三、一致性(如和图生图变体):
11. 空间结构和母版一致吗? 门窗/主要家具的位置有没有漂移?
12. 道具外观和母版一致吗? 颜色/纹理/大小?

逐条回答,不允许跳过。最后单独一行写: PASS 或 FAIL (说明最关键的一个原因)""",

        'director': base + """
【导演审查 — 逐项检查,每条必须回答具体发现】

一、电影基础(不合格直接FAIL):
1. 文字检查(最容易被AI搞砸!):画面里每一个中文字——招牌/通知/标签/任何文字——是正确的中文吗? 笔画对了吗? 有没有乱码? 镜像? 日文假名? 这是AI最常见的失败,必须逐字看!
2. AI痕迹:第一眼看——像真实照片吗? 还是能感觉到"这是AI生成的"? 哪里暴露了?
3. 这个画面如果放在大银幕上,观众会出戏吗? 最可能因为什么出戏?

二、画面叙事:
4. 这个画面有"故事"吗? 观众能看到画面后会想知道"发生了什么"或者"接下来呢"吗?
5. 画面里有没有一个明确的视觉焦点? 眼睛第一眼看哪里? 这是故意的吗?
6. 情绪:这个画面传达了什么感受? 安静/紧张/温暖/孤独/空洞/虚假? (不要说"还行",必须说具体感受)
7. 时间感:观众能从画面判断出这是什么时间(清晨/正午/傍晚/深夜)吗?
8. 空间感:这个空间让人想走进去吗? 还是像一个不能进入的画?

三、如果有角色:
9. 这个人是"活着"的还是"在拍照摆pose"? 表情自然吗? 还是僵硬的?
10. 这个人有性格吗? 观众能从画面推断出这个人的职业/年龄/心情吗?

逐条回答,不允许跳过。最后单独一行写: PASS 或 FAIL (说明最关键的一个原因)""",
    }
    return prompts.get(role, base)

def analyze(image_url: str, question: str) -> dict:
    import urllib.error, urllib.request
    payload = json.dumps({
        "model": "claude-opus-4-6", "stream": False,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": question},
            {"type": "image_url", "image_url": {"url": image_url}}
        ]}],
        "max_tokens": 800
    }).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/v1/chat/completions", data=payload,
        headers={"Authorization": f"Bearer {API_KEY}", "Accept": "application/json", "Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        msg = e.read().decode() if e.fp else str(e)
        print(f"HTTP {e.code}: {msg}", file=sys.stderr)
        sys.exit(1)

def main() -> int:
    if len(sys.argv) < 3:
        print("usage: vision_analyze.py <url> <question|--review=ROLE> [--context=SHOT_ID]", file=sys.stderr)
        return 2

    url, arg2 = sys.argv[1], sys.argv[2]
    shot_id = None
    for a in sys.argv[3:]:
        if a.startswith("--context="):
            shot_id = a.split("=", 1)[1]
    ctx = _load_shot_context(shot_id) if shot_id else ""

    if arg2.startswith("--review="):
        role = arg2.split("=", 1)[1]
        roles = ["cinematographer", "production-designer", "director"] if role == "all" else [role]
        for r in roles:
            if r not in ["cinematographer", "production-designer", "director"]:
                print(f"Unknown: {r}", file=sys.stderr); return 2
            q = _make_review_prompt(r, ctx)
            print(f"\n{'='*60}\n  {r.upper()} REVIEW\n{'='*60}")
            print(f"[上下文: {shot_id or '无'} | 问题长度: {len(q)}字符]")
            result = analyze(url, q)
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "No response")
            try: print(content)
            except UnicodeEncodeError: __import__('sys').stdout.buffer.write(content.encode('utf-8') + b'\n')
        return 0

    # Direct question mode
    result = analyze(url, arg2)
    content = result.get("choices", [{}])[0].get("message", {}).get("content", "No response")
    try: print(content)
    except UnicodeEncodeError: __import__('sys').stdout.buffer.write(content.encode('utf-8') + b'\n')
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
