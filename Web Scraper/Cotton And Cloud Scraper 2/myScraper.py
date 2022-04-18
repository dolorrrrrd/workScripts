import requests
from bs4 import BeautifulSoup
import os

def imagedown(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        images = soup.find_all('img', {'class':'carousel-image'})
        for image in images:
            name = image['alt']
            link = image['data-src-zoom-image']
            with open(name.replace(' ', '-').replace('/', '').replace('"','') + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print('Writing: ', name)
    except:
        pass

postLinks = ["https://www.etsy.com/listing/766993131/barn-quilt-14-sunflower?epik=dj0yJnU9V3c0ZHlpV0tnSHRWT0tRSGRGQkdfdGZ2VXhWSU1Sa04mcD0wJm49aEhNOHpYZmZWeldMS1NfTmpOODdwQSZ0PUFBQUFBRi0yZFdJ&variation0=1293734765",
"https://www.etsy.com/listing/707119662/sun-flower-barn-quilt-board-2x2?epik=dj0yJnU9WmZ2ckVoWnh1T0hZN2JFMFdJYkpLdHI0dF9MNE1SaTkmcD0wJm49Q3ZoeWtJbERSLXgtY2RhZVVFMXJJZyZ0PUFBQUFBR0RndkJJ",
"https://www.etsy.com/listing/599933137/patriotic-barn-quilt-svg-liberty-barn?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=patriotic+barn+quilt+design&ref=sr_gallery-1-1&organic_search_click=1",
"https://www.etsy.com/theTinyEasel/listing/471744745/barn-quilt-hand-painted-2x2?utm_campaign=Share&utm_medium=social_organic&utm_source=DSMT2&utm_term=so.smt&share_time=1524321286000",
"https://www.etsy.com/listing/814952270/patriotic-barn-quilt-designs?epik=dj0yJnU9Y3p0WktickpVOE9iUndQVWNMT3FHSk9WRXdfbVJIQlkmcD0wJm49U0p2MTdqOGhQckhhWFNHRFY5RVpYdyZ0PUFBQUFBRi0yZ2JZ",
"https://www.etsy.com/listing/477085041/barn-quilt-1x1-to-hang-on-porchgarden?show_sold_out_detail=1&epik=dj0yJnU9TTNSUTgwbU9iWjBMcXFYWWdRaFlCSThBRUtVX0RJWFcmcD0wJm49MG1UQ1NCczlPdXVPWnNaVWJhM2NmdyZ0PUFBQUFBR0RneDg0",
"https://www.etsy.com/listing/800280682/glowforge-projects-svg-simple-barn-quilt?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=patriotic+barn+quilt+pattern&ref=sr_gallery-1-4&organic_search_click=1",
"https://www.etsy.com/listing/806385068/barn-quilt-svg-cut-file-pattern-for?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=modern+barn+quilt+pattern&ref=sr_gallery-1-1&organic_search_click=1",
"https://www.etsy.com/listing/749186061/sweet-judy-blue-eyes-barn-quilt-4x4?epik=dj0yJnU9aEN4dHdQbkVfdGVoN0NNcldFSFZTM0MyT2U0UHd1aEQmcD0wJm49SkpJZjBWWHRpdEpmNU4wVlVLZ1U3USZ0PUFBQUFBR0Rnemt3"]

count = 0
for links in postLinks:
    count += 1
    try:
        os.mkdir(os.path.join("C:\Users\Admin\Desktop\stuff\Cotton And Cloud Pics 2", 'item '+ str(count)))
    except:
        pass
    os.chdir(os.path.join("C:\Users\Admin\Desktop\stuff\Cotton And Cloud Pics 2", 'item '+str(count)))
    imagedown(links)
