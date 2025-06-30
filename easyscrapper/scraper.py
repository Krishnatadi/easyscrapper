import requests
import re
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class WebScraper:
    def __init__(self, url, user_agent=None):
        self.url = url
        self.user_agent = user_agent or "Mozilla/5.0"
        self.content = None
        self.soup = None
        self.title = None

    def fetch_content(self):
        headers = {'User-Agent': self.user_agent}
        try:
            response = requests.get(self.url, headers=headers, timeout=10)
            response.raise_for_status()
            self.content = response.text
            self.soup = BeautifulSoup(self.content, 'html.parser')
            self.title = self.extract_title()
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")

    def get_raw_content(self):
        if self.content is None:
            raise ValueError("Content is empty. Please fetch the content first.")
        return self.content

    def extract_title(self):
        if not self.soup:
            return ''
        title_tag = self.soup.find('title')
        return title_tag.text.strip() if title_tag else ''

    def extract_custom_tags(self, tags):
        if self.soup is None:
            raise ValueError("Soup is empty. Fetch content first.")
        result = {}
        for tag in tags:
            result[tag] = [elem.get_text(strip=True) for elem in self.soup.find_all(tag)]
        return result

    def extract_links(self):
        if self.soup is None:
            raise ValueError("Soup is empty. Fetch content first.")
        links = set()
        for a in self.soup.find_all('a', href=True):
            links.add(urljoin(self.url, a['href']))
        return list(links)

    def extract_emails(self):
        if self.content is None:
            raise ValueError("Content is empty. Please fetch content first.")
        emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", self.content))
        mailtos = [a['href'][7:] for a in self.soup.find_all('a', href=True) if a['href'].startswith('mailto:')]
        return list(emails.union(mailtos))

    def extract_images(self):
        if self.soup is None:
            raise ValueError("Soup is empty. Fetch content first.")
        images = []

        for img in self.soup.find_all('img'):
            src = img.get('src')
            if src:
                images.append({'src': urljoin(self.url, src), 'alt': img.get('alt', '')})

        href_imgs = re.findall(r'href=["\'](.*?\.(?:jpg|jpeg|png|gif|svg|webp))["\']', self.content, re.IGNORECASE)
        style_imgs = re.findall(r'url\(["\']?(.*?\.(?:jpg|jpeg|png|gif|svg|webp))["\']?\)', self.content, re.IGNORECASE)

        existing = {img['src'] for img in images}
        for img_url in href_imgs + style_imgs:
            full_url = urljoin(self.url, img_url)
            if full_url not in existing:
                images.append({'src': full_url, 'alt': 'background'})
                existing.add(full_url)

        return images

    def extract_plain_text(self):
        if self.soup is None:
            raise ValueError("Soup is empty. Fetch content first.")
        return self.soup.get_text(separator=' ', strip=True)

    def chunk_plain_text(self, text, max_words=100):
        """Splits plain text into chunks of max_words each using basic logic (no NLTK)."""
        words = text.split()
        chunks = []
        for i in range(0, len(words), max_words):
            chunk = " ".join(words[i:i + max_words])
            if chunk.strip():
                chunks.append(chunk)
        return chunks

    def chunk_provided_text(self, text, max_words=100):
        """User can provide custom text to chunk."""
        return self.chunk_plain_text(text, max_words)

    def scrape_all(self, tags=None, plain_text=False, rag_format=False):
        tags = tags or ['h1', 'h2', 'p']
        if self.soup is None:
            raise ValueError("Soup is empty. Fetch content first.")

        tag_data = self.extract_custom_tags(tags)
        plain = self.extract_plain_text() if plain_text or rag_format else None

        if rag_format:
            chunks = self.chunk_plain_text(plain)
            return {
                'url': self.url,
                'title': self.title,
                'rag_chunks': [{'url': self.url, 'title': self.title, 'text': chunk} for chunk in chunks],
                'plain_text': plain
            }

        return {
            'url': self.url,
            'title': self.title,
            'custom_tags': tag_data,
            'emails': self.extract_emails(),
            'links': self.extract_links(),
            'images': self.extract_images(),
            'plain_text': plain if plain_text else None
        }
    
    def extract_meta_tags(self):
        """Extracts meta tags such as title, description, keywords, and Open Graph data."""
        if self.soup is None:
            raise ValueError("Soup is empty. Fetch content first.")
        
        meta_data = {}
        for tag in self.soup.find_all('meta'):
            name = tag.get('name') or tag.get('property')
            content = tag.get('content')
            if name and content:
                meta_data[name.strip()] = content.strip()
        return meta_data

    def get_canonical_url(self):
        """
        Extracts the canonical URL from <link rel="canonical"> if available.
        Useful for SEO and content deduplication.
        """
        if self.soup is None:
            raise ValueError("Soup is empty. Fetch content first.")
        link_tag = self.soup.find('link', rel='canonical')
        return link_tag['href'] if link_tag and link_tag.has_attr('href') else None


    def save_to_file(self, data, filename='easyscrapper_data.txt'):
        if filename.endswith('.json'):
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"JSON data saved to {filename}")
        else:
            # If data is not string (like a dict), convert it
            if not isinstance(data, str):
                data = str(data)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(data)
            print(f"Text data saved to {filename}")
