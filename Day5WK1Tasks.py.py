# Q1
# stateName = "Virginia"
# for letter in stateName:
#     print(letter, end='')
#     
  
# -----------------------------------------
# Q2
total =  0.0
count = 0
inputStr = int(input("Enter a number or press enter to quit :"))

for value in range(inputStr+1) :
    if (inputStr !=""):
        value = float(inputStr)
        total = total + value
        inputStr = input("Enter a number or press enter to quit :")
        count = count +1
          
        
if (count > 0):
    average = total/count
    print ("average = ", average)
else:
    average = 0.0
