#Cagle-Myles-HW5
import re

sumtotal = 0
fh = open("regex_large.txt","r")
data = fh.read()
numlist = re.findall("[0-9]+",data)

for i in numlist:
    num = int(i)
    sumtotal += num

print("Sum of numbers in this file = ",sumtotal)
