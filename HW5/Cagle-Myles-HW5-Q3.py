#Cagle-Myles-HW5
import re

fh1 = open("long.txt","r")
data = fh1.read()
phraselist = re.findall("[F-f]rom:.*",data)
dictionary = dict()
fh1.close()

for i in phraselist:
    email = i.split()
    dictionary[email[1]] = dictionary.get(email[1], 0) + 1

maximum = max(dictionary, key=dictionary.get)
print("Most prolific email sender:",maximum+",",dictionary[maximum])
print(dictionary)


