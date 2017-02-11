import os
from selenium import webdriver


def single_page_source(url):
    driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + '/dependencies/chromedriver')
    driver.get(url)
    return driver.page_source
