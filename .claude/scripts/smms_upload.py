#!/usr/bin/env python3
"""Upload image to sm.ms free image hosting."""
import sys, json
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode

def upload(image_path: str) -> dict:
    """Upload image to sm.ms and return response."""
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    with open(image_path, 'rb') as f:
        image_data = f.read()

    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="smfile"; filename="{Path(image_path).name}"\r\n'
        f'Content-Type: image/png\r\n\r\n'
    ).encode() + image_data + f'\r\n--{boundary}--\r\n'.encode()

    req = Request(
        'https://sm.ms/api/v2/upload',
        data=body,
        headers={
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'User-Agent': 'Mozilla/5.0'
        }
    )

    with urlopen(req) as resp:
        result = json.loads(resp.read().decode())

    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python smms_upload.py <image_path>", file=sys.stderr)
        sys.exit(1)

    result = upload(sys.argv[1])
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if result.get('success'):
        print(f"\nURL: {result['data']['url']}", file=sys.stderr)
