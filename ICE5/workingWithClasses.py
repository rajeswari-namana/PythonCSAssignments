class Employee():
    Empcount= 0
    def _init_(self):
        pass

    def Empname(self,name):
        self.name=name
        return self.name

    def Empsal(self,salary):
        self.salary=salary
        return self.salary

    def EmpDisplay(self,nam,sal):
        self.Empname(nam)
        self.Empsal(sal)
        print(self.name)
        print(self.salary)
        self.Empcount= self.Empcount + 1
        print(self.Empcount)

emp1=Employee()

emp1.EmpDisplay('RAJI',50000)
emp1.EmpDisplay('esha',50000)

class Manager(Employee):
    pass

emp3=Manager()
emp3.EmpDisplay('swetha',45000)









