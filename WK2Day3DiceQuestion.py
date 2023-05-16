#sides = int(input ("Enter number of sides : "))
#probabilty = input ("Enter a number or Q to quit : ").lower()
def main():
    sides = int(input ("Enter number of sides : "))
    Count_Input = countInput(sides)
    printCounter(Count_Input)
    
def countInput(faces):
    lst = [0]*(faces+1)
    probabilty = int(input("Enter a number or 0 to quit : "))
    while(probabilty != 0):
        if(probabilty>=1 and probabilty<= faces):
            lst[probabilty]=lst[probabilty]+1
        else:
            print("the probabilty is out of range ")
        probabilty = int(input ("Enter a number or 0 to quit : "))
    return lst
            
def printCounter (lst):
    for i in range (1,len(lst)):
        print(i,":",lst[i])
    
                
             
    #probabilty = str(probabilty)
   
             
main()


        
        
        

"""entered_number = []
count = 0
while (probabilty != "q"):
    entered_number.append(probabilty)
    probabilty = input ("Enter a number or Q to quit : ").split()
    for i in entered_number:
        count[0] = count[0]+1
        print (j,":",counter[j])
            
            

    for i in range (sides+1):
        for j in probabilty:
            counter[j] =counter[j]+1
            j=j+1"""