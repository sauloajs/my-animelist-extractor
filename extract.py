import re
from bs4 import BeautifulSoup
import urllib.request
import json

response = urllib.request.urlopen('https://myanimelist.net/topanime.php')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

pattern = re.compile("/anime/")
temp = ''
myanimelist = []

def pushAnime(anime):
  myanimelist.append(anime)

def getImage(id):
  response = urllib.request.urlopen('https://myanimelist.net/anime/'+str(id))
  html_doc = response.read()
  soup = BeautifulSoup(html_doc, 'html.parser')
  img = soup.select('img.ac')
  return img[0]['data-src']

for x in soup.select('a.hoverinfo_trigger', href=True): 
  if pattern.search(x['href']):
    txt = x['href']
    anime = txt.split("myanimelist.net/anime/")[1].split("/")[0]

    if (x.img != None):
      try:
        pushAnime({
          "id": int(anime),
          "name": x.img['alt'].split('Anime: ')[1],
          "img": getImage(int(anime))
        })
      except:
        print('Failed')

with open('animes.json', 'w') as fp:
  json.dump(myanimelist, fp)

print('Extraction finished')
