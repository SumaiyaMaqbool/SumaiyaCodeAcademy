from math import *  # this is a way to import all the function from the math library as using the *
a=2
b= 5
n= 2
r= 1
t=10

print(b*((1+r/100)**n))
print(b*1+r/100**n)
print((7*(10-5)%3)*4+9)

print(sqrt((a**2)+(b**2)-2*a*b*cos(t)))


price = 4.35
Q = 100
total =price * Q
total = int(total * 100)/100.0 # this is  code to keep the decimal values wihtout rounding it  
print(format(total, '.2f' ))
