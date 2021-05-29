#Cagle-Myles-HW
def checkpal(x):
    revlist = []
    for i in range(len(x)):
        y = (x[-i - 1])
        revlist.append(y)

    print("Original:",x)
    print("Reversed:",revlist)
    if(revlist == x):
        return True
    else:
        return False

def main():
    ustr = input("Please enter a string to check if its a pallindrome: ")
    ustrlist1=list(ustr)
    print(ustr, "is a pallindrome:",checkpal(ustrlist1))

main()
