import requests
from bs4 import BeautifulSoup
import os

#url = 'https://www.etsy.com/uk/listing/857565688/crochet-pattern-amigurumi-snowman?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=christmas+ornament+and+decoration+crochet+pattern&ref=sr_gallery-1-36&organic_search_click=1&pop=1'

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    # print (type(images))
    # print(images)
    
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '').replace('"','') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)
            
picLinks = 'https://www.etsy.com/uk/listing/857565688/crochet-pattern-amigurumi-snowman?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=christmas+ornament+and+decoration+crochet+pattern&ref=sr_gallery-1-36&organic_search_click=1&pop=1'
imagedown(picLinks, 'f2')