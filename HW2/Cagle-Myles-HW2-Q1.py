#Cagle-Myles-HW
unum = int(input("How many numbers do you want to print the able for? "))
u=1
i=1
while(u<=unum):
    for i in range (1,11):
        num=i*u
        print(str(u),"x",str(i),"=",str(num), end=" ")
    u+=1
    print("")

        
        
        
    
