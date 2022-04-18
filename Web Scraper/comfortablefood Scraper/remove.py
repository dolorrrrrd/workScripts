my_file = open("Restos.txt", "r")
removedList = my_file.read()
my_file.close()

for x in removedList:
    print (x)