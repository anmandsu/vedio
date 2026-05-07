#!/usr/bin/env python3
"""Download scene images using curl."""

import json
import subprocess
from pathlib import Path

scenes_dir = Path(__file__).parent.parent.parent / "projects" / "daguangsai" / "renders" / "scenes"

response_files = sorted(scenes_dir.glob("*_response.json"))
print(f"Found {len(response_files)} response files\n")

for json_file in response_files:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    url = data['data'][0]['url']
    scene_id = json_file.stem.replace('_response', '')
    output_file = scenes_dir / f"{scene_id}.png"

    print(f"[{response_files.index(json_file)+1}/{len(response_files)}] {scene_id}")

    result = subprocess.run(
        ['curl', '-s', '-o', str(output_file), url],
        capture_output=True
    )

    if result.returncode == 0 and output_file.exists():
        size_mb = output_file.stat().st_size / (1024*1024)
        print(f"  OK: {size_mb:.1f}MB\n")
    else:
        print(f"  FAILED\n")

print("Download complete!")
