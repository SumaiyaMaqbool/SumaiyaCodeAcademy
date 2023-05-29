x = [1,4,5,7,3,0]

for i in range(len(x)-1,0,-1):
    j= i-1    
    if i>=j:
        print (x[i], end= " ")
    if  max(x) == x[i]:
        break
print()   
print("---------------------------")

y = [1,2,3,4]

for k in range(len(y)-1,0,-1):
    m= k-1    
    if k>=m:
        print (y[k], end= " ")
    if  max(y) == y[k]:
        break

        
   
        
        