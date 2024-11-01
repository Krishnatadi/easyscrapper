# EasyScrapper

**EasyScrapper** is a simple and effective Python package for web scraping. It allows you to fetch and extract data from any website without the hassle of complex parsing logic. This package is designed for developers who need quick and reliable web scraping solutions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [WebScraper Class Overview](#WebScraper-Class-Overview)
- [Usage](#usage)
  - [Fetching Raw Content]
  - [Providing Parsed Data]
  - [Extracting URLs]
  - [Saving Data to a Text File]
- [Use Cases](#Use-Cases)

## Features

- **Fetch Raw Content**: Get the full HTML content from any webpage.
- **Parse Content**: Extract headings and paragraphs as a single string without formatting.
- **User-Friendly**: EasyScrapper is designed to be intuitive and straightforward, making it perfect for both beginners and experienced developers.
- **Flexible**: With functionalities to extract raw content, parsed data, and URLs, it caters to various scraping needs.
- **Data Preservation**: Save scraped data to text files for future analysis or reporting.


## Installation

To install the EasyScrapper package, you can use `pip`. Run the following command:

```bash
pip install easyscrapper
```


## WebScraper Class Overview

| Function              | Description                                                                 | Example                                                       |
|-----------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------|
| `__init__(url, user_agent=None)` | Initializes the `WebScraper` instance with a URL and optional user agent. | `scraper = WebScraper("https://example.com")`              |
| `fetch_content()`     | Fetches the HTML content from the specified URL.                          | `scraper.fetch_content()`                                    |
| `get_raw_content()`   | Returns the entire scraped content without parsing.                       | `raw_content = scraper.get_raw_content()`                    |
| `parse_content()`     | Parses the HTML content and returns extracted headings and paragraphs.     | `parsed_data = scraper.parse_content()`                      |
| `extract_all_data(soup)` | Extracts all text content (headings and paragraphs) from the parsed HTML. | `content = scraper.extract_all_data(soup)`                  |
| `extract_links(soup)` | Extracts all links (URLs) from the HTML content.                         | `links = scraper.extract_links(soup)`                        |
| `save_to_file(data, filename='scraped_data.txt')` | Saves the provided data to a text file.                               | `scraper.save_to_file(parsed_data, 'output.txt')`          |



## Usage
### 1. Fetching Raw Content
This functionality retrieves the complete HTML content from a specified URL. You can also limit the output to the first 500 characters for a quick preview.
```python
from easyscrapper.scraper import WebScraper

# Specify the URL to scrape
url = 'https://example.com'  # Replace with your target URL

# Initialize the WebScraper
scraper = WebScraper(url)

# Fetch content from the URL
scraper.fetch_content()

# Get and print the raw content
raw_content = scraper.get_raw_content()
print("Raw Content:")
print(raw_content)  # Print the entire raw content
# Output: Entire HTML content of the webpage

# Get and print the first 500 characters of the raw content
print("\nFirst 500 Characters of Raw Content:")
print(raw_content[:500])  # Print the first 500 characters
# Output: (First 500 characters of the HTML content)
```


### 2. Providing Parsed Data
This functionality extracts headings and paragraphs from the fetched content, returning them as a single string without any HTML tags.
The `parse_content()` method processes the raw HTML to extract meaningful text, ignoring tags and formatting. This makes it easy for users to get a clean summary of the content.
```python
# Get parsed data from the fetched content
parsed_data = scraper.parse_content()
print("Parsed Data (Headings and Paragraphs):")
print(parsed_data)  # Output: Combined text of headings and paragraphs without formatting
```


### 3. Extracting URLs
This functionality retrieves all hyperlinks found on the webpage.
The `extract_links()` method identifies and returns all anchor tags (<a>) present in the HTML, providing users with a list of links for further exploration.
```python
# Extract URLs from the fetched content
urls = scraper.extract_links()
print("Extracted URLs:")
print(urls)  # Output: List of URLs found on the webpage
```


### 4. Saving Data to a Text File
This functionality allows users to save either raw or parsed data into text files for later use.
The `save_to_file()` method allows users to specify the content they wish to save and the desired filename. This feature is useful for archiving or further processing of scraped data.
```python
# Save raw content to a text file
scraper.save_to_file(scraper.get_raw_content(), 'easyscrapper_data.txt')
print("Raw content saved successfully to 'easyscrapper_data.txt'.")

# Save parsed data to a text file
parsed_data = scraper.parse_content()
scraper.save_to_file(parsed_data, 'parsed_data.txt')
print("Parsed data saved successfully to 'parsed_data.txt'.")
# Output: Confirmation messages indicating successful saving of files
```


## Use Cases

EasyScrapper is versatile and serves a wide range of users, including researchers, analysts, developers, and marketers. Here are some common use cases:

- **Research**: Easily gather information from multiple web pages for academic or market research. Many students and professionals rely on it to compile data for reports and studies.

- **Data Analysis**: Collect data points from various websites to analyze trends and patterns. Analysts utilize EasyScrapper to extract quantitative and qualitative data for deeper insights.

- **Content Aggregation**: Scrape content from different sources and compile it into a single location for easy access. Content creators and curators use it to gather relevant articles, blogs, and news for their audiences.

- **SEO Monitoring**: Extract meta tags and other SEO-related information to monitor website performance. Marketers leverage this functionality to assess competitors and optimize their own content.

- **E-commerce Price Tracking**: Monitor product prices across multiple e-commerce platforms to find the best deals. Shoppers and businesses use this feature for competitive pricing analysis.

- **Job Listings Aggregation**: Collect job postings from various job boards to create a centralized platform for job seekers. Recruiters and job seekers benefit from the aggregated data for better visibility.

With its user-friendly design and robust capabilities, EasyScrapper is trusted by a growing community of users who are enhancing their web scraping efforts across various fields.


## Join the Community

If you find EasyScrapper useful, consider giving it a star on GitHub and sharing it with others. Your support helps us improve and expand our tool!

