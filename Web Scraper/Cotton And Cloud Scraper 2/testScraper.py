import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.etsy.com/listing/766993131/barn-quilt-14-sunflower?epik=dj0yJnU9V3c0ZHlpV0tnSHRWT0tRSGRGQkdfdGZ2VXhWSU1Sa04mcD0wJm49aEhNOHpYZmZWeldMS1NfTmpOODdwQSZ0PUFBQUFBRi0yZFdJ&variation0=1293734765'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('img', {'class':'carousel-image'})
print(images)
for image in images:
    name = image['alt']
    link = image['data-src-zoom-image']
    with open(name.replace(' ', '-').replace('/', '').replace('"','') + '.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)
        print('Writing: ', name)
