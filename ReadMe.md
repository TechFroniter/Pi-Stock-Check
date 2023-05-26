# Raspberry Pi Availability Checker

This Python script is intended to help you find available Raspberry Pi units for purchase. It does so by scraping multiple websites to check if they have Raspberry Pi units in stock, and if so, it provides the relevant link.

## How it works

This script leverages Python's multithreading capabilities to speed up the web scraping process by checking multiple websites concurrently. Currently, the websites being scraped include Adafruit, Pi Shop, and Vilros.

## Requirements

- Python 3.6+
- `requests` Python module
- `beautifulsoup4` Python module
- `json` Python module
- `threading` Python module

## Usage

1. Clone this repository and navigate to its directory.

2. Install the necessary Python modules. You can do this by running `pip install -r requirements.txt` (Please note you must have pip installed).

3. Add or remove URLs in the urls.json file. The structure should follow: 
    ```
    {
        "adafruit": ["URL1", "URL2", ...],
        "pi_shop": ["URL1", "URL2", ...],
        "vilros": ["URL1", "URL2", ...]
    }
    ```
    Please note, the URL should be of the product page for a Raspberry Pi product. 

4. Run the script by typing `python run.py` in your terminal.

## Disclaimer

Please note that this script is intended for personal use only. Be sure to check each website's terms of service before using this script, as some sites may not allow this type of web scraping.
