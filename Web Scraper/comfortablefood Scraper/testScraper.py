import requests
from bs4 import BeautifulSoup
import os

url = 'https://docs.google.com/document/d/1cqBmfimG3Sa-Kfj5QWYrpDIjsLA6L88ftwbCPUHaowY/edit#heading=h.gm86lnj4cdvj'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('h2')
print(images)