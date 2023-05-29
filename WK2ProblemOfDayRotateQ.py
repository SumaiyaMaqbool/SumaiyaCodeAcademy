#Rotate an array
array = [1,2,3,4,5]
left_rotation_time = 2
len_array = len(array)
new_array = array[left_rotation_time:]+array[:left_rotation_time]
print (new_array)
