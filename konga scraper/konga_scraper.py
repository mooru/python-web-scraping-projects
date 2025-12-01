import csv
import sys
import time

import requests

ALGOLIA_APP_ID = "B9ZCRRRVOM"
ALGOLIA_API_KEY = (
    "1013eebf1ca008149d66ea7a385a1366"  # if restricted, this will still give 403
)


def extract_category(item):
    categories = item.get("categories")
    if not categories:
        return None
    if isinstance(categories, list):
        return categories[0] if categories else None
    if isinstance(categories, dict):
        return categories.get("lvl0") or next(iter(categories.values()), None)
    return None


def get_products(page=0, timeout=10):
    url = "https://b9zcrrrvom-dsn.algolia.net/1/indexes/*/queries"
    headers = {
        "Accept-Language": "en-US,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0)",
        "Accept": "application/json",
        "Content-Type": "application/json",
        # Explicit Algolia headers (more reliable than querystring)
        "X-Algolia-API-Key": ALGOLIA_API_KEY,
        "X-Algolia-Application-Id": ALGOLIA_APP_ID,
        "Origin": "https://www.konga.com",
        "Referer": "https://www.konga.com/",
    }

    payload = {
        "requests": [
            {
                "indexName": "catalog_store_konga_ranking",
                "params": (
                    f"query=&maxValuesPerFacet=50&page={page}"
                    "&highlightPreTag=%3Cais-highlight-0000000000%3E"
                    "&highlightPostTag=%3C%2Fais-highlight-0000000000%3E"
                    "&facets=%5B%22categories.lvl0%22%2C%22attributes.brand%22%5D"
                ),
            }
        ]
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=timeout)
        # Helpful debug info if it fails
        if resp.status_code != 200:
            print(
                f"Algolia responded {resp.status_code}: {resp.text[:400]}",
                file=sys.stderr,
            )
            resp.raise_for_status()
        data = resp.json()
        return data["results"][0]["hits"]
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e, file=sys.stderr)
        raise
    except requests.exceptions.RequestException as e:
        print("Request exception:", e, file=sys.stderr)
        raise


def scrape_all_products(max_pages=50):
    all_products = []
    for page in range(max_pages):
        print(f"Scraping page {page}...")
        items = get_products(page)
        if not items:
            print("No more products found. Stopping.")
            break
        for item in items:
            product = {
                "id": item.get("product_id"),
                "name": item.get("name"),
                "price": item.get("special_price") or item.get("price"),
                "brand": item.get("brand"),
                "category": extract_category(item),
                "url": "https://www.konga.com/product/" + (item.get("slug") or ""),
            }
            all_products.append(product)
        time.sleep(1)
    return all_products


def save_to_csv(products, filename="konga_products_2.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Price", "Brand", "Category", "URL"])
        for p in products:
            writer.writerow(
                [p["id"], p["name"], p["price"], p["brand"], p["category"], p["url"]]
            )
    print(f"Saved {len(products)} products to {filename}")


if __name__ == "__main__":
    products = scrape_all_products(max_pages=50)
    save_to_csv(products)
