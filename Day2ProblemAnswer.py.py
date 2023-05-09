x= input("Enter the first number: ")
x= int(x)
y= input("Enter Second Number : ")
y= int(y)
z= input("Enter Third Number : ")
z= int(z)
if (x>y and x>z):
    print(x, " is the largest number")
elif(y>x and y>z):
        print(y, " is the largest number")
elif(z>x and z>y):
        print(z, " is the largest number")
elif(x==y==z):
        print ("The entered numbers are equal")
