import requests
import re
from bs4 import BeautifulSoup

BASE_URL = "https://genius.com"
pattern = re.compile(r'\bLyrics__Container\b')
# pattern = re.compile(r'\bAbout__Container\b')

def scrapper(webpage_url):
    page_url = BASE_URL + webpage_url
    page = requests.get(page_url)
    html = BeautifulSoup(page.text, "html.parser")
    # remove script tags that they put in the middle of the lyrics
    [h.extract() for h in html('script')]
    lyrics_containers = html.find_all('div', class_=pattern)

    lyrics = ""
    for lyrics_container in lyrics_containers:
        # Replace <br> tags with spaces
        for br in lyrics_container.find_all('br'):
            br.replace_with(' ')

        # Extract the text
        lyrics += lyrics_container.get_text() + '\n'

    return lyrics

if __name__ == "__main__":
    path = "/Lil-nas-x-sun-goes-down-lyrics"
    lyrics = scrapper(path)
    print(lyrics)