#!/usr/bin/env python3
"""Create a project skeleton for the AI video studio."""

from __future__ import annotations

import argparse
from pathlib import Path
from datetime import date


DIRS = [
    "script",
    "research",
    "crew",
    "bible/characters",
    "bible/scenes",
    "bible/props",
    "bible/moodboard",
    "bible/fingerprints",
    "shots",
    "boards",
    "prompts",
    "renders/images",
    "renders/video",
    "reviews",
    "memory",
]


def write_if_missing(path: Path, text: str) -> None:
    if not path.exists():
        path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", help="Folder-safe project id, e.g. desert-episode-01")
    parser.add_argument("--title", default="", help="Human title")
    parser.add_argument("--root", default=".", help="Workspace root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    project = root / "projects" / args.project_id
    project.mkdir(parents=True, exist_ok=True)

    for rel in DIRS:
        (project / rel).mkdir(parents=True, exist_ok=True)

    title = args.title or args.project_id
    write_if_missing(
        project / "STATUS.md",
        f"""# {title}

- Project id: {args.project_id}
- Created: {date.today().isoformat()}
- Current phase: intake

## Next Actions

- Add source script to `script/script.md`
- Run video-script-intake
- Build reference research pack
""",
    )
    write_if_missing(project / "script" / "script.md", "# Script\n\nPaste or link the script here.\n")
    write_if_missing(project / "research" / "INDEX.md", "# Research Index\n\n")
    write_if_missing(project / "crew" / "creative-brief.md", "# Creative Brief\n\n")
    write_if_missing(project / "bible" / "characters" / "INDEX.md", "# Character Index\n\n")
    write_if_missing(project / "bible" / "scenes" / "INDEX.md", "# Scene Index\n\n")
    write_if_missing(project / "bible" / "props" / "INDEX.md", "# Prop Index\n\n")
    write_if_missing(project / "memory" / "project-lessons.md", "# Project Lessons\n\n")
    print(project)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

