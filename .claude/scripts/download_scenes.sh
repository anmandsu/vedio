#!/bin/bash
# Download all scene images from response JSON files

cd "C:\Users\123\Videos\视频V3\projects\daguangsai\renders\scenes"

# Extract URLs and download
for json_file in *_response.json; do
    scene_id="${json_file%_response.json}"
    url=$(grep -o '"url":"[^"]*"' "$json_file" | cut -d'"' -f4)

    if [ -n "$url" ]; then
        echo "Downloading $scene_id..."
        curl -s -o "${scene_id}.png" "$url"
        echo "  Done: ${scene_id}.png"
    fi
done

echo ""
echo "All images downloaded!"
ls -lh *.png
