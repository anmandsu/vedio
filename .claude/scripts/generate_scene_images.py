#!/usr/bin/env python3
"""Generate scene reference images based on scene descriptions."""

import json
import os
import sys
from pathlib import Path

# Scene descriptions for image generation
SCENES = [
    {
        "id": "SC01_OLD_EMBROIDERY_SHOP_MORNING",
        "name": "老绣坊-清晨",
        "prompt": "Interior of traditional Shu embroidery workshop, early morning, cold gray tone, color temperature 3200K, hard light, high contrast, side light from window, wooden embroidery frame in center, silk threads and needles on table, aged wooden furniture, minimalist composition, realistic style, cinematic lighting, 35mm lens, shallow depth of field",
        "reference_url": None
    },
    {
        "id": "SC02_OLD_EMBROIDERY_SHOP_EVENING",
        "name": "老绣坊-傍晚",
        "prompt": "Interior of traditional Shu embroidery workshop, evening, low saturation, color temperature 3500K, indoor lighting mixed with natural light, wooden embroidery frame, traditional Chinese furniture, warm indoor lamps, realistic style, cinematic lighting, 50mm lens",
        "reference_url": None
    },
    {
        "id": "SC03_OLD_EMBROIDERY_SHOP_NIGHT",
        "name": "老绣坊-夜晚",
        "prompt": "Interior of traditional Shu embroidery workshop, night, no indoor lights, only cold light from window, color temperature 3000K, very low illumination, high contrast, dark atmosphere, wooden embroidery frame silhouette, oppressive mood, realistic style, cinematic lighting, 35mm lens",
        "reference_url": None
    },
    {
        "id": "SC04_OLD_EMBROIDERY_SHOP_DEEP_NIGHT",
        "name": "老绣坊-深夜",
        "prompt": "Interior of traditional Shu embroidery workshop, deep night, warm yellow lamp light, color temperature 3800K, soft light, low contrast, cozy atmosphere, wooden embroidery frame, traditional Chinese furniture, warm reconciliation mood, realistic style, cinematic lighting, 50mm lens",
        "reference_url": None
    },
    {
        "id": "SC05_OLD_HOUSE_FLASHBACK",
        "name": "旧屋-闪回",
        "prompt": "Interior of old traditional Chinese house, night flashback scene, oil lamp lighting, warm yellow tone, color temperature 2700K, soft light, low illumination, nostalgic atmosphere, simple wooden furniture, embroidery frame, grandmother and young girl, vintage film grain, realistic style, cinematic lighting, 50mm lens",
        "reference_url": None
    },
    {
        "id": "SC09_MORNING_WARM",
        "name": "老绣坊-清晨温暖",
        "prompt": "Interior of traditional Shu embroidery workshop, morning, warm tone transition, color temperature 4500K, soft light, natural light from window, wooden embroidery frame, computer and camera equipment, modern meets traditional, hopeful atmosphere, realistic style, cinematic lighting, 35mm lens",
        "reference_url": None
    },
    {
        "id": "SC12_SUNSET",
        "name": "老绣坊-夕阳",
        "prompt": "Interior of traditional Shu embroidery workshop, sunset, warm golden light, color temperature 5500K, soft light, high saturation, warm atmosphere, wooden embroidery frame, family gathering, reconciliation mood, beautiful sunset glow through window, realistic style, cinematic lighting, 50mm lens",
        "reference_url": None
    }
]


def generate_batch_manifest():
    """Generate batch manifest for scene images."""
    project_dir = Path(__file__).parent.parent.parent / "projects" / "daguangsai"
    output_dir = project_dir / "renders" / "scenes"
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = output_dir / "scene_batch.json"

    batch_data = []
    for scene in SCENES:
        batch_data.append({
            "id": scene["id"],
            "prompt": scene["prompt"],
            "reference_url": scene["reference_url"]
        })

    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(batch_data, f, ensure_ascii=False, indent=2)

    print(f"Batch manifest created: {manifest_path}")
    print(f"Total scenes: {len(batch_data)}")
    print("\nTo generate images, run:")
    print(f'LINKAPI_KEY="your-key" python .claude/scripts/gen_api.py batch "{manifest_path}" --output-dir="{output_dir}"')

    return manifest_path


def main():
    manifest_path = generate_batch_manifest()

    print("\n=== Scene List ===")
    for idx, scene in enumerate(SCENES, 1):
        print(f"{idx}. {scene['name']} ({scene['id']})")


if __name__ == "__main__":
    main()
