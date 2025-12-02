#!/usr/bin/env python3
"""
scrape_breweries.py

Fetch brewery data from Open Brewery DB and save to CSV.
This script is defensive: it checks response types and logs helpful errors
so a beginner can understand what went wrong.
"""

import csv
import time
from typing import Any, Dict, List

import requests

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"  # v1 breweries list endpoint
PER_PAGE = 50  # number of items per page (v1 supports pagination by page param)


def fetch_page(page: int) -> List[Dict[str, Any]]:
    """Fetch one page of breweries. Returns a list of dicts (may be empty)."""
    params = {"page": page, "per_page": PER_PAGE}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
    except requests.RequestException as e:
        print(f"[ERROR] Network error when fetching page {page}: {e}")
        return []

    if resp.status_code != 200:
        print(
            f"[ERROR] Received status {resp.status_code} for page {page}: {resp.text[:200]}"
        )
        return []

    # parse JSON safely
    try:
        data = resp.json()
    except ValueError as e:
        print(f"[ERROR] Failed to parse JSON for page {page}: {e}")
        print("Response (first 500 chars):", resp.text[:500])
        return []

    # now check type
    if isinstance(data, list):
        return data
    else:
        # If it's not a list, print debug info and return empty list
        print(
            f"[ERROR] Expected list for page {page} but got {type(data).__name__}. Data preview:"
        )
        print(data if isinstance(data, (dict, str)) else str(data)[:500])
        return []


def normalize_brewery(item: Dict[str, Any]) -> Dict[str, Any]:
    """Return a clean dict with fields we want, using .get safely."""
    return {
        "id": item.get("id"),
        "name": item.get("name"),
        "brewery_type": item.get("brewery_type"),
        "street": item.get("street"),
        "city": item.get("city"),
        "state": item.get("state"),
        "postal_code": item.get("postal_code"),
        "country": item.get("country"),
        "longitude": item.get("longitude"),
        "latitude": item.get("latitude"),
        "phone": item.get("phone"),
        "website_url": item.get("website_url"),
    }


def scrape_all(max_pages: int = 20, pause: float = 0.5) -> List[Dict[str, Any]]:
    """Scrape multiple pages until an empty page is returned or max_pages reached."""
    results = []
    for page in range(1, max_pages + 1):
        print(f"[INFO] Fetching page {page} ...")
        items = fetch_page(page)
        if not items:
            print("[INFO] No items returned — stopping.")
            break

        for item in items:
            if not isinstance(item, dict):
                print(
                    f"[WARN] Skipping non-dict item on page {page}: {type(item).__name__}"
                )
                continue
            results.append(normalize_brewery(item))

        time.sleep(pause)  # be polite
    return results


def save_csv(rows: List[Dict[str, Any]], filename: str = "breweries.csv"):
    if not rows:
        print("[WARN] No rows to save.")
        return
    keys = list(rows[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    print(f"[INFO] Saved {len(rows)} rows to {filename}")


if __name__ == "__main__":
    data = scrape_all(max_pages=10, pause=0.3)
    save_csv(data)
