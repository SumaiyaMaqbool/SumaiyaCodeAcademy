#Q1
i= 0
count = 0
while count<10:
    if(i%2==0):
       count +=1
       print(i)
    i = i+1


'''-------------------------------------------------------------------'''
#Q2
x= 0
countx = 0
while countx<10:
    countx +=1
    x +=1
    y=x**2
    print(y)
'''------------------------------------------------------------------------'''

# Q3

number = 105
seq= 7

while number >= seq:
    print(number)
    number = number - seq
   

'''------------------------------------------------------------------------'''
#Q4
user_input = str(input ("Enter something: "))
length_user_input = len(user_input)
count = 0

#user_input = list(user_input)
while (count < length_user_input ):
    print ("The ASCII decimal for ", user_input[count], "is/are", ord(user_input[count]))
    count+=1


# ---------------------------------------------------------------------

#Q5

number_input= int(input("Enter a number "))
count = 0
while (True):
    count = count +1
    if(number_input%count==0):
        print(number_input, " is divisable on ", count)

    


    
    
   

    
