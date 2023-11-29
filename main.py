from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = "https://www.h2hc.com.br"
bs = BeautifulSoup(urlopen(base_url), 'html.parser')
# print(bs)

def search_pages():
    pages = bs.find_all("a", {"class": "nav-link"})
    for page in pages:
        if "Palestrantes" in page:
            speakers = page["href"]
            return speakers 
        
speakers_url = f"{base_url}{search_pages()}"
open_speakers = urlopen(speakers_url)
bs = BeautifulSoup(open_speakers, 'html.parser')
speakers_content = bs.find_all("div", {"class": "card"})
for speaker in speakers_content:
    names = speaker.find_all("a", {"class": "card-link text-center font-weight-bold"})[0]
    speaker_name = names.text.split("-")[0]
    speaker_title = names.text.split("-")[1]
    print(speaker_name, speaker_title)