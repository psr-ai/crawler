from bs4 import BeautifulSoup, Comment
from lxml import etree
from math_lib import standard_deviation, ljust, transpose, mean


def most_relevant_element(page_source):

    clean_page_source = str(clean_soup(page_source))
    # Page Root
    page_source_root = form_root(clean_page_source)

    # Element tree
    element_tree = etree.ElementTree(page_source_root)

    xpaths_and_children = []
    for e in page_source_root.iter():
        xpaths_and_children.append((element_tree.getelementpath(e), e.getchildren()))

    # sorting xpaths in descending order on number of children
    xpaths_and_children = sorted(xpaths_and_children, key=lambda xpath_and_children: len(xpath_and_children[1]), reverse=True)

    return element_tree.find(most_relevant_dom(xpaths_and_children))


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
                padded_sorted_distributions.append(ljust(sorted_distribution, matrix_length, -10))

            children_matrix_distributions.append((distribution[0], padded_sorted_distributions))

    # Assuming that such elements are having more than 10 children recursively
    children_matrix_distributions = [children_matrix_distribution for children_matrix_distribution in children_matrix_distributions if len(children_matrix_distribution[1][0]) > 10]

    transposed_children_distributions = [(e[0], transpose(e[1]).tolist()) for e in children_matrix_distributions]

    sd_distributions = []
    for matrix_distribution in transposed_children_distributions:
        sd_distributions.append((matrix_distribution[0], [standard_deviation(count_distribution) for count_distribution in matrix_distribution[1]]))

    mean_sd_distributions = [(sd_distribution[0], mean(sd_distribution[1])) for sd_distribution in sd_distributions if mean(sd_distribution[1]) > 0]

    for mean_sd_distribution in mean_sd_distributions:
        if mean_sd_distribution[1] < 2.5:
            return mean_sd_distribution[0]

    return None


# Takes page source as the input, returns beautiful soup without script tags and comments
def clean_soup(content):
    soup = BeautifulSoup(content, 'html.parser')
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    [comment.extract() for comment in comments]
    [s.extract() for s in soup('script')]
    return soup


# Takes the lxml tree and xpath as input, returns list of dom elements found
def fetch_dom_by_xpath(tree, xpath):
    elements = tree.xpath(xpath)
    return elements


def nodes_and_text(root):
    root_name = root.get('class') + " " + root.get('id') if root.get('class') and root.get('id') else root.get('class') if root.get('class') else root.get('id') if root.get('id') else 'None'
    output = {root_name: " ".join(root.itertext())}
    if len(root.getchildren()) > 0:
        for child in root.iterchildren():
            child_nodes_and_text = nodes_and_text(child)
            for key, value in child_nodes_and_text.iteritems():
                output[root_name + " " + key] = value

    return output
    # for child in root.iter():
    #     child_text = ''
    #     for text in root.textiter():
    #         child_text += text


def elements_attribute_map(page_source):
    wrapper = most_relevant_element(page_source)

    for elem in wrapper:
        print nodes_and_text(elem)
