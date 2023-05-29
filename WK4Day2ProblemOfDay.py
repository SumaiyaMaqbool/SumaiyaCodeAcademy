def Multiples(num,length):
    count = 0
    lst = []
    while len(lst)<length:
        #for x in range (num, len(lst)):
            count = count+num
            lst.append(count)
    #if len(lst)==7:
        #break
        #print(len(lst))
    print(lst)
        
        
Multiples(3,7)
print("--------------------------------")
Multiples(10,4)
