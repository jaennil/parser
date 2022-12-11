import html2text
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

api_key = "AIzaSyCVVCTXzFHAK8jA1-jFYsbKZqePMFs63n8"
options = Options()
options.headless = True
url = 'https://sch2114uz.mskobr.ru'
browser = webdriver.Firefox(options=options)
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
text = html2text.html2text(soup.prettify())
print(text)
print("Новостии" in text)
print("Новости" in text)
browser.quit()
