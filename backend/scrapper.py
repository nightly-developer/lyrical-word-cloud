import requests
import re
from bs4 import BeautifulSoup

BASE_URL = "https://genius.com"
pattern = re.compile(r'\bLyrics__Container\b')

def scrapper(webpage_url):
    page_url = BASE_URL + webpage_url
    page = requests.get(page_url)
    html = BeautifulSoup(page.text, "html.parser")
    # remove script tags that they put in the middle of the lyrics
    [h.extract() for h in html('script')]
    # at least Genius is nice and has a tag called 'lyrics'!
    lyrics_container = html.find('div', class_=pattern)
    return lyrics_container.get_text() if  lyrics_container else "html"

if __name__ == "__main__":
    path = "/Lil-nas-x-sun-goes-down-lyrics"
    lyrics = scrapper(path)
    print(lyrics)