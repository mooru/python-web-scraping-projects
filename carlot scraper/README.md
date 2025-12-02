# **Carlots.ng Web Scraper 🚗🕸️**

A Python web scraping script that extracts car listings from **Carlots.ng**, including:
- Car make & model
- Price
- Location
- Seller
- Description
- Listing link
- And more

This project demonstrates practical skills in **Python**, **Requests**, **BeautifulSoup**, and **data extraction for CSV**.  
It is part of my growing portfolio of real-world web scraping projects.

---

## **📌 Features**
- Scrapes multiple pages automatically
- Extracts all essential listing details
- Structured output into a clean CSV file
- Handles missing values gracefully
- Simple, readable code

---

## **📁 Data Extracted**

Each row in the CSV contains:

| Field         | Description                 |
| ------------- | --------------------------- |
| `make`        | Car manufacturer            |
| `car`         | Title/model name            |
| `price`       | Listed price                |
| `location`    | General location on listing |
| `duration`    | Time since posted           |
| `seller`      | Seller name                 |
| `city`        | City                        |
| `state`       | State                       |
| `description` | Short description           |
| `link`        | URL to the full listing     |

---

## **🛠️ Technologies Used**
- Python 3
- Requests
- BeautifulSoup (bs4)
- Pandas

---

## **🚀 How to Run**
1. Clone the repository
2. Install dependencies:

`pip install -r requirements.txt`

3. Run the scraper:

`python carlots_scraper.py`

4. Output will be saved as:

`car_listings.csv`

---

## **📌 Notes**
- This scraper is for **educational and portfolio purposes only**.
- Respect website terms of service & robots.txt before scraping any site.

---

## **📧 Contact / Hire Me**
If you need **custom web scraping**, **data extraction**, or **automation tools**, feel free to reach out.