import url2soup


def get_page_text(url, browser):
    soup = url2soup.get(url, browser)
    return soup.get_text()
