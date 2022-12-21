import url2soup
from bs4 import Tag


def get(school_name, browser, amount=5):
    """get all links related to a school number from google search"""
    url = f"https://www.google.com/search?q=Школа+{school_name}+о+нас"
    soup = url2soup.get(url, browser)
    search = type_fix(soup.find("div", {"id": "search"}))
    links = search.find_all("a")
    proper_links = []
    for link in links:
        href = link.get("href")
        if not href:
            continue
        if not href.startswith("https"):
            continue
        if href not in proper_links:
            proper_links.append(href)
            if len(proper_links) == amount:
                return proper_links
    print(f"failed to get {amount} links. got {len(proper_links)}")
    return proper_links

def type_fix(element) -> Tag:
    return element
