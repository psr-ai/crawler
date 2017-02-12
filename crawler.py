import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from scraper import Scraper


class Crawler:

    def __init__(self, total_items_to_scrape=240):
        self.driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + '/dependencies/chromedriver')
        self.driver_wait = WebDriverWait(self.driver, 5)
        self.scraper = Scraper()
        self.total_items_to_scrape = total_items_to_scrape

    def auto_crawl(self, url):

        self.driver.get(url)
        last_page_height = 0
        match = False
        if_new_page = True
        while match is False:
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            try:
                self.driver_wait.until(lambda drv: self.driver.execute_script("return document.documentElement.scrollHeight;") > last_page_height)
                self.scraper.scrape(self.driver.page_source, new_page=if_new_page)
                if_new_page = False
                if self.scraper.total_items > self.total_items_to_scrape:
                    match = True
            except TimeoutException:
                print "Cannot scroll down more"
                print "Checking if there is pagination"

                next_buttons = self.driver.find_elements_by_xpath("//*[contains(text(), 'Next')]")

                if next_buttons:
                    print "Clicking next button"
                    self.driver.execute_script("arguments[0].click();", next_buttons[0])
                    if_new_page = True

                else:
                    print "Cannot find pagination. Exiting..."
                    match = False

            if not match:

                if if_new_page:
                    last_page_height = 0
                else:
                    last_page_height = self.driver.execute_script("return document.documentElement.scrollHeight;")

            else:

                print "Total items scraped. Exiting..."





# auto_crawl("http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphone")