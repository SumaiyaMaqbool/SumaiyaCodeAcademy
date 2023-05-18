#Q1
"""file = open("SpeedAndTime.txt","r")
speed = []
time =[]
for line in file:
    data = line.split()
    speed.append(int(data[0]))
    time.append(int(data[1]))
    distance = [speed[i]*time[i] for i in range (len(speed))]
print(speed)
print(time)
print (distance)    
file.close()"""

#Q2
file = open("Numbers.txt","r")
numbers = []
factors = []
count = 1
for lines in file:
    number = int(lines.rstrip())
    print(number)
    #numbers.append(int(data[0]))
    for i in range(1,number+1):
        #while True :
            if number%i==0:
                factors.append(i)
    print(factors)
    factors =[]
    
file.close()
