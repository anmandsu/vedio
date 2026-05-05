#!/usr/bin/env python3
"""Get TMDB movie images"""

import requests
import sys
import json

ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZGMwOWNjMmUyMGNhODU0MTJhYzY1ZDc1ODVmMDE2YiIsIm5iZiI6MTc3Nzc1NjA4My40NDYsInN1YiI6IjY5ZjY2N2IzNWIyZjM1NTEzYzdkMGU1YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qQEhgpvbw5-vlkMJxHBwKVJ3vzyE2vqPZFb2oUSTKT4"

def get_movie_images(movie_id):
    """Get images for a movie"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print("Usage: python tmdb_images.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    result = get_movie_images(movie_id)

    # Print backdrop URLs
    print("Backdrops:")
    for img in result.get('backdrops', [])[:10]:
        print(f"https://image.tmdb.org/t/p/original{img['file_path']}")
