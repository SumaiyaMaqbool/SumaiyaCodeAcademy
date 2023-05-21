
from datetime import date
#Q1
"""try:
    file = open("numbetrs.txt","r").read()   

except Exception as exception:
    print (exception)"""
#Q2
"""class Person:
    # to count number of objects 
    no_of_persons = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.no_of_persons =+ 1
    def __str__(self):
        # small f down below is for formatting
        return f"This person name is {self.name} and {self.age} years old"
        #another correct way for formatting
        #return "This person name is {} and {} years old".format(self.name,self.age)

    
p1 = Person("Hamza", 22)
p2 = Person("Ali", 32)
print (p1)
print (type(p1))
print(Person.no_of_persons)
p1.age=25 # using this way to change the value of the age it kinds of constract with the capsulation method in classes and hence it is wrong and the best way to have another class for the age changing 
print(p1.__str__())"""
#Q3
class Person:
    # to count number of objects 
    no_of_persons = 0
    def __init__(self,name,age,address, hours):
        self.name = name
        self.age = age
        self.address = address
        self.hours = hours
    def class_type (self):
        return "This is Parent class "
class Student (Person):
    def __init__(self,name,age,address,hours,grades):
        super().__init__(name,age,address,hours)
        self.grades = grades
    def class_type (self):
        return "This is Student class "
    @classmethod
    def new_student(cls,name,birth_year,address,hours,grades):
        return cls(name,date.today().year-birth_year,address,hours,grades)
s1 = Student("Salim", 23, "Muscat", 180, [3.1,2.5,2])
p1 = Person("Salim", 23, "Muscat", 180)
s3 = Student.new_student("Salim", 1993, "Muscat", 180, [3.1,2.5,2])
print(s3.age)

print (p1.class_type())
print(s1.class_type())















"""
        Person.no_of_persons =+ 1
    def __str__(self):
        # small f down below is for formatting
        return f"This person name is {self.name} and {self.age} years old"
        #another correct way for formatting
        #return "This person name is {} and {} years old".format(self.name,self.age)

    
p1 = Person("Hamza", 22)
p2 = Person("Ali", 32)
print (p1)
print (type(p1))
print(Person.no_of_persons)
p1.age=25 # using this way to change the value of the age it kinds of constract with the capsulation method in classes and hence it is wrong and the best way to have another class for the age changing 
print(p1.__str__())"""


