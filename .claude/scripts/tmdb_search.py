#!/usr/bin/env python3
"""Search TMDB (The Movie Database)"""

import requests
import sys
import json

API_KEY = "1dc09cc2e20ca85412ac65d7585f016b"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZGMwOWNjMmUyMGNhODU0MTJhYzY1ZDc1ODVmMDE2YiIsIm5iZiI6MTc3Nzc1NjA4My40NDYsInN1YiI6IjY5ZjY2N2IzNWIyZjM1NTEzYzdkMGU1YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qQEhgpvbw5-vlkMJxHBwKVJ3vzyE2vqPZFb2oUSTKT4"

def search_tmdb(query, media_type="movie"):
    """Search TMDB for movies or TV shows"""
    url = f"https://api.themoviedb.org/3/search/{media_type}"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "accept": "application/json"
    }

    params = {
        "query": query,
        "language": "zh-CN"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python tmdb_search.py <query> [movie|tv]")
        sys.exit(1)

    query = sys.argv[1]
    media_type = sys.argv[2] if len(sys.argv) > 2 else "movie"

    result = search_tmdb(query, media_type)
    print(json.dumps(result, indent=2, ensure_ascii=False))
