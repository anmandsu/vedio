#!/usr/bin/env python3
"""Download scene images from response JSON files."""

import json
import urllib.request
from pathlib import Path

scenes_dir = Path(__file__).parent.parent.parent / "projects" / "daguangsai" / "renders" / "scenes"

for json_file in scenes_dir.glob("*_response.json"):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    url = data['data'][0]['url']
    scene_id = json_file.stem.replace('_response', '')
    output_file = scenes_dir / f"{scene_id}.png"

    print(f"Downloading {scene_id}...")
    urllib.request.urlretrieve(url, output_file)
    print(f"  Saved: {output_file.name}")

print("\nAll images downloaded!")
