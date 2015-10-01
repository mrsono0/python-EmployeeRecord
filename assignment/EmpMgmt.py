__author__ = 'gunner'
class Employee:
    name = ""
    emp_num = 0
    department = ""
    dob = ""
    join_date = ""
    salary = 0.0

    def __init__(self,name,emp_num,department,dob,join_date,salary):
        self.name = name
        self.emp_num = emp_num
        self.department = department
        self.dob = dob
        self.join_date = join_date
        self.salary = salary

    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

    def setEmp_num(self,emp_num):
        self.emp_num = emp_num
    def getEmp_num(self):
        return self.emp_num

    def setDepartment(self,department):
        self.department = department
    def getDepartment(self):
        return self.department

    def setdob(self,dob):
        self.dob = dob
    def getdob(self):
        return self.dob

    def setjoin_date(self,join_date):
        self.join_date = join_date
    def getjoin_date(self):
        return self.join_date

    def setSalary(self,salary):
        self.salary = salary
    def getSalary(self):
        return self.salary

e1 = Employee('rajesh',101,'DBA','1990-01-04','2014-01-01',11000)
print "Employee Name : ", e1.getName()

