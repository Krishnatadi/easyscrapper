import argparse
from easyscrapper.scraper import WebScraper
import json

def main():
    parser = argparse.ArgumentParser(
        description="EasyScrapper is a lightweight and flexible web scraping utility designed to extract structured and unstructured content from any public web page. It helps developers and AI engineers effortlessly retrieve"
    )

    parser.add_argument("url", help="URL of the website to scrape")

    parser.add_argument("--tags", "-t", nargs="+", help="HTML tags to extract (e.g. h1 p div)")
    
    parser.add_argument("--plain", "-p", action="store_true", help="Extract all visible plain text from the page")
    parser.add_argument("--emails", "-e", action="store_true", help="Extract email addresses")
    parser.add_argument("--links", "-l", action="store_true", help="Extract all links")
    parser.add_argument("--images", "-i", action="store_true", help="Extract image URLs and alt text")
    parser.add_argument("--rag", "-r", action="store_true", help="Return plain text chunks for RAG/AI use")
    parser.add_argument("--meta", "-m", action="store_true", help="Extract meta tags")
    parser.add_argument("--canonical", "-c", action="store_true", help="Extract canonical URL")
    parser.add_argument("--json", action="store_true", help="Output result in JSON format")
    parser.add_argument("--output", "-o", help="Save result to a file (e.g. output.json or output.txt)")

    args = parser.parse_args()

    scraper = WebScraper(args.url)
    scraper.fetch_content()

    result = {
        "url": scraper.url,
        "title": scraper.title,
    }

    # HTML Tag content
    if args.tags:
        result["custom_tags"] = scraper.extract_custom_tags(args.tags)

    # Plain text and RAG chunks
    if args.plain or args.rag:
        plain = scraper.extract_plain_text()
        result["plain_text"] = plain
        if args.rag:
            result["rag_chunks"] = scraper.chunk_plain_text(plain)

    # Emails, Links, Images
    if args.emails:
        result["emails"] = scraper.extract_emails()

    if args.links:
        result["links"] = scraper.extract_links()

    if args.images:
        result["images"] = scraper.extract_images()

    if args.meta:
        result["meta_tags"] = scraper.extract_meta_tags()

    if args.canonical:
        result["canonical_url"] = scraper.get_canonical_url()

    # Output File
    if args.output:
        scraper.save_to_file(result, args.output)
    else:
        if args.json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(result)

if __name__ == "__main__":
    main()
