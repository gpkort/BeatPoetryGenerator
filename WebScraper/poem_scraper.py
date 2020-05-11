"""

This module provides the functionality to scrape the website
http://famouspoetsandpoems.com to get lines of a specified poet. The
website has many poems for many poets. The user will have to know the
specific URL for a poet (see Examples). The methods in the utility assume
a this structure:

Poet
|_______Poem
|_______Poem
|_______Poem etc...

Once the poet is found the scraper has a utility to return an array of
poem urls. These can be used to to call another method to get an array
of lines from the poem. The lines can be pretty ugly so there exists a
method to clean up some of the known formatting.

Example:
    Poet URL: http://famouspoetsandpoems.com/poets/allen_ginsberg/poems
    Poem URL: http://famouspoetsandpoems.com/poets/gary_snyder/poems/18114


"""

import requests
import bs4
from WebScraper import Constants


class UnexpectedResponse(Exception):
    """UnexpectedResponse Exception

        Exception thrown by methods when response is empty or does not
        conform with the expected response


        Args:
            msg (str): Human readable string describing the exception.
            url (str): URL that responded unexpectedly.

        Attributes:
            msg (str): Human readable string describing the exception.
            url (str): URL that responded unexpectedly.

        """

    def __init__(self, msg, url):
        super().__init__(msg)
        self.url = url
        self.msg = msg


def get_poem_urls(url: str, poet: str) -> list:
    """

    :param url: URL for a specific poet
    :return: List of URLS of specific poems. Depends on html containing
            a specific href format.
    """
    request = requests.get(url)

    if request.content is None or request.content == "":
        raise UnexpectedResponse("No content in get_poem_urls", url)

    soup = bs4.BeautifulSoup(request.content, 'html.parser')
    poems = []

    for link in soup.find_all('a'):
        href = link.get('href')
        poem_href = f'/poets/{poet}/poems/'

        if poem_href in href:
            poems.append(f'{Constants.URL_PREFIX}{href}')

    if len(poems) == 0:
        raise UnexpectedResponse("No poem urls found", url)

    return poems


def get_poem_lines(url: str) -> list:
    """

    :param url:
    :return: List of text lines from a specific poem
    """
    return convert_contents_to_string_list(get_poems_tags(url))


def get_poems_tags(url: str):
    """

    :param url: URL to a specific poem
    :return: List of BeautifulSoup html tags fond in a unique <Div> containing a
            specific style attribute.
    """
    request = requests.get(url)

    if request.content is None or request.content == "":
        raise UnexpectedResponse("No content in get_poems_tags", url)

    soup = bs4.BeautifulSoup(request.content, 'html.parser')
    divs = soup.find_all(style=Constants.POEM_CSS_STYLE)

    if len(divs) != 1:
        raise UnexpectedResponse(
            f"Found {len(divs)} of divs with style:{Constants.POEM_CSS_STYLE}, must equal 1", url
        )
    if divs[0].contents is None or len(divs[0].contents) == 0:
        raise UnexpectedResponse(
            f"Divisions with style:{Constants.POEM_CSS_STYLE} had no content", url
        )

    return divs[0].contents


def convert_contents_to_string_list(bs_list: list) -> list:
    """

    :param bs_list: List of BeautifulSoup tags
    :return: List of str containing the only the text found with
            in the bs_list parameter.
    """
    string_contents = [str(c) for c in bs_list if not isinstance(c, bs4.element.Tag)]
    return string_contents


def get_clean_poem_lines(poem_lines: list, remove_non_ascii: bool = False) -> list:
    """
    The website can return lines of text that have a lot of formatting for
    the purpose of visual pleasing presentation on the page but contains
    escaped characters and line breaks that may have not existed in the
    in the original poem.

    :param poem_lines: List of str
    :param remove_non_ascii: Remove any characters that are not UTF-8
    :return: List of str
    """
    current_line = ""
    clean_poem_lines = []
    for line in poem_lines:
        line = line.lstrip()

        if remove_non_ascii:
            line = ''.join(i for i in line if ord(i) < 128)

        line = line if not line.endswith("- ") else line[:-2]
        current_line = current_line + line
        temp_line = current_line.strip()

        if temp_line.endswith(".") or temp_line.endswith("?") or temp_line.endswith("!"):
            clean_poem_lines.append(current_line + " ")
            current_line = ""

    if len(current_line) != 0:
        clean_poem_lines.append(current_line)

    return clean_poem_lines


def write_poems_to_file(filename: str, poem_lines: list, append: bool = False, encoding: str = 'utf-16') -> None:
    """
    Handy utility to save off list of str to file.

    :param filename: full name and path of file
    :param poem_lines: List of str
    :param append: open file either as write which will overwrite if exist or append to file
    :param encoding: encoding for file type
    """

    write_type = "a" if append else "w"

    with open(filename, write_type, encoding=encoding) as text_file:
        for line in poem_lines:
            text_file.write(f"\n{line}")



