#Cagle-Myles-HW
def passcheck(x,y):
    list1 = list(x)
    count = 0
    try:
        num = int(list1[0])
        return y,print("Password can not start with an integer. Try again.\n")
    except:
        for i in list1:
            try:
                num = int(i)
                count += 1
            except:
                continue
        if(count >= 2 and len(list1) >= 8 and len(list1) <= 16):
            y = True
            return y,print("Password is valid. Details below: \n"),print("Your password",x,"is",len(list1),"characters long in total."),print("Your password",x,"contains",count,"integers."),print("Your password",x,"contains",len(list1)-count,"characters.")
        elif(count < 2):
            return y,print("Password must contain at least 2 numbers. Try again.\n")
        elif(len(list1) < 8):
            return y,print("Password must be at least 8 characters long. Try again.\n")
        else:
            return y,print("Password cant be more than 16 characters long. Try again.\n")

def main():
    print("Please enter a password between 8 and 16 characters long\n")
    stop = False
    while stop is False:
        password = input("Please enter your password: ")
        y = passcheck(password,stop)
        stop = y[0]
main()
