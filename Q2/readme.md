# Foreign Tourism Data Processing

## Overview

This Python script is designed to extract and process foreign tourism data from a PDF file containing statistics for the year 2022. It uses the `tabula` library to extract tables from specified pages of the PDF file and then combines the extracted data into a single CSV file.

## Features

- Extracts tables from specified pages of a PDF file.
- Processes foreign tourism data from the extracted tables.
- Combines data from different page groups into a single DataFrame.
- Saves the consolidated data to a CSV file.

## Requirements

- Python 3.x
- `tabula` library
- `pandas` library

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install the required Python libraries using pip:

## Usage

1. Place the PDF file containing foreign tourism data (`India Tourism Statistics English 2022.pdf`) in the same directory as the script.
2. Run the `main()` function in the script.
3. The script will process the data and save the consolidated data to a CSV file named `output.csv` in the same directory.

## Notes

- Ensure that you have a stable internet connection while running the script.
- Make sure the `India Tourism Statistics English 2022.pdf` file is correctly located in the script's directory.
