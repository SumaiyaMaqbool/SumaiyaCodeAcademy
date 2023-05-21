class Employee:
    def __init__(self,emp_Id,emp_name,__emp_salary, emp_dep):
        self.emp_Id = emp_Id
        self.emp_name =emp_name
        self.__emp_salary = __emp_salary
        self.__emp_dep = emp_dep #by addign __ meaning we are changing the class instant from public to private
    def calculate_emp_salary(self,hoursWorked):
        if hoursWorked > 50:
            overtime = hoursWorked-50
            Overtime_amount = (overtime*(self.__emp_salary/50))
            return Overtime_amount
        else:
            return self.__emp_salary
            
        return __emp_salary
    def set_emp_assign_dep (self,newDep):
        self.__emp_dep = newDep
    def print_emp_details(self):
        return "employee name : {} employee ID : {} employee dep : {} employee salary : {}".format(self.emp_name,self.emp_Id,self.__emp_dep,self.__emp_salary)
    
emp1= Employee("E787","ADAMS",50000,"ACCOUNTING")
emp2= Employee("E7499","JONES",45000,"RESEARCH")
emp3= Employee("E7900","MARTIN",50000,"SALES")
emp4= Employee("E7698","SMITH",55000,"OPERATIONS")
print (emp1.print_emp_details())
print (emp2.print_emp_details())
print (emp3.print_emp_details())
print (emp4.print_emp_details())

emp4.set_emp_assign_dep("HR")
print (emp1.calculate_emp_salary(20))
print (emp2.calculate_emp_salary(50))
print (emp3.calculate_emp_salary(70))
print (emp4.calculate_emp_salary(30))




    
    
    
    
    