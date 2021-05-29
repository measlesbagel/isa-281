#Cagle-Myles-HW
print("This program calculates the total surface area and volume of a cylinder.")
#Explains program
radius = float(input("Please enter radius: "))
#Creates radius value and allows user to input measurement
height = float(input("Please enter height: "))
#Creates height value and allows user to input measurement
pi = 3.1415925
#Sets value of PI
surfacearea = 2.0*pi*radius*(radius+height)
#Calculates value of surface area with given measurements
volume = pi*radius*radius*height
#Calculates value of volume with given measurements
print("Total surface area of a cylinder with a radius",radius,"and height",height,"=",round(surfacearea,2))
#Outputs the calculated value for surface area given the users measurements
print("Volume of a cylinder with a radius",radius,"and height",height,"=",round(volume,2))
#Outputs the caluclated value for volume given the users measurements

