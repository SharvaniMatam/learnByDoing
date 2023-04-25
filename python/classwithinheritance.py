class Employee:
  companyName = "CTS Pvt Ltd"

  def __init__(self, name, age, employeeId):
    self.name = name
    self.age = age
    self.employeeId = employeeId

  def getEmployeeDetails(self):
    return "Name : " + self.name + ", Employee Id : " + str(self.employeeId) + ", Company Name : " + Employee.companyName


class ItTeam(Employee):
  reportingManger = 'Bhargavi'

  def __init__(self, name, age, employeeId):
    super().__init__(name, age, employeeId)
  

class EngineeringTeam(Employee):
  reportingManger = "Bhargavi"

  def __init__(self, name, age, employeeId):
    super().__init__(name, age, employeeId)

  def getMyWork(self):
    return " => I work as programmer"

class MangementTeam(Employee):
  def __init__(self, name, age, employeeId):
    super().__init__(name, age, employeeId)


  def checkCompanyPerformance(self):
    return " Done "


it1 = ItTeam("keerthi",40,34440)
eEmp1 = EngineeringTeam('akhila', 35, 4500)
mEmp1 = MangementTeam('Sunny', 55, 12)

print(it1.getEmployeeDetails())
print(eEmp1.getEmployeeDetails(),

 eEmp1.getMyWork())


print(mEmp1.getEmployeeDetails(), mEmp1.checkCompanyPerformance())
