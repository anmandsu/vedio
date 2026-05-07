#!/usr/bin/env python3
"""AI generation API CLI: text-to-image, image-to-image, text-to-video.

Provider: linkapi.org  |  Key: LINKAPI_KEY env  |  Base: LINKAPI_BASE_URL env

Image endpoint: POST /v1/images/generations (gpt-image-2, quality=high)
Video endpoint: POST /v2/videos/generations (grok-video-3)

Usage:
  python gen_api.py image "<prompt>" [--ar=21:9] [--quality=high] [--ref=URL] [--output=path]
  python gen_api.py video "<prompt>" [--output=path]
  python gen_api.py batch <input.json> [--output-dir=renders] [--concurrency=4] [--download]
"""

from __future__ import annotations

import asyncio
import json
import mimetypes
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import aiohttp

BASE_URL = os.environ.get("LINKAPI_BASE_URL", "https://api.linkapi.org").rstrip("/")
API_KEY = os.environ.get("LINKAPI_KEY", "")
REQUEST_TIMEOUT = float(os.environ.get("LINKAPI_TIMEOUT", "600"))
DEFAULT_BATCH_CONCURRENCY = int(os.environ.get("LINKAPI_BATCH_CONCURRENCY", "4"))
DEFAULT_DOWNLOAD_CONCURRENCY = int(os.environ.get("LINKAPI_DOWNLOAD_CONCURRENCY", "8"))


class ApiError(RuntimeError):
    pass


@dataclass
class BatchResult:
    sid: str
    output_path: Path
    result: dict | None = None
    error: str | None = None


def _require_api_key() -> None:
    if not API_KEY:
        print("ERROR: LINKAPI_KEY not set", file=sys.stderr)
        raise SystemExit(1)


def _session_headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
    }


def _timeout() -> aiohttp.ClientTimeout:
    return aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)


def _connector(limit: int) -> aiohttp.TCPConnector:
    return aiohttp.TCPConnector(
        limit=max(1, limit),
        limit_per_host=max(1, limit),
        resolver=aiohttp.ThreadedResolver(),
        ttl_dns_cache=300,
    )


async def _request_json(
    session: aiohttp.ClientSession,
    method: str,
    path: str,
    body: dict | None = None,
) -> dict:
    url = f"{BASE_URL}{path}"
    async with session.request(method, url, json=body) as resp:
        text = await resp.text()
        if resp.status >= 400:
            raise ApiError(f"HTTP {resp.status}: {text}")
        if not text:
            return {}
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise ApiError(f"Invalid JSON response from {url}: {text[:500]}") from exc


def _write_json(result: dict, output_path: str | Path | None) -> None:
    if not output_path:
        return
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[saved] {path}", file=sys.stderr)


async def _write_json_async(result: dict, output_path: str | Path | None) -> None:
    await asyncio.to_thread(_write_json, result, output_path)


def _image_body_from_parts(prompt: str, aspect_ratio: str, quality: str, ref_urls: list[str]) -> dict:
    body: dict = {
        "model": "gpt-image-2",
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "quality": quality,
    }
    if ref_urls:
        body["image"] = ref_urls
    return body


def _parse_image_args(args: list[str]) -> tuple[dict, str | None]:
    if not args:
        print("ERROR: prompt required", file=sys.stderr)
        raise SystemExit(1)

    prompt = args[0]
    aspect_ratio = "21:9"
    quality = "high"
    ref_urls: list[str] = []
    output_path: str | None = None

    for arg in args[1:]:
        if arg.startswith("--ar="):
            aspect_ratio = arg.split("=", 1)[1]
        elif arg.startswith("--quality="):
            quality = arg.split("=", 1)[1]
        elif arg.startswith("--ref="):
            ref_urls.append(arg.split("=", 1)[1])
        elif arg.startswith("--output="):
            output_path = arg.split("=", 1)[1]

    return _image_body_from_parts(prompt, aspect_ratio, quality, ref_urls), output_path


async def cmd_image(args: list[str]) -> int:
    _require_api_key()
    body, output_path = _parse_image_args(args)
    if body.get("image"):
        print(f"[image] img2img with {len(body['image'])} ref(s)...", file=sys.stderr)
    else:
        print(f"[image] generating ({body['aspect_ratio']}, {body['quality']})...", file=sys.stderr)

    async with aiohttp.ClientSession(headers=_session_headers(), timeout=_timeout(), connector=_connector(1)) as session:
        result = await _request_json(session, "POST", "/v1/images/generations", body)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    await _write_json_async(result, output_path)
    return 0


async def cmd_video(args: list[str]) -> int:
    _require_api_key()
    if not args:
        print("ERROR: prompt required", file=sys.stderr)
        raise SystemExit(1)

    prompt = args[0]
    output_path: str | None = None
    for arg in args[1:]:
        if arg.startswith("--output="):
            output_path = arg.split("=", 1)[1]

    body = {"prompt": prompt, "model": "grok-video-3"}
    print("[video] submitting...", file=sys.stderr)
    async with aiohttp.ClientSession(headers=_session_headers(), timeout=_timeout(), connector=_connector(1)) as session:
        result = await _request_json(session, "POST", "/v2/videos/generations", body)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    await _write_json_async(result, output_path)
    return 0


async def cmd_query_video(args: list[str]) -> int:
    _require_api_key()
    limit = 10
    for arg in args:
        if arg.startswith("--limit="):
            limit = int(arg.split("=", 1)[1])

    async with aiohttp.ClientSession(headers=_session_headers(), timeout=_timeout(), connector=_connector(1)) as session:
        result = await _request_json(session, "GET", f"/v2/videos/generations/?limit={limit}")

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def _coerce_ref_urls(item: dict) -> list[str]:
    refs: list[str] = []
    for key in ("reference_urls", "reference_url", "refs", "ref", "image"):
        value = item.get(key)
        if not value:
            continue
        if isinstance(value, str):
            refs.append(value)
        else:
            refs.extend(str(v) for v in value if v)
    return refs


def _body_from_batch_item(item: dict) -> dict:
    return _image_body_from_parts(
        prompt=item["prompt"],
        aspect_ratio=item.get("aspect_ratio", item.get("ar", "21:9")),
        quality=item.get("quality", "high"),
        ref_urls=_coerce_ref_urls(item),
    )


async def _generate_batch_item(
    session: aiohttp.ClientSession,
    semaphore: asyncio.Semaphore,
    item: dict,
    index: int,
    total: int,
    output_dir: Path,
) -> BatchResult:
    sid = item.get("id", f"batch_{index:03d}")
    output_path = output_dir / f"{sid}_response.json"
    body = _body_from_batch_item(item)
    mode = f"img2img/{len(body.get('image', []))}" if body.get("image") else "text2img"

    async with semaphore:
        print(f"[batch {index + 1}/{total}] {sid} {mode}", file=sys.stderr)
        try:
            result = await _request_json(session, "POST", "/v1/images/generations", body)
        except Exception as exc:  # Keep other concurrent jobs alive.
            error = str(exc)
            print(f"[batch {sid}] FAILED: {error}", file=sys.stderr)
            return BatchResult(sid=sid, output_path=output_path, error=error)

    await _write_json_async(result, output_path)
    return BatchResult(sid=sid, output_path=output_path, result=result)


def _extract_image_urls(result: dict) -> list[str]:
    urls: list[str] = []
    for item in result.get("data", []):
        url = item.get("url")
        if url:
            urls.append(url)
    return urls


def _extension_from_url_or_type(url: str, content_type: str | None) -> str:
    if content_type:
        ext = mimetypes.guess_extension(content_type.split(";", 1)[0].strip())
        if ext:
            return ".jpg" if ext == ".jpe" else ext

    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
        return suffix
    return ".png"


async def _download_one_image(
    session: aiohttp.ClientSession,
    semaphore: asyncio.Semaphore,
    url: str,
    base_path: Path,
) -> Path:
    async with semaphore:
        async with session.get(url) as resp:
            data = await resp.read()
            if resp.status >= 400:
                text = data.decode(errors="replace")
                raise ApiError(f"HTTP {resp.status} downloading {url}: {text[:500]}")
            output_path = base_path.with_suffix(_extension_from_url_or_type(url, resp.headers.get("Content-Type")))
            output_path.parent.mkdir(parents=True, exist_ok=True)
            await asyncio.to_thread(output_path.write_bytes, data)
            size_mb = len(data) / (1024 * 1024)
            print(f"[download] {output_path.name} {size_mb:.1f}MB", file=sys.stderr)
            return output_path


async def _download_batch_images(
    results: list[BatchResult],
    download_dir: Path,
    concurrency: int,
) -> int:
    jobs: list[tuple[str, Path]] = []
    for batch_result in results:
        if not batch_result.result:
            continue
        urls = _extract_image_urls(batch_result.result)
        for index, url in enumerate(urls):
            suffix = "" if len(urls) == 1 else f"_{index + 1:02d}"
            jobs.append((url, download_dir / f"{batch_result.sid}{suffix}"))

    if not jobs:
        print("[download] no image URLs found", file=sys.stderr)
        return 0

    print(f"[download] {len(jobs)} image(s), concurrency={concurrency}", file=sys.stderr)
    semaphore = asyncio.Semaphore(max(1, concurrency))
    async with aiohttp.ClientSession(timeout=_timeout(), connector=_connector(concurrency)) as session:
        tasks = [_download_one_image(session, semaphore, url, base_path) for url, base_path in jobs]
        settled = await asyncio.gather(*tasks, return_exceptions=True)

    failures = [item for item in settled if isinstance(item, Exception)]
    for failure in failures:
        print(f"[download] FAILED: {failure}", file=sys.stderr)
    return len(failures)


def _parse_batch_args(args: list[str]) -> tuple[Path, Path, int, bool, Path | None, int]:
    if not args:
        print("ERROR: input json required", file=sys.stderr)
        raise SystemExit(1)

    input_path = Path(args[0])
    output_dir = Path("renders")
    concurrency = DEFAULT_BATCH_CONCURRENCY
    download = False
    download_dir: Path | None = None
    download_concurrency = DEFAULT_DOWNLOAD_CONCURRENCY

    for arg in args[1:]:
        if arg.startswith("--output-dir="):
            output_dir = Path(arg.split("=", 1)[1])
        elif arg.startswith("--concurrency="):
            concurrency = int(arg.split("=", 1)[1])
        elif arg == "--download":
            download = True
        elif arg.startswith("--download-dir="):
            download_dir = Path(arg.split("=", 1)[1])
            download = True
        elif arg.startswith("--download-concurrency="):
            download_concurrency = int(arg.split("=", 1)[1])

    return input_path, output_dir, max(1, concurrency), download, download_dir, max(1, download_concurrency)


async def cmd_batch(args: list[str]) -> int:
    _require_api_key()
    input_path, output_dir, concurrency, download, download_dir, download_concurrency = _parse_batch_args(args)
    items = json.loads(input_path.read_text(encoding="utf-8"))
    output_dir.mkdir(parents=True, exist_ok=True)
    if download_dir is None:
        download_dir = output_dir

    print(f"[batch] {len(items)} prompt(s), concurrency={concurrency}", file=sys.stderr)
    semaphore = asyncio.Semaphore(concurrency)
    async with aiohttp.ClientSession(
        headers=_session_headers(),
        timeout=_timeout(),
        connector=_connector(concurrency),
    ) as session:
        tasks = [
            _generate_batch_item(session, semaphore, item, index, len(items), output_dir)
            for index, item in enumerate(items)
        ]
        results = await asyncio.gather(*tasks)

    failures = sum(1 for item in results if item.error)
    download_failures = 0
    if download:
        download_failures = await _download_batch_images(results, download_dir, download_concurrency)

    if failures or download_failures:
        print(f"[batch] completed with {failures} generation failure(s), {download_failures} download failure(s)", file=sys.stderr)
        return 1

    print("[batch] complete", file=sys.stderr)
    return 0


COMMANDS = {
    "image": cmd_image,
    "video": cmd_video,
    "query-video": cmd_query_video,
    "batch": cmd_batch,
}


async def amain(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print("usage: gen_api.py <image|video|batch|query-video> [args]", file=sys.stderr)
        print("  image \"<prompt>\" [--ar=21:9] [--quality=high] [--ref=URL] [--output=path]", file=sys.stderr)
        print("  batch <input.json> [--output-dir=renders] [--concurrency=4] [--download]", file=sys.stderr)
        return 2
    return await COMMANDS[argv[1]](argv[2:])


def main() -> int:
    return asyncio.run(amain(sys.argv))


if __name__ == "__main__":
    raise SystemExit(main())
