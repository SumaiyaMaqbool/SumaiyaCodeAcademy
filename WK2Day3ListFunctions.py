x= ['1','2','3']
#y=[4,5]
#x.extend(y)
for i in x:
   y= "|".join(x)
print(y)
# list comprehension
result = []
for i in range(5):
    result.append(i**2)
print (result)
# the above one is exactly same as the down one but the down one is shorter 
result = []
result = [i**2 for i in range (5)]
print(result)
# list comprehension for if statement
result1 = []
result1 = [i for i in range (5) if i%2==0]
print(result1)
   
