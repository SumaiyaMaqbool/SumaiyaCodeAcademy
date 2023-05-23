lst=[]
def insertionSort(array):
    for step in range (1, len(array)):
        key = array[step]
        j= step -1
        
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j=j-1
        array[j+1] = key
        
array = ["Said,25","Majid,19","Salim,32","Ali,21","Sultan,28"]
New_array = []
digit =  "0123456789"
for x in array:
    p=""
    for y in x:
        if y in digit:
            p+=y
    New_array.append(int(p))
yx=[]
yx.extend(New_array)
insertionSort(New_array)
print(yx)
array_final = []
for k in New_array:
    array_final.append(array[yx.index(k)])
    
lst=[]
for names in range( len(array_final)):
        z=array_final[names].split(',')
        lst.append(str(z[0]))
print(lst)

        
