# Soil Health Data Scraper

## Overview

This Python script is designed to scrape soil health data from the [Soil Health Portal](https://soilhealth.dac.gov.in/piechart) website. It automates the process of downloading CSV files containing soil health data for different states and districts in India.

## Features

- Scrapes soil health data for different states and districts in India.
- Downloads CSV files containing soil health data.
- Organizes downloaded files into subdirectories based on state names.
- Combines CSV files for each state into a single combined CSV file.

## Requirements

- Python 3.x
- Selenium
- Pandas
- Chrome WebDriver
- Google Chrome browser

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install required Python packages using pip:
3. Download the Chrome WebDriver for your Chrome browser version from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your system PATH.

## Usage

1. Run the `scrape_data.py` script.
2. The script will open the Soil Health Portal website and start scraping data.
3. Downloaded CSV files will be saved in the `prati` directory.
4. Combined CSV files for each state will also be saved in the respective subdirectories.

## Notes

- Ensure that you have a stable internet connection while running the script.
- The script may take some time to complete depending on the number of states and districts being scraped.
