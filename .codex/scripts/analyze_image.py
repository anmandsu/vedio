#!/usr/bin/env python3
"""Analyze images using Claude Opus 4.6 vision API"""

import json
import os
import sys
import urllib.request
import urllib.error

BASE_URL = os.environ.get("LINKAPI_BASE_URL", "https://api.linkapi.org")
API_KEY = os.environ.get("LINKAPI_KEY", "")

def analyze_image(image_url, prompt="Describe this image in detail"):
    """Analyze image using Claude Opus 4.6"""
    if not API_KEY:
        print("ERROR: LINKAPI_KEY not set", file=sys.stderr)
        sys.exit(1)

    url = f"{BASE_URL}/v1/chat/completions"

    payload = {
        "model": "claude-opus-4-6",
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ],
        "max_tokens": 1000
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result['choices'][0]['message']['content']
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}", file=sys.stderr)
        print(e.read().decode(), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python analyze_image.py <image_url> [prompt]")
        sys.exit(1)

    image_url = sys.argv[1]
    prompt = sys.argv[2] if len(sys.argv) > 2 else "Describe this image in detail"

    result = analyze_image(image_url, prompt)
    print(result)
