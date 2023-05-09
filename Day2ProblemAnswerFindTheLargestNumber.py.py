'''x= input("Enter the first number: ")
x= int(x)
y= input("Enter Second Number : ")
y= int(y)
z= input("Enter Third Number : ")
z= int(z)
if(x==y==z):
        print ("The entered numbers are equal")
elif (x>y and x>z):
    print(x, " is the largest number")
elif(y>x and y>z):
        print(y, " is the largest number")
elif(z>x and z>y):
        print(z, " is the largest number")'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
largest = 0
if(num1==num2==num3):
    print ("The entered numbers are equal")
elif (num1 >= num2) and (num1 >= num3):
    largest = num1
    print("The largest number between", num1, ",", num2, "and", num3, "is", largest)

elif (num2 >= num1) and (num2 >= num3):
    largest = num2
    print("The largest number between", num1, ",", num2, "and", num3, "is", largest)

else:
    largest = num3
    print("The largest number between", num1, ",", num2, "and", num3, "is", largest)