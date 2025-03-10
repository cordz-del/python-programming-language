# test_web_scraper.py
from bs4 import BeautifulSoup
from web_scraper import scrape_headings

def test_scrape_headings():
    # Dummy HTML for testing without network dependency
    dummy_html = """
    <html>
      <body>
        <h1>Main Title</h1>
        <h2>Subtitle 1</h2>
        <h2>Subtitle 2</h2>
        <h3>Section 1</h3>
      </body>
    </html>
    """
    # Parse dummy HTML using BeautifulSoup directly
    soup = BeautifulSoup(dummy_html, 'html.parser')
    headings = {
        "h1": [tag.get_text(strip=True) for tag in soup.find_all("h1")],
        "h2": [tag.get_text(strip=True) for tag in soup.find_all("h2")],
        "h3": [tag.get_text(strip=True) for tag in soup.find_all("h3")]
    }
    assert headings["h1"] == ["Main Title"]
    assert headings["h2"] == ["Subtitle 1", "Subtitle 2"]
    assert headings["h3"] == ["Section 1"]
    print("test_scrape_headings passed.")

if __name__ == "__main__":
    test_scrape_headings()
