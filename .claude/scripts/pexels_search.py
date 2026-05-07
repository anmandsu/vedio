#!/usr/bin/env python3
"""Search Pexels for photos"""

import requests
import sys
import json

API_KEY = "DKZTpTnbajuZw2cvSxbDY1YsoETk7pV1xCyoq5wkEq2h2CVKpZM9ZsIg"

def search_pexels(query, per_page=15):
    """Search Pexels for photos"""
    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": API_KEY
    }

    params = {
        "query": query,
        "per_page": per_page
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python pexels_search.py <query> [per_page]")
        sys.exit(1)

    query = sys.argv[1]
    per_page = int(sys.argv[2]) if len(sys.argv) > 2 else 15

    result = search_pexels(query, per_page)
    print(json.dumps(result, indent=2, ensure_ascii=False))
