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
def get_poem_urls(url: str) -> list:
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

    return convert_contents_to_strList(contents)


def convert_contents_to_strList(bsList: list) -> list:
    string_contents = [str(c) for c in bsList if not isinstance(c, bs4.element.Tag)]
    return string_contents[: -1]

# TODO: add exception handling
def get_clean_poem_lines(poem_lines: list, remove_non_asscii : bool = False) -> list:
    current_line = ""
    clean_poem_lines = []
    for line in poem_lines:
        line = line.replace("\n", "").lstrip()

        if remove_non_asscii:
            text = text.decode("utf - 8").encode("ascii", "ignore")

        line = line if not line.endswith("- ") else line[:-2]
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
    poem_links = get_poem_urls(current_url)

    line_list = []
    for link in poem_links:
        line_list = line_list + get_poem_lines(link)

    clean_lines = get_clean_poem_lines(line_list)
    write_poems_to_file(filename, clean_lines)


# pl = get_poem_urls(f"{URL_PREFIX}{URL_POET}{POETS[0]}{URL_POST}")
# print(pl)

l = [1, 2, 3, 4, 5, 6]
print(l[: -1])
# poem_urls = ['http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8315', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8318', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8320', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8322', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8325', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8327', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8329', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8331', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8333', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8335', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8337', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8340', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8342', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8344', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8346', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8348', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8349', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8350', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8351', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8352', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8355', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8356', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8358', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8360', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8362', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8365', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8367', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8369', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8371', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8374', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8376', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8378', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8381', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8382', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8386', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8388', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8390', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8391', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8392', 'http://famouspoetsandpoems.com//poets/allen_ginsberg/poems/8393']
