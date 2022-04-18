my_file = open("removed csv.txt", "r")
removedList = my_file.read()
removed_list = removedList.split(",")
my_file.close()

my_file2 = open("Url csv.txt", "r")
urlList = my_file2.read()
url_list = urlList.split(",")
my_file2.close()

print (len(removed_list),len(url_list))

diff = list();

for x in url_list:
    if x in removed_list:
        print ("nop")
    else:
        diff.append(x)
print (len(diff))