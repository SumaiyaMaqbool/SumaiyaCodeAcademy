#Q1
slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1)
print (slope(5,6,2,4))
#Q2 Sorting a dictionary by age 
people= [{"name":"Jhon","Age":28},
        {"name":"Mary","Age":23},
        {"name":"Bob","Age":35},
        {"name":"Alice","Age":32}
        ]
sorted_list = sorted (people, key = lambda x:x['Age'])
print(sorted_list)
people.sort(key=lambda x:x['Age'])
print(people)
print(sorted(people, key=lambda x:x['Age']))
#Q3


