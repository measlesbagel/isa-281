#Cagle-Myles-HW5
import re

fh1 = open("long.txt","r")
data = fh1.read()
phraselist = re.findall("Expected_Probability:.*",data)
total = 0
count = 0
fh1.close()

for i in phraselist:
    calc = i.split()
    total += float(calc[1])
    count += 1

fh2 = open("Cagle-Myles.txt","w")
print("Line count: "+str(count))
fh2.write("Line count: "+str(count)+"\n")
print("Total: "+str(round(total,3)))
fh2.write("Total: "+str(round(total,3))+"\n")
print("Average probability: "+str(round(total/count,3)))
fh2.write("Average probability: "+str(round(total/count,3)))
fh2.close()







