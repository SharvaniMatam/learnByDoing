class Employee:
    companyName="Google India Pvt Ltd"
    def __init__(self,name,employeeid,salary):
        self.name=name
        self.employeeid=employeeid
        self.salary=salary
    def getEmployeesalary(self):
        return "Employee salary :"+str(self.salary)
    def getEmployeename(self):
        return "Employeename :"+str(self.name)

emp1=Employee("pandu",8880,90000)
emp2=Employee("raja",9959,95000)
print(emp1.companyName,emp1.getEmployeesalary(),emp2.getEmployeename())