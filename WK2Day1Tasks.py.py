#Q1
"""string = input ("Enter phone in format (XXX)XXX-XXXX: ")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
    if position ==0:
        valid = string [position] == "("
    elif position ==4:
        valid = string [position] == ")"
    elif position ==8:
        valid = string [position] == "-"
    else:
        valid = string[position].isdigit()
    position = position +1
    
if valid:
    print("The string contains a valid phone number")
else:
    print ("The string does not contains a valid phone number")"""
#Q2          
"""password = input("Enter a password:")
length_password = len(password) >=8
position_l = 0
position_u = 0
position_sp = 0
position_n = 0
if(length_password):
    for i in password:
        if (i.islower()):
            position_l += 1
        if (i.isupper()):
            position_u+=1
        if (i=="@" or i=="#" or i=="$" or i=="_"):
            position_sp +=1
        if (i.isdigit()):
            position_n +=1
            
if (position_l >=1 and position_u >=1 and position_sp>=1 and position_n>=1):
    print (password,"valid password")
else:
    print(password, "invalid password")"""
    
    
#Q3 from Dr.Sultan on default value in functions
def number(x=3,y=8):
    z = x + y
    print (z)

#print(number(2,))
#print (number(5))
    
    
      
 
    