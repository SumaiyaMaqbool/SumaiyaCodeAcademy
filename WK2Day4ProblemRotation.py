arrary={1,2,3,4,5}
left_rotation_time =input("Rotation times : ")

for i in left_rotation_time:
    first = arrary[0]
    for j in range (len(array)-1):
        array[j]=array[j+1]
    array[len(array)-1]= first
print ()
for m in array:
    print(array[m])