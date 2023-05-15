x = str(input("Enter a number: "))
def sum_digits(x):
    sum = 0
    for i in x :
        sum= sum + int(i)
    return sum
print(sum_digits(x))

"""n=int(input("Enter a Number :"))
sum=0
while(n>0):
    i=n%10   # reminder value of division
    sum=sum+i
    n=n//10  # floor value of division
print("sum of digits in number=",sum)"""




