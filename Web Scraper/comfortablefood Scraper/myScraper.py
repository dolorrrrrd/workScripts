import requests
from bs4 import BeautifulSoup
import os

def imagedown(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img')
        for image in images:
            name = image['alt']
            link = image['data-src-zoom-image']
            with open(name.replace(' ', '-').replace('/', '').replace('"','') + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print('Writing: ', name)
    except:
        pass

postLinks = ["https://cottonandcloud.com/31-womens-crochet-dress-patterns/",
"https://cottonandcloud.com/35-baby-blanket-crochet-patterns/",
"https://cottonandcloud.com/30-chunky-crochet-blanket-patterns/",
"https://cottonandcloud.com/51-cowl-knitting-patterns/",
"https://cottonandcloud.com/25-knit-christmas-stocking-patterns/",
"https://cottonandcloud.com/25-crochet-triangle-shawl-patterns/",
"https://cottonandcloud.com/21-crochet-turtle-patterns/",
"https://cottonandcloud.com/33-crochet-mitten-patterns/",
"https://cottonandcloud.com/35-popular-etsy-crochet-patterns/",
"https://cottonandcloud.com/25-knit-and-purl-stitch-patterns/",
"https://cottonandcloud.com/31-mandala-yarn-crochet-patterns/",
"https://cottonandcloud.com/39-macrame-wall-hanging-patterns/",
"https://cottonandcloud.com/25-crochet-alpine-stitch-blanket-patterns/",
"https://cottonandcloud.com/10-knit-stuffed-animals-patterns/"]

for links in postLinks:
    count = 0
    r = requests.get(links)
    soup = BeautifulSoup(r.text, 'html.parser')
    foldern = soup.find('h1').string
    try:
        os.mkdir(os.path.join("C:/Users/Admin/Desktop/stuff/Web Scraper/", foldern))
    except:
        pass
    os.chdir(os.path.join("C:/Users/Admin/Desktop/stuff/Web Scraper/", foldern))
    for x in soup.find_all('h2'):
        # count += 1
        # try:
        #     os.mkdir(os.path.join("C:/Users/Admin/Desktop/stuff/Web Scraper/"+foldern, 'item '+ str(count)))
        # except:
        #     pass
        # os.chdir(os.path.join("C:/Users/Admin/Desktop/stuff/Web Scraper/"+foldern, 'item '+str(count)))
        if(x.find('a')):
            imagedown(x.find('a').get('href'))