import requests
from bs4 import BeautifulSoup

def getTopicCount(topic):
    url = "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=" + sys.argv[1]
    html = requests.get(url)
    if not 'parse' in html.json():
        raise ValueError
    soup = BeautifulSoup(html.json()['parse']['text']['*'], features="html.parser")
    text = soup.get_text()
    print(text.count(topic))

# TEST | usage : python3 ex3.py topic
import sys

try:
    print(getTopicCount(sys.argv[1]))
except ValueError:
    print("Wrong arguments")
