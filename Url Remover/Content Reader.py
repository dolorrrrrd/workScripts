import re

my_file = open("Scraper.txt", "r", encoding="utf8")
content = my_file.readlines()
my_file.close()

links = []

for x in content:
    if re.search('href', x):
        links.append(x)
print(links)
# print(l1 = re.sub('.*http','http',links[0]))
# print (re.sub())
