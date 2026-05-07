#!/usr/bin/env python3
"""Download scene images from response JSON files concurrently."""

from __future__ import annotations

import asyncio
import json
import mimetypes
from pathlib import Path
from urllib.parse import urlparse

import aiohttp

SCENES_DIR = Path(__file__).parent.parent.parent / "projects" / "daguangsai" / "renders" / "scenes"
DOWNLOAD_CONCURRENCY = 8


def _extension_from_url_or_type(url: str, content_type: str | None) -> str:
    if content_type:
        ext = mimetypes.guess_extension(content_type.split(";", 1)[0].strip())
        if ext:
            return ".jpg" if ext == ".jpe" else ext

    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
        return suffix
    return ".png"


def _jobs_from_response_files(scenes_dir: Path) -> list[tuple[str, Path]]:
    jobs: list[tuple[str, Path]] = []
    for json_file in sorted(scenes_dir.glob("*_response.json")):
        data = json.loads(json_file.read_text(encoding="utf-8"))
        scene_id = json_file.stem.replace("_response", "")
        urls = [item["url"] for item in data.get("data", []) if item.get("url")]
        for index, url in enumerate(urls):
            suffix = "" if len(urls) == 1 else f"_{index + 1:02d}"
            jobs.append((url, scenes_dir / f"{scene_id}{suffix}"))
    return jobs


async def _download_one(
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
                raise RuntimeError(f"HTTP {resp.status} downloading {url}: {text[:500]}")
            output_path = base_path.with_suffix(_extension_from_url_or_type(url, resp.headers.get("Content-Type")))
            output_path.write_bytes(data)
            size_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"OK {output_path.name} {size_mb:.1f}MB")
            return output_path


async def main() -> int:
    jobs = _jobs_from_response_files(SCENES_DIR)
    print(f"Found {len(jobs)} image URL(s)")
    if not jobs:
        return 0

    semaphore = asyncio.Semaphore(DOWNLOAD_CONCURRENCY)
    timeout = aiohttp.ClientTimeout(total=600)
    connector = aiohttp.TCPConnector(
        limit=DOWNLOAD_CONCURRENCY,
        limit_per_host=DOWNLOAD_CONCURRENCY,
        resolver=aiohttp.ThreadedResolver(),
        ttl_dns_cache=300,
    )
    async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
        tasks = [_download_one(session, semaphore, url, base_path) for url, base_path in jobs]
        settled = await asyncio.gather(*tasks, return_exceptions=True)

    failures = [item for item in settled if isinstance(item, Exception)]
    for failure in failures:
        print(f"FAILED {failure}")

    print("Download complete!")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
