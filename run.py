from crawler import single_page_source
from html_lib import elements_attribute_map


url = "http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphone"
elements_attribute_map(single_page_source(url))

