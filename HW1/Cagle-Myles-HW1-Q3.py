#Cagle-Myles-HW
while True:
    try:
        choice = int(input("This program calculates the area of a geometric figure. \nFor a circle enter 1, for a square enter 2, for a rectangle enter 3: "))
        if(choice == 1):
            print("You chose circle because you entered 1")
            pi = 3.1415295
            radius = float(input("Please enter the radius: "))
            area = pi*radius*radius
            print("Area of the circle is",round(area,2))
            break
        elif(choice == 2):
            print("You chose square because you entered 2")
            side = float(input("Please enter the length of the side: "))
            area = side*side
            print("Area of the square is",round(area,2))
            break
        elif(choice == 3):
            print("You chose rectangle because you entered 3")
            length = float(input("Please enter the length: "))
            width = float(input("Please enter the width: "))
            area = length*width
            print("Area of the rectangle is",round(area,2))
            break
        else:
            print("Invalid entry made, please enter a valid number")
            pass
    except:
        print("Invalid entry made, please enter a valid number")
