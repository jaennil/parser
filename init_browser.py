from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def headless():
    """initialize invisible browser for parsing"""
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    return browser

def default():
    """initialize visible browser for debugging"""
    browser = webdriver.Firefox()
    return browser
