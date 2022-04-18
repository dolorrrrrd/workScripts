import pywhatkit as kt
import re

my_file = open("Restos3.txt", "r")
removedList = my_file.readlines()
editedList = re.sub('\&', 'and',removedList)
my_file.close()

for x in editedList:
    kt.search(x)

