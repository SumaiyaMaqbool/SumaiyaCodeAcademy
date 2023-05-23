#Q1 reverse answer 1

class Stack:
    def __init__(self,st):
        self.st = st
    def string_without_reverse(self,st):
        stack = []
        for i in range (len(st)):
            stack.append(st[i])
        print(stack, end="")      
        
    def string_with_reverse(self,stack):
        for j in range(len(stack)):
            print(stack.pop(),end="")
            
        
stack = ['W', 'e', 'l', 'c', 'o', 'm', 'e']        
word=Stack(stack)
word.string_with_reverse(stack)


#Q1 reverse answer 2
class Stack:
   
    def __init__(self,st,stack):
        self.st = st
        self.stack = stack
    def string_without_reverse(self,st,stack):        
        for i in range (len(st)):
            stack.append(st[i])
        print(stack, end="")
        print()
        
    def string_with_reverse(self,stack):
        for j in range(len(stack)):
            print(stack.pop(),end="")
            
        
#stack = ['W', 'e', 'l', 'c', 'o', 'm', 'e']
stack = []
word=Stack("Welcome",stack)
word.string_without_reverse("Welcome",stack)
word.string_with_reverse(stack)