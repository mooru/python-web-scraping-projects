import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

BASE_URL = "https://carlots.ng/search/pn,{}"


def extract_text(parent, tag, class_name):
    el = parent.find(tag, class_=class_name)
    return el.text.strip() if el else None


def scrape_carlots(page_number):
    response = requests.get(BASE_URL.format(page_number), headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("div", class_="simple-wrap")

    listings = []

    for product in products:
        title_el = product.find("a", class_="title2")
        title = title_el.text.strip() if title_el else None
        link = "https://carlots.ng" + title_el["href"] if title_el else None

        listings.append(
            {
                "make": extract_text(product, "span", "e4"),
                "car": title,
                "price": extract_text(product, "div", "price"),
                "location": extract_text(product, "div", "location"),
                "duration": extract_text(product, "span", "dt"),
                "seller": extract_text(product, "strong", "cn"),
                "city": extract_text(product, "a", "reg"),
                "state": extract_text(product, "a", "cit"),
                "description": extract_text(product, "div", "description"),
                "link": link,
            }
        )

    return listings


all_listings = []

for page in range(1, 11):
    print(f"Scraping page {page}...")
    data = scrape_carlots(page)

    if not data:
        print("No more data found. Stopping.")
        break

    all_listings.extend(data)

df = pd.DataFrame(all_listings)
df.to_csv("car_listings.csv", index=False)

print(f"Saved {len(all_listings)} car listings to car_listings.csv")
