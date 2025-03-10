# web_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_headings(url):
    """
    Scrapes the headings (h1, h2, h3) from the given URL.
    
    Args:
        url (str): The URL of the webpage to scrape.
    
    Returns:
        dict: A dictionary with keys 'h1', 'h2', and 'h3' containing lists of heading texts.
    """
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    headings = {
        "h1": [tag.get_text(strip=True) for tag in soup.find_all("h1")],
        "h2": [tag.get_text(strip=True) for tag in soup.find_all("h2")],
        "h3": [tag.get_text(strip=True) for tag in soup.find_all("h3")]
    }
    return headings

if __name__ == "__main__":
    url = "https://www.example.com"
    headings = scrape_headings(url)
    print("Headings found:", headings)
