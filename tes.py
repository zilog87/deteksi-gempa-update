import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.bmkg.go.id/')

soup = BeautifulSoup(r.content, "html.parser")
print(soup.prettify())
