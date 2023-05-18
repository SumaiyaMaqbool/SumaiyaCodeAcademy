file = open("Document.txt","r")
dsalary  = 0
highest = 0
i=0
employee={}
salary = []
for line in file:
    data = line.split()
    salary.append(float(data[0]))
    employee[data[1]] = data[0]
print(employee)
print(salary)
avg = sum(salary)/len(salary)
print(avg)
x=max(salary)
for key in employee:
    if (float(employee[key])==x):
        print(key)
file.close()
    
# Convert the list into a dictionary
#values = {line[0]:line[i] for i in range (len(line))}
    
    