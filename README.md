# EasyScrapper

**EasyScrapper** is a simple yet powerful Python package that helps you scrape structured content, plain text, emails, links, images, and generate RAG-ready chunks from any webpage. Built on requests and BeautifulSoup, it is easy to use and ready for integration with AI/NLP workflows.


## Installation

To install the EasyScrapper package, you can use `pip`. Run the following command:

```bash
pip install easyscrapper
```


## Features

| Feature                | Description |
|------------------------|-------------|
| URL Fetching           | Fetches and parses HTML content from any public webpage. |
| Custom Tag Extraction  | Extracts content from specified HTML tags like h1, h2, p, etc. |
| Link Extraction        | Gathers all valid hyperlinks from anchor tags (`<a href>`). |
| Email Extraction       | Finds email addresses from plain text and mailto: links. |
| Image Extraction       | Extracts images from `<img>`, href, and style attributes including background images. |
| Plain Text Extraction  | Extracts and cleans all text content from the page. |
| RAG Chunking           | Converts plain text into AI-friendly chunks (useful for RAG and vector databases). |
| Save to File           | Saves the scraped result in `.txt` or `.json` formats. |
| Manual Chunking        | Allows users to input their own text and get it chunked for AI applications. |



## Use Cases

| Use Case                   | Description |
|----------------------------|-------------|
| Basic Web Scraping         | Extract headings, paragraphs, links, and other HTML content from any public website. |
| SEO Audits                 | Collect all headings and metadata to analyze page structure and content hierarchy. |
| Email Lead Collection      | Quickly find and extract emails from websites and landing pages. |
| Image Collection           | Gather all image URLs (including hidden ones) for data analysis or machine learning. |
| Plain Text Conversion      | Convert a web page into clean, readable plain text. |
| RAG (Retrieval-Augmented Generation) | Convert scraped or custom text into clean, token-friendly chunks for RAG/LLM ingestion. |
| Data Archiving             | Save scraped data in JSON or TXT format for offline use or long-term storage. |
| Preprocessing for AI       | Prepare web data for indexing into vector stores like Pinecone, FAISS, ChromaDB, etc. |


## WebScraper Class Overview

| Function              | Description                                                                 | Example                                                       |
|-----------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------|
| `__init__(url, user_agent=None)` | Initializes the `WebScraper` instance with a URL and optional user agent. | `scraper = WebScraper("https://www.example.com")`              |
| `fetch_content()`     | Fetches the HTML content from the specified URL.                          | `scraper.fetch_content()`                                    |
| `get_raw_content()`   | Returns the entire scraped content without parsing.                       | `raw_content = scraper.get_raw_content()`                    |
| `parse_content()`     | Parses the HTML content and returns extracted headings and paragraphs.     | `parsed_data = scraper.parse_content()`                      |
| `extract_all_data(soup)` | Extracts all text content (headings and paragraphs) from the parsed HTML. | `content = scraper.extract_all_data(soup)`                  |
| `extract_links(soup)` | Extracts all links (URLs) from the HTML content.                         | `links = scraper.extract_links(soup)`                        |
| `save_to_file(data, filename='scraped_data.txt')` | Saves the provided data to a text file.                               | `scraper.save_to_file(parsed_data, 'output.txt')`          |




## Function Reference

| Function                                | Description                                      |
|-----------------------------------------|--------------------------------------------------|
| `fetch_content()`                       | Loads content from the URL                       |
| `get_raw_content()`                     | Returns the raw HTML                             |
| `extract_title()`                       | Gets the `<title>` of the page                   |
| `extract_custom_tags(tags)`             | Extracts content from specified tags             |
| `extract_links()`                       | Extracts all absolute hyperlinks                 |
| `extract_emails()`                      | Finds emails in the HTML and mailto links        |
| `extract_images()`                      | Finds images from `<img>`, href, style           |
| `extract_plain_text()`                  | Returns the entire plain text of the page        |
| `chunk_plain_text(text, max_words)`     | Chunks plain text into N-word segments           |
| `chunk_provided_text(text, max_words)`  | Same as above, but from user input               |
| `scrape_all(tags, plain_text, rag_format)` | Extracts everything at once                    |
| `save_to_file(data, filename)`          | Saves output to `.txt` or `.json` file           |



## EasyScrapper CLI Options

| Flag            | Alias | Description                                                                 | Example Usage                      |
|------------------|-------|-----------------------------------------------------------------------------|------------------------------------|
| `--tags`         | `-t`  | Extract specified HTML tags (`h1`, `p`, `div`, etc.)                         | `--tags h1 p div`                  |
| `--plain-text`   | `-p`  | Extract full plain visible text                                             | `--plain-text` or `-p`             |
| `--emails`       | `-e`  | Extract all email addresses (inline and `mailto:` links)                    | `--emails` or `-e`                 |
| `--links`        | `-l`  | Extract all hyperlinks (from `<a href>`)                                    | `--links` or `-l`                  |
| `--images`       | `-i`  | Extract all image URLs (including background images in `style`/`href`)      | `--images` or `-i`                 |
| `--rag`          | `-r`  | Extract RAG-style chunks from plain text (for vector DBs or AI pipelines)   | `--rag` or `-r`                    |
| `--output`       | `-o`  | Save the result to a JSON file                                              | `--output data.json` or `-o out.json` |
| `--help`         | `-h`  | Show help message                                                           | `--help` or `-h`                   |





## Usage

### 1. Fetching Raw Content - fetch_content()
Fetches and prepares the HTML content from the given URL. This is required before calling any other function.
```python
from easyscrapper.scraper import WebScraper

# Specify the URL to scrape
url = 'https://www.example.com'  # Replace with your target URL

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

# Get and print the last 500 characters of the raw content
print(raw_content[-500:])  # Print the last 500 characters
# Output: (Last 500 characters of the HTML content)
```


### 2. Fetching Raw Content - get_raw_content()
Returns the raw HTML content (with all tags and markup).
```python
scraper.fetch_content()
html = scraper.get_raw_content()
print(html[:500])  # Print the first 500 characters of raw HTML
```


### 3. Extract Page Title - extract_title()
Retrieve the content of the title tag from the webpage.
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

title = scraper.extract_title()
print("Page Title:", title)
```


### 4. Extract Specific Tags - extract_custom_tags(tags: List[str])
Get only the clean text from selected HTML tags like headings (h1, h2) or paragraphs (p).
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

data = scraper.extract_custom_tags(['h1', 'p'])
print(data)
```


### 5. Extract All Links - extract_links()
Finds and returns all hyperlink URLs ( href="...") as absolute URLs.
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

links = scraper.extract_links()
print("Links found:", links)
```


### 6. Extract Emails - extract_emails()
Detect and extract all email addresses present on the webpage.
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

emails = scraper.extract_emails()
print("Emails:", emails)
```


### 7. Extract Image URLs - extract_images()
Automatically extract all image sources, including those in image tags, links, and styles.
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

images = scraper.extract_images()
for img in images:
    print("Image:", img['src'], "| Alt Text:", img['alt'])
```


### 8. Extract Plain Text - extract_plain_text()
Get the full visible plain text of the webpage, without any HTML tags or scripts.
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

text = scraper.extract_plain_text()
print("Visible Text:", text[:500])
```


### 9. Chunk Extracted Text - chunk_plain_text(text: str, max_words: int = 100)
Split the extracted plain text into smaller chunks (e.g., 100 words each) for use in NLP, AI, or search systems.
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

plain_text = scraper.extract_plain_text()
chunks = scraper.chunk_plain_text(plain_text, max_words=100)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
```


### 10. Chunk Custom Text - chunk_provided_text(text: str, max_words: int = 100)
Split your own text (not scraped) into chunks — useful for preparing content for AI training or search indexing.
```python
scraper = WebScraper('https://www.example.com')

custom_text = "This is a long paragraph that needs to be broken into smaller chunks..."
chunks = scraper.chunk_provided_text(custom_text, max_words=50)

for chunk in chunks:
    print(chunk)
```


### 11. Scrape All Content Together - scrape_all(tags=None, plain_text=True, rag_format=False)
Extract everything in one go - title, text tags, emails, links, images, and full text.
- plain_text=True to extract full text
- rag_format=True to get AI/RAG chunks
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()
# Extract full data with plain text
full_data = scraper.scrape_all(tags=['h1', 'p'], plain_text=True)
print(full_data)
```


### 12. Get RAG-Friendly Chunks - scrape_all(tags=None, plain_text=False, rag_format=True)
Automatically turn plain text into source-linked chunks ready for retrieval-augmented generation (RAG) systems.
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

# Get just RAG-ready text chunks
rag_data = scraper.scrape_all(tags=['p'], rag_format=True)
for chunk in rag_data['rag_chunks']:
    print(chunk)
```

### 13. Save Output to File - save_to_file(data, filename='output.txt')
Save any output (plain text or structured data) to a .txt or .json file.
- .txt for plain text
- .json for structured data
```python
scraper = WebScraper('https://www.example.com')
scraper.fetch_content()

# Save plain text
text = scraper.extract_plain_text()
scraper.save_to_file(text, filename='easyscrapper_output.txt')

# Save full scraped result as JSON
data = scraper.scrape_all(tags=['h1', 'p'], plain_text=True)
scraper.save_to_file(data, filename='easyscrapper_output.json')
```

---

## Example CLI Commands

```bash
# Extract h1, h2, and p tags
easyscrapper https://www.example.com --tags h1 h2 p

# Extract all plain text and save to a JSON file
easyscrapper https://www.example.com --plain --output page.json

# Extract all emails, links, and images
easyscrapper https://www.example.com --emails --links --images

# RAG-style chunked output
easyscrapper https://www.example.com --rag

# Full combo with everything
easyscrapper https://www.example.com -t h1 p -p -e -l -i -r -o full_output.json

```

---

# What Can You Do with EasyScrapper?
Whether you're a developer, researcher, or digital marketer, EasyScrapper helps you pull structured content from websites—fast. Here’s how you can put it to work:

---

## AI & Machine Learning
- **Build NLP Training Sets**: Easily gather clean text from multiple websites to create high-quality datasets.
- **Summarize Content Automatically**: Scrape blog posts or articles and feed them into summarization models.
- **Train Language Models**: Collect multilingual data to train or test language detection and classification systems.

---

## Retrieval-Augmented Generation (RAG)
- **Feed Your Vector DB**: Break down scraped text into chunks for vector embedding with FAISS, Pinecone, etc.
- **Inject Real-Time Context**: Dynamically scrape relevant info and add it to prompts for more accurate LLM outputs.
- **Tap into Web Knowledge**: Let your RAG systems stay up-to-date with live website content.

---

## Web & SEO Analytics
- **Analyze HTML Tags**: Extract headings, paragraphs, and other tags to optimize SEO strategies.
- **Monitor Links**: Find broken or redirected internal and outbound links.
- **Audit Media**: Check images for alt-text, size, and loading performance.

---

## Market Intelligence
- **Track Competitors**: Monitor product pages or blogs for pricing or messaging changes.
- **Spot Trends**: Pull headlines or blog snippets to detect emerging topics.
- **Collect Emails (Ethically!)**: Scrape emails for outreach—just be sure to follow privacy laws.

---

## Legal & Compliance
- **Compare Legal Docs**: Scrape privacy policies or terms of service for quick analysis or summaries.
- **Run Compliance Checks**: Make sure required disclaimers or clauses exist on client or partner sites.

---

## News Aggregation
- **Chunk the News**: Break long articles into readable bits for newsletters or summaries.
- **Detect Events in Real-Time**: Pull headlines to power event detection systems or alerts.

---

## Developer Utilities
- **Generate Realistic Test Data**: Use real-world HTML for unit or integration tests.
- **Build Your Own Crawler**: Combine EasyScrapper with your custom logic to scrape multiple pages or domains.

---

## Documentation Mining
- **Scrape Technical Docs**: Pull changelogs, API references, or developer guides for indexing or embedding.
- **Parse Open Source Projects**: Extract structured info from READMEs or API docs.

---

## E-commerce Data Extraction
- **Mine Product Info**: Scrape titles, prices, descriptions, and more for research or comparison.
- **Grab Images & Metadata**: Collect all product-related images and details automatically.

---

## Research & Academia
- **Create Custom Web Datasets**: Pull content from niche sites to build your own research corpus.
- **Explore Search & Retrieval**: Use real-world data for experiments in search relevance, ranking, and more.


## Join the Community

If you find EasyScrapper useful, consider giving it a star on GitHub and sharing it with others. Your support helps us improve and expand our tool!


## Issues and Feedback
For issues, feedback, and feature requests, please open an issue on our [GitHub Issues page](http://github.com/krishnatadi/easyscrapper/issues). We actively monitor and respond to community feedback.
