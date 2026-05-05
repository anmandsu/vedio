#!/usr/bin/env python3
"""Lightweight structural continuity lint for VPipe shot YAML."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_yaml(path: Path):
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("PyYAML is required: pip install pyyaml") from exc
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def lint(path: Path) -> dict:
    data = load_yaml(path)
    shots = data.get("shots") or []
    warnings = []
    blockers = []
    strong = []

    for i, shot in enumerate(shots):
        sid = shot.get("shot_id", f"#{i + 1}")
        if not shot.get("style_notes"):
            warnings.append({"shot": sid, "layer": "style", "problem": "missing style_notes"})
        duration = shot.get("duration_sec")
        if isinstance(duration, (int, float)):
            if duration < 3:
                warnings.append({"shot": sid, "layer": "rhythm", "problem": f"very short duration {duration}s"})
            if duration > 12:
                warnings.append({"shot": sid, "layer": "rhythm", "problem": f"long duration {duration}s needs internal evolution"})

        if i == 0:
            continue
        prev = shots[i - 1]
        prev_id = prev.get("shot_id", f"#{i}")
        pair = f"{prev_id}->{sid}"
        same_scene = prev.get("scene_id") == shot.get("scene_id")
        same_character = prev.get("character") == shot.get("character")

        if same_scene and prev.get("location") != shot.get("location"):
            warnings.append({
                "pair": pair,
                "layer": "space",
                "problem": "same scene_id but location text changes; confirm geography",
            })
        if same_character and not (shot.get("continuity_from") or prev.get("continuity_to")):
            warnings.append({
                "pair": pair,
                "layer": "character",
                "problem": "same character across adjacent shots without explicit continuity handoff",
            })
        if prev.get("sound") and shot.get("sound"):
            strong.append({"pair": pair, "layer": "sound", "note": "both shots have sound design; check for bridge or contrast"})

    return {
        "ok": not blockers,
        "shot_count": len(shots),
        "blockers": blockers,
        "warnings": warnings,
        "strong_connections_to_review": strong[:20],
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: continuity_lint.py <file.yaml>", file=sys.stderr)
        return 2
    result = lint(Path(sys.argv[1]))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

