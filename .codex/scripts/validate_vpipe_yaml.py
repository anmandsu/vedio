#!/usr/bin/env python3
"""Validate the VPipe shot YAML structure."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED = [
    "shot_id",
    "scene_id",
    "character",
    "location",
    "plot",
    "performance",
    "lighting",
    "camera",
    "blocking",
    "sound",
    "dialogue",
    "duration_sec",
    "beat_type",
    "style_notes",
]


def load_yaml(path: Path):
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("PyYAML is required: pip install pyyaml") from exc
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def validate(path: Path) -> dict:
    data = load_yaml(path)
    issues = []
    if not isinstance(data, dict):
        return {"ok": False, "issues": ["Top-level YAML is not a mapping"]}

    for key in ["episode", "title", "style", "shots"]:
        if key not in data:
            issues.append(f"Missing top-level key: {key}")

    shots = data.get("shots") or []
    if not isinstance(shots, list) or not shots:
        issues.append("shots must be a non-empty list")
        shots = []

    seen = set()
    for idx, shot in enumerate(shots):
        if not isinstance(shot, dict):
            issues.append(f"Shot #{idx + 1} is not a mapping")
            continue
        shot_id = shot.get("shot_id", f"#{idx + 1}")
        if shot_id in seen:
            issues.append(f"Duplicate shot_id: {shot_id}")
        seen.add(shot_id)
        for field in REQUIRED:
            if field not in shot or shot.get(field) in ("", None):
                issues.append(f"{shot_id}: missing {field}")
        duration = shot.get("duration_sec")
        if isinstance(duration, (int, float)) and (duration <= 0 or duration > 30):
            issues.append(f"{shot_id}: unusual duration_sec {duration}")

    return {
        "ok": not issues,
        "shot_count": len(shots),
        "issues": issues,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_vpipe_yaml.py <file.yaml>", file=sys.stderr)
        return 2
    result = validate(Path(sys.argv[1]))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

