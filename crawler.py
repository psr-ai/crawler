import os, StringIO
from selenium import webdriver
from lxml import etree
from html_lib import clean_soup
from math_lib import standard_deviation, ljust, transpose


def crawl():
    driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + '/dependencies/chromedriver')
    driver.get("http://www.amazon.in/s/ref=nb_sb_ss_i_4_6?url=search-alias%3Daps&field-keywords=iphone+7&sprefix=iphone%2Caps%2C316&crid=3JK7HCRRBBHHS")
    page_source = driver.page_source
    driver.quit()

    clean_page_source = str(clean_soup(page_source))
    # Page Root
    page_source_root = form_root(clean_page_source)

    # Element tree
    element_tree = etree.ElementTree(page_source_root)

    xpaths_and_children = []
    for e in page_source_root.iter():
        xpaths_and_children.append((element_tree.getpath(e), e.getchildren()))

    # sorting xpaths in descending order on number of children
    xpaths_and_children = sorted(xpaths_and_children, key=lambda xpath_and_children: len(xpath_and_children[1]), reverse=True)

    most_relevant_dom(xpaths_and_children)


# Takes source without comments and returns the lxml tree for the same
def form_root(source):
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(source, parser)
    return root


def most_relevant_dom(elements):

    distributions = []
    total_distributions = []

    # Looping on all found child elements of the source
    for element in elements:
        distribution = []
        total_distribution = []
        for child_element in element[1]:
            total_children_recursively = 0
            children_at_same_level_counts = []
            for e in child_element.iter():
                children_at_same_level_counts.append(len(e.getchildren()))
                total_children_recursively += 1

            distribution.append(children_at_same_level_counts)
            total_distribution.append(total_children_recursively)

        distributions.append((element[0], distribution))
        total_distributions.append((element[0], len(element[1]), total_distribution))

    # each distribution is recursive children count distribution for each child in parent element
    children_matrix_distributions = []
    for distribution in distributions:

        sorted_distributions = sorted(distribution[1], key=lambda each_distribution: len(each_distribution), reverse=True)

        if len(sorted_distributions) > 0:

            matrix_length = len(sorted_distributions[0])
            padded_sorted_distributions = []
            for sorted_distribution in sorted_distributions:
                padded_sorted_distributions.append(ljust(sorted_distribution, matrix_length, -1))

            children_matrix_distributions.append((distribution[0], padded_sorted_distributions))

    transposed_children_distributions = [(e[0], transpose(e[1]).tolist()) for e in children_matrix_distributions]

    sd_distributions = []
    for matrix_distribution in transposed_children_distributions:
        sd_distributions.append([standard_deviation(count_distribution) for count_distribution in matrix_distribution[1]])

    print sd_distributions[2]
    print transposed_children_distributions[2][1]







# def child_freq_counts_by_level(elements, distribution=[]):
#     this_level_distribution = []
#     next_level_elements = []
#     for child_element in elements:
#         if child_element.findall("*").count > 0:
#             this_level_distribution.append(child_element.findall("*").count)
#             next_level_elements.push()


crawl()