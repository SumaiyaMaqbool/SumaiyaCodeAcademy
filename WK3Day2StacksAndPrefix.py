class Stack:
    def __init__(self,stackList,expression):
        self.expression = expression
        self.stackList = stackList      
   
    def stack(self, stackList,expression):
        for i in range (len(expression)):
            if expression[i] == "^":
                stackList.append(expression[i])
                #var[i-1][i+1]=(expression[i-1],expression[i+1])
                print (stackList.pop(),expression[i-1],expression[i+1])                
                #character.append(expression[i-1]expression[i+1])
            elif expression[i] =="*" or expression[i]=="/":
                stackList.append(expression[i])
                print (stackList.pop(),expression[i-1],expression[i+1])
            elif expression[i]=="+" or expression[i]=="-":
                stackList.append(expression[i])
                print (stackList.pop(),expression[i-1],expression[i+1])

            else:
                continue 
        print (stackList)
                

stackList = []
character = []
var = []
x = Stack([],"a^b*c")
x.stack([],"a^b*c")
print(stackList)


""" def Input (self, string):
        string = string
        
        
    def Output():"""