from bs4 import BeautifulSoup

def get(url: str, browser) -> BeautifulSoup:
    """Get a BeautifulSoup object from a URL."""
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    return soup
