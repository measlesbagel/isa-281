fhand = open("1.txt","r")
total = 0
count = 0

for line in fhand:
    line = line.rstrip()
    num = int(line)
    count += 1
    total += num

average = round(total/count,2)
fhand2 = open("2.txt","w")
fhand2.write("Total: "+str(total)+"\nAverage: "+str(average))
fhand2.close()
fhand2 = open("2.txt","r")
data = fhand2.read()
fhand2.close()
print(data)
