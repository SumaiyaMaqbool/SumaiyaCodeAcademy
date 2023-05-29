numbers =[[1,2,3],[4,5,6],[9,8,9]]
for i in range (3):
    for j in range (3):
        print(numbers[i][j],end=" ")
    print()
print()
x=(numbers[0][0]+numbers[1][1]+numbers[2][2])
y=(numbers[0][2]+numbers[1][1]+numbers[2][0])
print(numbers[0][0],"+",numbers[1][1],"+",numbers[2][2],"=",x)
print(numbers[0][2],"+",numbers[1][1],"+",numbers[2][0],"=",y)
print("|",x,"-",y,"|","=",abs(x-y))