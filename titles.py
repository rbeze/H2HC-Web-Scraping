from urllib.request import urlopen
from bs4 import BeautifulSoup

titles_url = "https://www.h2hc.com.br/articles/speaker.html"
bs = BeautifulSoup(urlopen(titles_url), 'html.parser')

titles = bs.find_all("strong")

for title in titles:
    print(title.text)