import requests
# from bs4 import BeautifulSoup
import bs4
# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
#


#  Allen Ginsberg, Lawrence Ferlinghetti, Gregory Corso, and Gary Snyder
# http://famouspoetsandpoems.com/poets/allen_ginsberg/poems
# http://famouspoetsandpoems.com/poets/lawrence_ferlinghetti/poems
# http://famouspoetsandpoems.com/poets/gregory_corso/poems
# http://famouspoetsandpoems.com/poets/gary_snyder/poems
POETS = ["allen_ginsberg", "lawrence_ferlinghetti", "gregory_corso", "gary_snyder"]
URL_PREFIX = "http://famouspoetsandpoems.com/"
URL_POET = "poets/"
URL_POST = "/poems"
POEM_CSS_STYLE = "padding-left:14px;padding-top:20px;font-family:Arial;font-size:13px;"


# TODO: add exception handling
def get_poems(url: str) -> list:
    request = requests.get(url)
    soup = bs4.BeautifulSoup(request.content, 'html.parser')
    poems = []

    for link in soup.find_all('a'):
        href = link.get('href')
        poem_href = f'/poets/{POETS[0]}/poems'
        if poem_href in href and href != poem_href:
            poems.append(f'{URL_PREFIX}{href}')

    return poems


# TODO: add exception handling
def get_poem_lines(url: str) -> list:
    request_page = requests.get(url)
    soup = bs4.BeautifulSoup(request_page.content, 'html.parser')

    divs = soup.find_all(style=POEM_CSS_STYLE)
    contents = divs[0].contents
    string_contents = [str(c) for c in contents if not isinstance(c, bs4.element.Tag)]
    return string_contents[:len(string_contents)-1]


# TODO: add exception handling
def get_clean_poem_lines(poem_lines: list) -> list:
    current_line = ""
    clean_poem_lines = []
    for line in poem_lines:
        line = line.replace("\n", "").lstrip()
        line = line if not line.endswith("- ") else line[:len(line) - 2]
        current_line = current_line + line

        if current_line.endswith(". ") or current_line.endswith("? ") or current_line.endswith("! "):
            clean_poem_lines.append(current_line.strip())
            current_line = ""

    if current_line != "":
        clean_poem_lines.append(current_line)

    return clean_poem_lines


def write_poems_to_file(filename: str, poem_lines: list, encoding: str = 'utf-16') -> None:
    with open(filename, 'w', encoding=encoding) as f:
        for l in poem_lines:
            f.write(f"\n{l}")


def write_poet_to_file(poet_name: str, filename: str):
    current_url = f"{URL_PREFIX}{URL_POET}{poet_name}{URL_POST}"
    poem_links = get_poems(current_url)

    line_list = []
    for link in poem_links:
        line_list = line_list + get_poem_lines(link)

    clean_lines = get_clean_poem_lines(line_list)
    write_poems_to_file(filename, clean_lines)


write_poet_to_file(POETS[0], filename='whitman.txt')
# l = [1,2,3,4,5,6]
# print(l[:len(l)-1])