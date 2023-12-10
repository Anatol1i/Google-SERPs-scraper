# README for SERP URL Scraper and Data Extractor

## Introduction
This repository contains two Python scripts:
1. A JavaScript bookmarklet for scraping URLs from Google Search Engine Results Pages (SERP).
2. A Python script for extracting specific data (emails and phone numbers) from the scraped URLs.

## Prerequisites
- Basic understanding of JavaScript and Python.
- Web browser (preferably Google Chrome or Firefox).
- Python environment with necessary libraries installed (requests, BeautifulSoup, pandas).

## Installation
1. **JavaScript Bookmarklet**: 
   - Create a new bookmark in your browser.
   - Name the bookmark (e.g., "SERP URL Scraper").
   - In the URL field, paste the provided JavaScript code.
   - Save the bookmark.

2. **Python Script**: 
   - Ensure Python is installed on your machine.
   - Install the required libraries by running `pip install requests beautifulsoup4 pandas lxml`.

## Usage
### SERP URL Scraper
1. Open Google and perform a search query.
2. Scroll through the SERP to load all desired results.
3. Click on the previously saved bookmark.
4. A new page will open, displaying a list of URLs.
5. Click on the "Download URLs as Text File" link to save the URLs.

### Data Extractor Script
1. Place the downloaded text file containing URLs in an accessible directory.
2. Open the Python scraper script.
3. Modify the line `with open('path to txt file', 'r') as file:` to include the correct path to your text file.
4. Optionally, customize the `kategorie_value` variable and regex patterns in `sequences` as needed.
5. Run the script. It will process each URL and extract emails and phone numbers.
6. The results will be saved in a CSV file named after the `kategorie_value`.

## Customization
- Users can modify the regex patterns in the Python script to suit their specific data extraction needs.
- Modify the `sequences` list to filter out unwanted URLs.

## Troubleshooting
- If the bookmarklet does not work, ensure JavaScript is enabled in your browser.
- For the Python script, check if all required libraries are installed and the file paths are correct.

