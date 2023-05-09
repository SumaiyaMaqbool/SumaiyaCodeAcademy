# constants

PI = float(22/7)

Raduis = input("Enter the raduis of your cylinder : ")

r  = float(Raduis)

Height = input("Enter the height of your cylinder: ")

h = float(Height)

Area_Of_Cylinder = 2*PI*r*(r+h)

Volume_Of_Cylinder = PI*(r**2)*h

print("Your cylinder's area is :", format((Area_Of_Cylinder), '.2f'))
print ("Your cylinder's volume is :", format((Volume_Of_Cylinder), '.2f'))




