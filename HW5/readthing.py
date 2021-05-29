import os

fh1 = open("abc.txt","r")
data = fh1.read()
print(data)

fh2 = open("123.txt","w")
fh2.write("Whats Up Youtube...")
fh2.close()
#Anytime you are creating a data file you MUST close it.
#be safe and close all data connections

