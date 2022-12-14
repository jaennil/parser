import get_links
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def main():
    browser = init_headless_browser()
    school_numbers = get_school_numbers()
    for number in school_numbers:
        links = get_links.get_links(number, browser)
        for link in links:
            text = get_page_text(link, browser)
            print(f"{text = }")


def get_school_numbers():
    result = []
    dataset = pd.read_excel("dataset.xlsx")
    school_numbers = dataset["nomer"].tolist()
    for number in school_numbers:
        if any(char.isdigit() for char in number):
            result.append(int(number))
    return result


def init_headless_browser():
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    return browser


def get_page_text(url, browser):
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


if __name__ == "__main__":
    main()
