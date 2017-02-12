from crawler import single_page_source
from scraper import Scraper


url = "http://www.amazon.in/s/ref=nb_sb_ss_i_4_6?url=search-alias%3Daps&field-keywords=iphone+7&sprefix=iphone%2Caps%2C284&crid=ZNKHKONNIHBA"

scraper = Scraper()
scraper.scrape(single_page_source(url))
print len(scraper.output)

