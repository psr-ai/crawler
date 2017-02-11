from bs4 import BeautifulSoup, Comment


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