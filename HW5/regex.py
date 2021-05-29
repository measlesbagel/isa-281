import re

str1 = "Johnny jonny78.34yes papa, 45abc hsh mtr3.2 j29.1dj3df"
list1 = re.findall("[0-9]+\.*[0-9]*",str1)
list2 = [float(x) for x in list1]
print(list2,"\n",round(sum(list2),2))


