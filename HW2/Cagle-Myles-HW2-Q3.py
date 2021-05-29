#Cagle-Myles-HW
while True:
    try:
        i=1
        print("This program stops taking more numbers if you enter 0")
        newNumber = int(input("Enter number "+str(i)+": "))
        numberList = [newNumber]
        while(newNumber is not 0):
            i += 1
            newNumber = int(input("Enter number "+str(i)+": "))
            numberList.append(newNumber)
        numberList.remove(0)
        positiveList = [n for n in numberList if n > 0]
        negativeList = [n for n in numberList if n < 0]
        print("You stopped entering numbers. Summary below")
        count = len(numberList)
        positiveCount = len(positiveList)
        negativeCount = len(negativeList)
        largest = max(numberList)
        smallest = min(numberList)
        total = sum(numberList)
        average = round(float(total / count),3)
        print("Count:",count)
        print("Positive:",positiveCount)
        print("Negative:",negativeCount)
        print("Largest:",largest)
        print("Smallest:",smallest)
        print("Total:",total)
        print("Average:",average)
        break
    
    except:
        print("Not an integer... Restart Please")
        numberList.clear
        
