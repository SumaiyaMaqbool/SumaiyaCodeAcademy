#Q1
"""x= [[1,2,3],
    [4,5,6]]

for i in range (2):
    for j in range (3):
        print(x[i][j], end=" ")
    print()


#Q2
n = [[]*3 for x in range (3)]
for i in range (3):
    for j in range(3):
        count= i+1
        n[i].append(count)
    
print(n)
for elements in n:
    for item in elements:
        print (item, end=" ")
    print()"""
    
    
#Q3
"""
row = int(input ("Enter number of rows : "))
col = int(input ("Enter number of coloums : "))
lst = [[0]*col for x in range(row)]

for i in range (row):
    for j in range(col):
        value = input("enter something : ")
        lst[i][j]=value
print (lst)
for elements in lst:
    for item in elements:
        print (item, end=" ")
    print() """
#Q4
"""m = [[0]*4 for x in range(4)]
for i in range(4):
    for j in range(4):
        if(i==j):           
            m[i][j]=1
        elif(i>j):            
            m[i][j]=2
        else:            
            m[i][j]=0   
print(m)
for elements in m:
    for item in elements:
        print (item, end=" ")
    print()"""
#Q5
y = [[0]*4 for x in range(4)]
for i in range(4):
    for j in range(4):
        if(i==j):           
            y[i][j]=1
        elif((i+j)%2==0 ):            
            y[i][j]=1
        else:            
            y[i][j]=0   
print(y)
for elements in y:
    for item in elements:
        print (item, end=" ")
    print()    
    









    