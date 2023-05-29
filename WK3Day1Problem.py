arr=[1,8,7,4,1,2,2,2]
def most_frequent(arr):
    return max(set(arr), key = arr.count)
print(most_frequent(arr))