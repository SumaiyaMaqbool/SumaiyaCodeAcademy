temp = float (input ("Enter and temprature "))
temp_type = str(input ("Enter C for Celisus or F for Fahrenheit ")).lower()


if (temp_type=="c" ):
    print ("Entered Temprature is in Celsius: ", temp, temp_type)
    temp_in_F =float (temp*(9/5)+32)

    print ("Entered Temprature is in Fahrenheit will be: ", temp_in_F,"F" )
    
elif(temp_type=="f"):
    print ("Entered Temprature is in Fahrenheit: ", temp, temp_type)
    temp_in_C = (temp-32)*(5/9)

    print ("Entered Temprature is in Celsius will be: ", temp_in_C, "C")
else:
    print("Invalid Entry")
    