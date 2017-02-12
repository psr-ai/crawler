from html_lib import HtmlLib


class Scraper:

    def __init__(self):
        self.output = []
        self.html_lib = HtmlLib()

    def scrape(self, page_source, new_page=False):
        self.output += self.html_lib.elements_attribute_map(page_source)
