#!/usr/bin/env python3
"""Pinterest image search via RapidAPI"""

import requests
import sys
import json

RAPIDAPI_KEY = "ebc81085cfmshe8f9fafa9c026a4p170c32jsn7980091293b5"
RAPIDAPI_HOST = "pinterest-pin-search.p.rapidapi.com"

def search_pinterest(keyword, offset=0):
    """Search Pinterest for images"""
    url = "https://pinterest-pin-search.p.rapidapi.com/rapidapi/search"

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }

    params = {
        "offset": str(offset),
        "keyword": keyword,
        "r": "search/pinterest"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python pinterest_search.py <keyword> [offset]")
        sys.exit(1)

    keyword = sys.argv[1]
    offset = int(sys.argv[2]) if len(sys.argv) > 2 else 0

    result = search_pinterest(keyword, offset)
    print(json.dumps(result, indent=2, ensure_ascii=False))
