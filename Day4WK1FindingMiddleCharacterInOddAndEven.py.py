user_string = input("Enter something ")
user_string_length = int(len(user_string))

if(user_string_length%2!=0):
    middle_string = int((user_string_length)/2)
    print ("the middle character from your input is: ",user_string[middle_string])
elif(user_string_length%2==0):
    first_middle_string = int((user_string_length)/2)
    second_middle_string = int((first_middle_string) +2)
    print ("the two middle characters from your input are: ",user_string[first_middle_string : second_middle_string])
else:
    print("Invalid Entry")


