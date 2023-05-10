year_entered = int(input("please enter the year which you want to check if it is the leap year: "))

if ((year_entered%4==0) or (year_entered%400==0)):
    print(year_entered, " is a leap year")
else:
    print (year_entered, " is not a leap year")