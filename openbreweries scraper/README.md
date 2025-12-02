# Open Brewery DB Scraper

**What this is:**  
A simple, well-documented Python script that fetches brewery data from the Open Brewery DB public API and saves it to CSV. This project demonstrates how to work with API-driven sites, pagination, error handling, and data normalization.

## Why this project
- Example of API-based data extraction (not HTML parsing)
- Clean, reusable code structure for production-like scripts
- Useful dataset for analysis, mapping, or demo dashboards

## Features
- Pagination support (iterates until no more results)
- Retry with exponential backoff on transient errors
- Incremental CSV writing to avoid high memory usage
- Clear normalization of fields for easy downstream use

## Files
- `open_breweries_scraper.py` — main script
- `open_breweries.csv` — sample output (if generated)
- `README.md` — this file

## Requirements
- Python 3.8+
- `requests` (install with `pip install requests`)

Optional:
- `pandas` if you prefer to write/read dataframes for analysis

## How to run
1. Clone the repo:
   ```bash
   git clone git@github.com:<your-username>/python-web-scraping-projects.git
   cd python-web-scraping-projects/open-brewery
