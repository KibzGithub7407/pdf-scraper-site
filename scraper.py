import requests
from bs4 import BeautifulSoup
import json

# 🔗 Replace this with any website you want to scrape
TARGET_URL = 'https://example.com'

# 📁 Output file path
OUTPUT_PATH = 'data/pdfs.json'

def scrape_pdfs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = []

    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.pdf'):
            full_url = requests.compat.urljoin(url, href)
            pdf_links.append({
                'title': link.text.strip() or 'Untitled PDF',
                'url': full_url
            })

    return pdf_links

def save_to_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    pdfs = scrape_pdfs(TARGET_URL)
    save_to_json(pdfs, OUTPUT_PATH)
    print(f"✅ Scraped {len(pdfs)} PDFs and saved to {OUTPUT_PATH}")
