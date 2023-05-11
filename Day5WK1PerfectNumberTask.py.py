count = 0
for i in range(101):
    h = i+i
    if(i%2==0 and h==i):
        count = count +1
        print(i, " is a perfect number", h, end ="  " )
        count = count +1

    #number_input= int(input("Enter a number "))
#     print(number_input, " is divisable on ", count)

#