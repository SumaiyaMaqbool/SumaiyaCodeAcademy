#Q1
"""prime_numbers =  [2,3,5,7,11]
print (prime_numbers)"""
#--------------------------------------
#Q2
x = [22,3,-2,-1,10,1]
count = 0
product_all = 1
negative_count = 0
for elements in x:
    print (elements, end=" ")
    product_all = product_all*elements
    if (elements<0):
        negative_count= negative_count+1
    count = count +1
print ("\nTotal numbers of negative numbers : ",negative_count)
print ("\n", product_all)

#--------------------------
#Q3
print (x[-3:])
"""y= [3, 'a', 4,'b']
y.sort()"""
    
