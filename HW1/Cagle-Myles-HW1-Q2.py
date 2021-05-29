#Cagle-Myles-HW
food = float(input("Enter the cost of food "))
tip = float(input("Enter the amount tipped: "))
ratio = (tip/food)*100
if(ratio < 10):
    print("You only tipped",round(ratio,2),"% please tip better next time.")
elif(ratio >= 10 and ratio <= 20):
    print("You tipped",round(ratio,),"% thats perfect keep it up!")
else:
    print("You seriously tipped",round(ratio,2),"% thats way too much!")
