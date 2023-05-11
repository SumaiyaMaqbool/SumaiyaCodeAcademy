import math 
points =[[-10,20,-10,-18],[-10,20,0,3],[0,3,8,17],[8,17,10,-16],[16,-16,-10,-18]]

s1=points[0]
s2=points[1]
s3=points[2]
s4=points[3]
s5=points[4]

vectors = ["s1","s2","s3","s4","s5"]
vectors_string = vectors
x1=[s1[0],s2[0],s3[0],s4[0],s5[0]]
y1=[s1[1],s2[1],s3[1],s4[1],s5[1]]
x2=[s1[2],s2[2],s3[2],s4[2],s5[2]]
y2=[s1[3],s2[3],s3[3],s4[3],s5[3]]

y_coordintor = [y1,y2]
count = 0

print ("Vector\t\tLength\t\tSlop")

while (count<len(vectors)):
    length_sector =math.sqrt((x2[count] - x1[count])**2+(y2[count] -y1[count])**2)
    if ((x2[count]- x1[count])==0):
        slop = "NA"
    else:
        slop = (y2[count]- y1[count])/(x2[count]- x1[count])
        slop = format(slop,".1f")

    print(vectors[count],"\t\t", format(length_sector, ".1f"),"\t\t",slop)
    count = count+1
y_max = max(y_coordintor)
print("y max = ", y_max[0] )
y_min = min(y_coordintor)
print("y min = ", y_min[0])