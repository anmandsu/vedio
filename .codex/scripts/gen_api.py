#!/usr/bin/env python3
"""AI generation API CLI — text-to-image, image-to-image, text-to-video.

Provider: linkapi.org  |  Key: LINKAPI_KEY env  |  Base: LINKAPI_BASE_URL env

Image endpoint: POST /v1/images/generations (gpt-image-2, quality=high)
Video endpoint: POST /v2/videos/generations (grok-video-3)

Usage:
  python gen_api.py image "<prompt>" [--ar=21:9] [--quality=high] [--ref=URL] [--output=path]
  python gen_api.py video "<prompt>" [--output=path]
  python gen_api.py batch <input.json> [--output-dir=renders]
"""

from __future__ import annotations
import json, os, sys, time
from pathlib import Path

BASE_URL = os.environ.get("LINKAPI_BASE_URL", "https://api.linkapi.org")
API_KEY = os.environ.get("LINKAPI_KEY", "")

def _req(method: str, path: str, body: dict | None = None) -> dict:
    import urllib.error, urllib.request
    if not API_KEY:
        print("ERROR: LINKAPI_KEY not set", file=sys.stderr); sys.exit(1)
    url = f"{BASE_URL}{path}"
    headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        msg = e.read().decode() if e.fp else str(e)
        print(f"HTTP {e.code}: {msg}", file=sys.stderr); sys.exit(1)

# ── Image Generation (gpt-image-2, /v1/images/generations) ──

def cmd_image(args: list) -> None:
    if not args: print("ERROR: prompt required", file=sys.stderr); sys.exit(1)
    prompt = args[0]
    aspect_ratio = "21:9"
    quality = "high"
    ref_urls: list[str] = []
    output_path: str | None = None

    for a in args[1:]:
        if a.startswith("--ar="):       aspect_ratio = a.split("=",1)[1]
        elif a.startswith("--quality="): quality = a.split("=",1)[1]
        elif a.startswith("--ref="):     ref_urls.append(a.split("=",1)[1])
        elif a.startswith("--output="):  output_path = a.split("=",1)[1]

    body: dict = {
        "model": "gpt-image-2",
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "quality": quality,
    }
    if ref_urls:
        body["image"] = ref_urls
        print(f"[image] img2img with {len(ref_urls)} ref(s)...", file=sys.stderr)
    else:
        print(f"[image] generating ({aspect_ratio}, {quality})...", file=sys.stderr)

    result = _req("POST", "/v1/images/generations", body)
    _output(result, output_path)

def _output(result: dict, output_path: str | None) -> None:
    formatted = json.dumps(result, ensure_ascii=False, indent=2)
    print(formatted)
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(formatted, encoding="utf-8")
        print(f"[saved] {output_path}", file=sys.stderr)

# ── Video Generation (grok-video-3, /v2/videos/generations) ──

def cmd_video(args: list) -> None:
    if not args: print("ERROR: prompt required", file=sys.stderr); sys.exit(1)
    prompt = args[0]
    output_path: str | None = None
    for a in args[1:]:
        if a.startswith("--output="): output_path = a.split("=",1)[1]
    body = {"prompt": prompt, "model": "grok-video-3"}
    print("[video] submitting...", file=sys.stderr)
    result = _req("POST", "/v2/videos/generations", body)
    _output(result, output_path)

def cmd_query_video(args: list) -> None:
    limit = 10
    for a in args:
        if a.startswith("--limit="): limit = int(a.split("=",1)[1])
    result = _req("GET", f"/v2/videos/generations/?limit={limit}")
    print(json.dumps(result, ensure_ascii=False, indent=2))

# ── Batch ──

def cmd_batch(args: list) -> None:
    if not args: print("ERROR: input json required", file=sys.stderr); sys.exit(1)
    input_path = args[0]
    output_dir = "renders"
    for a in args[1:]:
        if a.startswith("--output-dir="): output_dir = a.split("=",1)[1]
    items = json.loads(Path(input_path).read_text(encoding="utf-8"))
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    print(f"[batch] {len(items)} prompts", file=sys.stderr)
    for i, item in enumerate(items):
        sid = item.get("id", f"batch_{i:03d}")
        sub = [item["prompt"]]
        if item.get("reference_url"):
            sub.append(f"--ref={item['reference_url']}")
        if item.get("aspect_ratio"):
            sub.append(f"--ar={item['aspect_ratio']}")
        if item.get("quality"):
            sub.append(f"--quality={item['quality']}")
        sub.append(f"--output={output_dir}/{sid}_response.json")
        print(f"[batch {i+1}/{len(items)}] {sid}", file=sys.stderr)
        cmd_image(sub)
        time.sleep(1)

COMMANDS = {"image": cmd_image, "video": cmd_video, "query-video": cmd_query_video, "batch": cmd_batch}

def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("usage: gen_api.py <image|video|batch|query-video> [args]", file=sys.stderr)
        print("  image \"<prompt>\" [--ar=21:9] [--quality=high] [--ref=URL] [--output=path]", file=sys.stderr)
        print("  batch <input.json> [--output-dir=renders]", file=sys.stderr)
        return 2
    COMMANDS[sys.argv[1]](sys.argv[2:]); return 0

if __name__ == "__main__":
    raise SystemExit(main())
