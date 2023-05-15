#Q1
"""import math 
n = int(input("Enter the number of sides : "))
side = float(input ("Enter the side : "))
PI= (22/7)
def area (n, side):
    Area = 0
    if (n != 0):
        Area = float((n* (side**2))/(4*(math.tan(PI/n))))
        return Area
    else:
        print ("Invalid entry")
print (area (n, side))"""
#---------------------------------------------------------
#Q2
user_input = input("Enter something : ").lower()
def countVowels (user_input):
    allVolwes = 0
    a= 0
    o = 0
    i = 0
    u = 0
    e = 0
    for I in user_input:
        if (I == "a"):
            a = a + 1
        if (I == "o"):
            o = o + 1
        if (I == "i"):
            i = i +1
        if (I == "u"):
            u = u +1
        if (I == "e"):
            e = e+1
        
    if (a >= 0 and o >= 0 and i>= 0 and  u >= 0 and e >=0):
        allVolwes = a + o + i+ u+ e
        return allVolwes
    else:
        ("There is no volwe in ", user_input)    
print ("Number of volwes in ", user_input, ": ",str(countVowels (user_input)) )
