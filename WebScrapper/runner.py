import requests
from bs4 import BeautifulSoup

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

current_url = f"{URL_PREFIX}{URL_POET}{POETS[0]}{URL_POST}"
print(current_url)

page = requests.get(current_url)
soup = BeautifulSoup(page.content, 'html.parser')

for link in soup.find_all('a'):
    href = link.get('href')
    poem_href = f'/poets/{POETS[0]}/poems'
    if poem_href in href and href != poem_href:
        print(f'{URL_PREFIX}{href}')
