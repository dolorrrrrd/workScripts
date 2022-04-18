import requests
from bs4 import BeautifulSoup
import os
import re

def imagedown(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img', {'class':'carousel-image'})
        for image in images:
            name = image['alt']
            link = image['data-src-zoom-image']
            with open(name.replace(' ', '-').replace('/', '').replace('"','').replace(':','') + '.jpg', 'wb') as f:
            # with open(re.sub('\W',name)+ '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print('Writing: ', name)
    except:
        pass

postLinks = ["https://www.etsy.com/listing/818128777/crochet-basket-pattern-sea-urchin-sea?zanpid=10723_1646303411_771aa057eafffbf05ca7ad28506d5914&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1646303411_771aa057eafffbf05ca7ad28506d5914",
"https://www.etsy.com/listing/863342976/mocha-me-cozy-crochet-pattern-pdf-mug?zanpid=10723_1646309943_59deb3905963a259a54aabddf5920ded&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1646309943_59deb3905963a259a54aabddf5920ded",
"https://www.etsy.com/listing/252035536/karlas-wrist-warmers-crochet-pattern?zanpid=10723_1650291406_ceab38088e15435eb8129d5c08abe702&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291406_ceab38088e15435eb8129d5c08abe702",
"https://www.etsy.com/listing/869245339/crochet-hat-pattern-harlequin-puff?zanpid=10723_1650291458_fff1ffd5a05343eab7055d513e864b1a&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291458_fff1ffd5a05343eab7055d513e864b1a",
"https://www.etsy.com/listing/212541722/pdf-snowflower-lace-coaster-crochet?zanpid=10723_1650291506_1cbf861663ffb3391211d7c43d08d96b&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291506_1cbf861663ffb3391211d7c43d08d96b",
"https://www.etsy.com/uk/listing/129252681/crochet-cross-bookmark-pattern-tutorial?zanpid=10723_1646309450_9ebd40c7a2092ba41024abc1aed3ad93&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1646309450_9ebd40c7a2092ba41024abc1aed3ad93",
"https://www.etsy.com/listing/207160622/crochet-pattern-for-the-chicken-or-the?ref=search_srv-4&zanpid=10723_1650291581_edf13849358a1102d47b11426cc0bafb&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291581_edf13849358a1102d47b11426cc0bafb",
"https://www.etsy.com/listing/841014031/harlequin-crochet-dishcloth-pattern-pdf?zanpid=10723_1650291603_6c933d751ecf888525214954dac5fc5b&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291603_6c933d751ecf888525214954dac5fc5b",
"https://www.etsy.com/listing/86190638/crochet-pattern-star-by-atergcrochet?zanpid=10723_1650291625_40d96130a1cbb35674632e8e259cae0a&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291625_40d96130a1cbb35674632e8e259cae0a",
"https://www.etsy.com/uk/listing/865220506/?zanpid=10723_1650291669_01c9f8c84f1958f82eb63273ca820a56&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291669_01c9f8c84f1958f82eb63273ca820a56",
"https://www.etsy.com/listing/724444291/baby-dribble-bib-pdf-crochet-pattern?zanpid=10723_1650291713_b0f6d987ff5ec405e6acd126a1b9ae6b&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291713_b0f6d987ff5ec405e6acd126a1b9ae6b",
"https://www.etsy.com/listing/677204069/easy-crochet-pattern-crochet-hat-isabel?zanpid=10723_1650291731_9c5c04e5d201722ef833bb471aa884c9&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291731_9c5c04e5d201722ef833bb471aa884c9",
"https://www.etsy.com/listing/510416182/crochet-pattern-crochet-christmas-basket?zanpid=10723_1650291748_df717958df01d600acc595527393c8ef&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291748_df717958df01d600acc595527393c8ef",
"https://www.etsy.com/listing/681242898/crochet-pattern-daybreak-trivet-crochet?zanpid=10723_1650291784_886bd84c8b734979cfaafc1204001b36&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291784_886bd84c8b734979cfaafc1204001b36",
"https://www.etsy.com/uk/listing/782663544/crochet-pattern-wine-cozy-pattern?zanpid=10723_1650291817_963d505924f6abb35791ac7bdff71534&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291817_963d505924f6abb35791ac7bdff71534",
"https://www.etsy.com/listing/116631129/crochet-pattern-crochet-christmas?zanpid=10723_1650291838_453ce69f3047ce36d8fef81fb196fc2d&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291838_453ce69f3047ce36d8fef81fb196fc2d",
"https://www.etsy.com/listing/661355167/crochet-planter-pattern-diy-crochet?zanpid=10723_1650291884_42859ce6a5f8becfc248b01767795aac&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291884_42859ce6a5f8becfc248b01767795aac",
"https://www.etsy.com/uk/listing/679433629/?g=&zanpid=10723_1650291929_a5e2d34837723681aa4338bc3a300efc&utm_medium=affiliate&utm_source=affiliate_window&utm_campaign=eu_buyer&utm_content=349161&awc=10723_1650291929_a5e2d34837723681aa4338bc3a300efc"]

count = 0
for links in postLinks:
    count += 1
    # r = requests.get(links)
    # soup = BeautifulSoup(r.text, 'html.parser')
    # images = soup.find('h1').string
    try:
        os.mkdir(os.path.join("C:/Users/Admin/Desktop/stuff/Cotton And Cloud Pics 2/35+ Fast and Easy Crochet Gift Ideas Anyone Can Make",'item '+ str(count)))
    except:
        pass
    os.chdir(os.path.join("C:/Users/Admin/Desktop/stuff/Cotton And Cloud Pics 2/35+ Fast and Easy Crochet Gift Ideas Anyone Can Make", 'item '+str(count)))
    imagedown(links)
