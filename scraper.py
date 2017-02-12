from html_lib import HtmlLib


class Scraper:

    def __init__(self):
        self.output = []
        self.html_lib = HtmlLib()
        self.current_page_index = -1
        self.total_items = sum([len(page_items) for page_items in self.output])

    def scrape(self, page_source, new_page=False):

        if new_page or self.current_page_index is -1:
            self.current_page_index += 1
            self.output.append([])

        self.output[self.current_page_index] += self.html_lib.elements_attribute_map(page_source, from_index=len(self.output[self.current_page_index]))

        self.total_items = sum([len(page_items) for page_items in self.output])

    def process_output(self):

        for output_per_page in self.output:

            for output in output_per_page:
                print output
