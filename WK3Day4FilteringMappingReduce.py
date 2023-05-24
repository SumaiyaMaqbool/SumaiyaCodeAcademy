from functools import reduce 
#Q1 Filtering positive numbers
"""numbers = [-1,0,4,-9,7,9,-9]
new_list = list(filter(lambda x:x>=0,numbers))
print(new_list)

#Q2 filtering the strings in the list that have lower cases
lst = ["Sumaiya","maqbool","bashir","Al","balushi"]
new_lst_1 = list(filter(lambda y:y.islower(),lst ))
new_lst_2 = list(filter(lambda z:z.isupper(),lst ))
new_lst_3 = list(filter(lambda m:m.isdigit(),lst ))
print(new_lst_1)
print(new_lst_2)
print(new_lst_3)"""

#Q3 Mapping a list names and converting them into upper cases
"""size_list = int(input ("Enter the length of your list: "))
lstt=[]
for i in range (size_list):
    names = input("Enter a name: ")
    lstt.append(names)
    NAMES = list(map(lambda n:n.upper(), lstt))
print (NAMES)"""

#Q4 Reduce function
num_size_list = int(input ("Enter the length of your list: "))
num = []
for i in range (num_size_list):
    numbs = int(input("Enter a number: "))
    num.append(numbs)    
numbrs = reduce(lambda x,q:x+q**2,num,0)
print (numbrs)

