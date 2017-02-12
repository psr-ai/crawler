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

        concatenated_output = []
        for result in self.output:
            concatenated_output += result
        print len(concatenated_output)
        all_keys = []
        result_keys = [result.keys() for result in concatenated_output]

        for result_key in result_keys:
            all_keys += result_key

        for result in concatenated_output:
            for key in all_keys:
                if key not in result:
                    result[key] = ''

        for output in concatenated_output:

            print output
