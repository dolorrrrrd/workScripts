import re

my_file = open("Complete Url csv.txt", "r")
fullList = my_file.read()
full_list = fullList.split(",")
my_file.close()

my_file2 = open("Url List.txt", "r")
urlList = my_file2.read()
url_list = re.split('\n',urlList)
my_file2.close()

removed_list = []

for x in range (len(url_list)):
    if url_list[x] in full_list:
        removed_list.append(url_list[x])
        full_list.remove(url_list[x])

l = open("Left.txt", "w")
for element in full_list:
    l.write(element + "\n")
l.close()

r = open("removed.txt", "w")
for element in removed_list:
    r.write(element + "\n")
r.close()

print("done")