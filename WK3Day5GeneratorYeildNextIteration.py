#Q1 from a lecture
#add another function for num**3 and then combine the square and x as defined below together

def fibonacci_numbers(numbs):
    x,y = 0 ,1
    for i in range (numbs):
        x,y = y, x+y
        yield x
        
def square(numbs):
    for i in numbs:
        yield i**2

def x(numbs):
    for j in numbs:
        yield j**3
        
print(sum(square(fibonacci_numbers(10))))
print(sum(square(x(fibonacci_numbers(10)))))

#Q2

def y():
    yield 1
    yield 2
    yield 3
    yield 4
value=y()
print(next(value))
for i in value:
    print(i)
print()    
    
#Q3 Exercise from a lecture
def number(lst):
    for i in lst:        
        if i%2==0:
            yield i
lst= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
number1= number(lst)
for n in number1:
    print(n)   

    

    