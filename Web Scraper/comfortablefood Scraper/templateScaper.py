import requests
from bs4 import BeautifulSoup
import os

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    print(os.getcwd())
    print(images)
    # for image in images:
    #     name = image['alt']
    #     if image.has_attr('data-src'):
    #         link = image['data-src']
    #     elif image.has_attr('src') and 'http' in image['src']:
    #         link = image['src']
    #     with open(name.replace(' ', '-').replace('/', '').replace('"','') + '.jpg', 'wb') as f:
    #         im = requests.get(link)
    #         f.write(im.content)
    #         print('Writing: ', name)
            
picLinks = 'https://www.veselka.com/'
imagedown(picLinks, 'f2')