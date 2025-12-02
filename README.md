A collection of practical web scraping scripts built using Python, showcasing different scraping techniques, patterns, and data-extraction workflows.
This repository serves as a growing portfolio of my skills in:

- Extracting real-world data from websites
- Consuming public APIs
- Cleaning and structuring data
- Saving results to CSV
- Building reusable, readable Python scripts
  
Each project includes:

✔ A dedicated folder
✔ Python code (.py)
✔ Sample output
✔ A clear README.md explaining how the scraper works

## 📌 Projects Included
### 1. Konga Product Scraper (API-based)

A scraper that interacts with Konga’s hidden Algolia API to extract product data such as name, price, category, brand, and product URL.

**Highlights**

- Demonstrates API request scraping
- Supports pagination
- Saves structured data to CSV
- Includes helper functions for cleaning and normalizing categories

### 2. Carlots.ng Car Listing Scraper (HTML-based)

Scrapes vehicle listings from Carlots.ng by parsing HTML elements.

**Highlights**

- BeautifulSoup HTML extraction
- Pagination handling
- Clean field extraction (make, price, seller, city, state, etc.)

### 3. Brewery API Scraper (Public API)

Fetches brewery information from the Open Brewery DB.

**Highlights**

- Uses a real public REST API
- Demonstrates pagination and metadata handling
- Clean JSON → CSV transformation

## 🛠️ Tech Stack

- Python 3.x
- Requests — for HTTP requests
- BeautifulSoup (bs4) — for HTML parsing
- Pandas — for data cleaning and CSV output
- CSV module — lightweight data export

## 📁 Project Structure
```md
python-web-scraping-projects/
│
├── konga-scraper/
│   ├── konga_scraper.py
│   ├── sample_output.csv
│   ├── requirements.txt
│   └── README.md
│
├── carlots-scraper/
│   ├── carlots_scraper.py
│   ├── car_listings.csv
│   ├── requirements.txt
│   └── README.md
│
└── brewery-scraper/
    ├── brewery_scraper.py
    ├── breweries.csv
    ├── requirements.txt
    └── README.md
```


## 📚 Goals of This Repository

This repo is designed to:

- Demonstrate core web scraping skills
- Serve as a portfolio for freelance platforms like Fiverr
- Show versatility across API-based, HTML-based, and pagination projects
- Act as a learning resource for anyone new to Python scraping

## 🚀 Future Additions

More scrapers will be added, including:

- E-commerce scrapers
- Business directories
- Finance & crypto data sources
- Job listing scrapers
- News article extractors

## 📬 Contact

If you’d like custom web scraping or data extraction work done, feel free to reach out.