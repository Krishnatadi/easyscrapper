# easyscrapper/scraper.py

import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url, user_agent=None):
        self.url = url
        self.content = None
        self.user_agent = user_agent or "Mozilla/5.0"

    def fetch_content(self):
        """Fetches the HTML content from the URL."""
        headers = {'User-Agent': self.user_agent}
        try:
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            self.content = response.text
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")

    def get_raw_content(self):
        """Returns the entire scraped content without parsing."""
        if self.content is None:
            raise ValueError("Content is empty. Please fetch the content first.")
        return self.content

    def parse_content(self):
        """Returns parsed data (headings, paragraphs, links) as a single string."""
        if self.content is None:
            raise ValueError("Content is empty. Please fetch the content first.")

        soup = BeautifulSoup(self.content, 'lxml')
        parsed_data = self.extract_all_data(soup)
        return parsed_data

    def extract_all_data(self, soup):
        """Extracts all text content, including headings and paragraphs, as a single string."""
        content = []
        
        # Extract headings
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            content.append(heading.get_text(strip=True))
        
        # Extract paragraphs
        for paragraph in soup.find_all('p'):
            content.append(paragraph.get_text(strip=True))
        
        # Join all extracted content into a single string
        return '\n\n'.join(content)

    def extract_links(self, soup):
        """Extracts all links (URLs) from the HTML content."""
        return [a['href'] for a in soup.find_all('a', href=True)]

    def save_to_file(self, data, filename='easyscrapper_data.txt'):
        """Saves the provided data to a text file."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f"Data saved to {filename}.")

