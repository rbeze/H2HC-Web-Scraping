from urllib.request import urlopen
from bs4 import BeautifulSoup

speakers_url = "https://www.h2hc.com.br/articles/speaker.html"
bs = BeautifulSoup(urlopen(speakers_url), 'html.parser')

names = bs.find_all("a", {"class": "card-link text-center font-weight-bold"})

for name in names:
    print(name.text.split("-")[0])