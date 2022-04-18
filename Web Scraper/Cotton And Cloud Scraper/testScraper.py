import requests
from bs4 import BeautifulSoup
import os

url = 'https://cottonandcloud.com/10-knit-stuffed-animals-patterns/'

# url = ["https://cottonandcloud.com/35-popular-etsy-crochet-patterns/",
# "https://cottonandcloud.com/25-knit-and-purl-stitch-patterns/",
# "https://cottonandcloud.com/31-mandala-yarn-crochet-patterns/",
# "https://cottonandcloud.com/39-macrame-wall-hanging-patterns/",
# "https://cottonandcloud.com/25-crochet-alpine-stitch-blanket-patterns/",
# "https://cottonandcloud.com/10-knit-stuffed-animals-patterns/"]

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
links = []
for x in soup.find_all('h2'):
    if(x.find('a')):
        links.append(x.find('a').get('href'))
print(links)

# import requests
# from bs4 import BeautifulSoup
# import os

# # url = 'https://cottonandcloud.com/10-knit-stuffed-animals-patterns/'

# url = ["https://cottonandcloud.com/35-popular-etsy-crochet-patterns/",
# "https://cottonandcloud.com/25-knit-and-purl-stitch-patterns/",
# "https://cottonandcloud.com/31-mandala-yarn-crochet-patterns/",
# "https://cottonandcloud.com/39-macrame-wall-hanging-patterns/",
# "https://cottonandcloud.com/25-crochet-alpine-stitch-blanket-patterns/",
# "https://cottonandcloud.com/10-knit-stuffed-animals-patterns/"]

# linklist = []

# for link in range (len(url)):
#     r = requests.get(url[link])
#     soup = BeautifulSoup(r.text, 'html.parser')
#     links = []
#     for x in soup.find_all('h2'):
#         if(x.find('a')):
#             links.append(x.find('a').get('href'))
#     linklist.append(links)
# print(linklist)