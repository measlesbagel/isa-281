#Cagle-Myles-HW
factorial = input("Please enter a positive integer to compute factorial: ")
i=3
u=1
while True:
    try:
        factorial = int(factorial)
        y=factorial
        if(factorial > 0):
            while(u<factorial):
                y=y*u
                u+=1
            print("The factorial of",factorial,"=",y)
            break
        elif(factorial <= 0):
            print("No zero or negative integers please. ")
            i-=1
        elif(i == 0):
            print("No attempts left...")
            break
        factorial = input(str(i)+" Attempts left, Please enter a postive integer to computer factorial: ")
        
    except ValueError:
        try:
            if(float(factorial)%1 != 0):
                print("No floats please. ")
                i-=1
            if(i == 0):
                print("No attempts left...")
                break
            factorial = input(str(i)+" Attempts left, Please enter a postive integer to computer factorial: ")
        except:
            print("No strings please. ")
            i-=1
            factorial = input(str(i)+" Attempts left, Please enter a postive integer to computer factorial: ")

            

