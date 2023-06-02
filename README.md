# Image Web Scraping with Python

This repository contains two Python scripts for web scraping images from different sources. The first script scrapes images from Google Images, while the second script scrapes images from swisswatchexpo.com.

## Google Images Web Scraper

The `google_images_scraper.py` script uses the Selenium library to automate the process of scrolling through Google Images and extracting image URLs. It then downloads the images using the requests library and saves them locally. Here's how to use it:

1. Install the necessary dependencies by running `pip install selenium requests Pillow`.
2. Make sure you have Chrome installed on your machine.
3. Download the ChromeDriver executable and provide its path in the `PATH` variable at the beginning of the script.
4. Customize the search query URL in the `url` variable to scrape images for your desired query.
5. Run the script, and it will download the specified number of images to the `rolex_images` directory.

## SwissWatchExpo Image Scraper

The `swisswatchexpo_scraper.py` script uses the requests library and regular expressions to scrape images from swisswatchexpo.com. It fetches the HTML content of the webpage, finds all image URLs that end with ".jpg," and downloads them locally. Here's how to use it:

1. Install the necessary dependency by running `pip install requests`.
2. Customize the `url` variable with the desired URL of the webpage you want to scrape images from.
3. Run the script, and it will download the images to the current directory with file names like "rolex_daydate_swisswatchexpo_pageX.jpg," where X is the page number.

Note: Remember to comply with the terms of service and legal requirements of the websites you are scraping.

