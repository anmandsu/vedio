#!/usr/bin/env python3
"""picui.cn image hosting CLI — upload, list, delete images.

Token: read from PICUI_API_TOKEN env var or --token flag.
Base URL: read from PICUI_BASE_URL env var, defaults to https://picui.cn/api/v1.

Usage:
  python picui_upload.py upload <file> [--public] [--strategy-id=N] [--album-id=N]
  python picui_upload.py list [--page=1] [--order=newest] [--public]
  python picui_upload.py delete <key>
  python picui_upload.py profile
  python picui_upload.py tokens --num=5 --seconds=3600
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


BASE_URL = os.environ.get("PICUI_BASE_URL", "https://picui.cn/api/v1")
TOKEN = os.environ.get("PICUI_API_TOKEN", "")


def _headers() -> dict:
    if not TOKEN:
        print("ERROR: PICUI_API_TOKEN not set in environment", file=sys.stderr)
        sys.exit(1)
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json",
    }


def _request(method: str, path: str, **kwargs) -> dict:
    import urllib.error
    import urllib.request

    url = f"{BASE_URL}{path}"
    headers = _headers()

    if "files" in kwargs:
        boundary = "----PicUIUploadBoundary2026"
        body = b""
        for field_name, file_path in kwargs.pop("files").items():
            file_bytes = Path(file_path).read_bytes()
            filename = Path(file_path).name
            body += f"--{boundary}\r\n".encode()
            body += f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'.encode()
            body += b"Content-Type: application/octet-stream\r\n\r\n"
            body += file_bytes
            body += b"\r\n"
        for key, val in kwargs.pop("fields", {}).items():
            body += f"--{boundary}\r\n".encode()
            body += f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode()
            body += f"{val}\r\n".encode()
        body += f"--{boundary}--\r\n".encode()

        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    elif "json_data" in kwargs:
        import urllib.parse

        data = json.dumps(kwargs.pop("json_data")).encode()
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        req.add_header("Content-Type", "application/json")
    elif "query" in kwargs:
        import urllib.parse

        query = urllib.parse.urlencode(kwargs.pop("query"))
        url = f"{url}?{query}"
        req = urllib.request.Request(url, headers=headers, method=method)
    else:
        req = urllib.request.Request(url, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode()
            return json.loads(body)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}", file=sys.stderr)
        try:
            print(e.read().decode(), file=sys.stderr)
        except Exception:
            pass
        sys.exit(1)


def cmd_upload(args: list) -> None:
    file_path = args[0] if args else None
    if not file_path or not Path(file_path).exists():
        print(f"ERROR: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    # Parse optional flags from remaining args
    fields = {}
    for arg in args[1:]:
        if arg == "--public":
            fields["permission"] = "1"
        elif arg.startswith("--strategy-id="):
            fields["strategy_id"] = arg.split("=", 1)[1]
        elif arg.startswith("--album-id="):
            fields["album_id"] = arg.split("=", 1)[1]

    result = _request("POST", "/upload", files={"file": file_path}, fields=fields)
    if result.get("status"):
        data = result["data"]
        links = data.get("links", {})
        print(json.dumps({
            "ok": True,
            "key": data["key"],
            "name": data["name"],
            "url": links.get("url", ""),
            "markdown": links.get("markdown", ""),
            "thumbnail_url": links.get("thumbnail_url", ""),
            "delete_url": links.get("delete_url", ""),
            "size_kb": data["size"],
            "mimetype": data["mimetype"],
        }, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_list(args: list) -> None:
    query = {}
    for arg in args:
        if arg.startswith("--page="):
            query["page"] = arg.split("=", 1)[1]
        elif arg.startswith("--order="):
            query["order"] = arg.split("=", 1)[1]
        elif arg == "--public":
            query["permission"] = "public"
        elif arg == "--private":
            query["permission"] = "private"

    result = _request("GET", "/images", query=query)
    if result.get("status"):
        data = result["data"]
        images = data.get("data", [])
        print(json.dumps({
            "ok": True,
            "total": data.get("total", 0),
            "page": data.get("current_page", 1),
            "last_page": data.get("last_page", 1),
            "per_page": data.get("per_page", 15),
            "images": [
                {
                    "key": img["key"],
                    "name": img["name"],
                    "url": img["links"]["url"],
                    "thumbnail_url": img["links"]["thumbnail_url"],
                    "size_kb": img["size"],
                    "width": img.get("width", 0),
                    "height": img.get("height", 0),
                    "date": img.get("date", ""),
                }
                for img in images
            ],
        }, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_delete(args: list) -> None:
    if not args:
        print("ERROR: key required", file=sys.stderr)
        sys.exit(1)
    key = args[0]
    result = _request("DELETE", f"/images/{key}")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_profile(_args: list) -> None:
    result = _request("GET", "/profile")
    if result.get("status"):
        data = result["data"]
        capacity = data.get("capacity", 0)
        size = data.get("size", 0)
        print(json.dumps({
            "ok": True,
            "username": data.get("username", ""),
            "name": data.get("name", ""),
            "avatar": data.get("avatar", ""),
            "email": data.get("email", ""),
            "capacity_mb": round(capacity / 1024, 1) if capacity > 1000 else capacity,
            "used_mb": round(size / 1024, 1) if size > 1000 else size,
            "usage_pct": round(size / capacity * 100, 1) if capacity else 0,
            "image_num": data.get("image_num", 0),
            "album_num": data.get("album_num", 0),
        }, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_tokens(args: list) -> None:
    body = {"num": 5, "seconds": 3600}
    for arg in args:
        if arg.startswith("--num="):
            body["num"] = min(int(arg.split("=", 1)[1]), 100)
        elif arg.startswith("--seconds="):
            body["seconds"] = min(int(arg.split("=", 1)[1]), 2626560)
    result = _request("POST", "/images/tokens", json_data=body)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_albums(args: list) -> None:
    query = {}
    for arg in args:
        if arg.startswith("--page="):
            query["page"] = arg.split("=", 1)[1]

    result = _request("GET", "/albums", query=query)
    if result.get("status"):
        data = result["data"]
        albums = data.get("data", [])
        print(json.dumps({
            "ok": True,
            "total": data.get("total", 0),
            "albums": [
                {"id": a["id"], "name": a["name"], "intro": a.get("intro", ""), "image_num": a["image_num"]}
                for a in albums
            ],
        }, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


COMMANDS = {
    "upload": cmd_upload,
    "list": cmd_list,
    "delete": cmd_delete,
    "profile": cmd_profile,
    "tokens": cmd_tokens,
    "albums": cmd_albums,
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("usage: picui_upload.py <command> [args]", file=sys.stderr)
        print(f"  commands: {', '.join(COMMANDS)}", file=sys.stderr)
        print("  upload <file> [--public] [--strategy-id=N] [--album-id=N]", file=sys.stderr)
        print("  list [--page=N] [--order=newest|earliest|utmost|least] [--public|--private]", file=sys.stderr)
        print("  delete <key>", file=sys.stderr)
        print("  profile", file=sys.stderr)
        print("  tokens [--num=N] [--seconds=N]", file=sys.stderr)
        print("  albums [--page=N]", file=sys.stderr)
        return 2

    cmd = sys.argv[1]
    args = sys.argv[2:]
    COMMANDS[cmd](args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
