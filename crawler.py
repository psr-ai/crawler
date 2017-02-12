import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def single_page_source(url):
    driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + '/dependencies/chromedriver')
    driver.get(url)
    return driver.page_source


def auto_crawl(url, scrape):

    driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + '/dependencies/chromedriver')
    driver_wait = WebDriverWait(driver, 5)
    driver.get(url)

    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    match = False

    while match is False:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        try:
            driver_wait.until(lambda drv: driver.execute_script("return document.documentElement.scrollHeight;") > last_page_height)
        except TimeoutException:
            print "Cannot scroll down more"
            print "Checking if there is pagination"

            next_buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Next')]") + driver.find_elements_by_xpath("//*[contains(text(), 'NEXT')]")

            if next_buttons:
                print "Clicking next button"
                print len(next_buttons)
                print next_buttons[0].get_attribute("xpath")
                ActionChains(driver).click(next_buttons[0]).perform()





            match = True

        if not match:

            last_page_height = driver.execute_script("return document.documentElement.scrollHeight;")


# auto_crawl("http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphone")