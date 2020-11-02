import re
from bs4 import BeautifulSoup
import urllib.request
import json

animes = []

def pushAnime(anime):
    animes.append(anime)

response = urllib.request.urlopen('https://myanimelist.net')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

for div in soup.find_all('div', attrs={'class': 'seasonal'}):
    w_body = div.find('div', attrs={'class':'widget-content'})

lis = []

for ul in w_body.find_all('ul', attrs={'class':'widget-slide'}):
    for li in ul.findAll('li'):
        if li.find('ul'):
            break
        lis.append(li)

for li in lis:
    content = li.find('a')
    name = content.find('span')
    txt = content['href']
    anime = txt.split("myanimelist.net/anime/")[1].split("/")[0]
    img = content.find('img')
    pushAnime({ 
        'anime': anime, 
        'nome': name.text, 
        'img': img['data-src']
    })


with open('animes-season.json', 'w') as fp:
  json.dump(animes, fp)

print('Extraction finished')