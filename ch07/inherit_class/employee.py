
from person import Person

class Employee(Person):
    def __init__(self,name,age,empid):
        super().__init__(name,age)
        self.empid=empid

    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getempid(self):
        return self.empid

e1=Employee('g',20,201)
print(e1.getname(),e1.getage(),e1.getempid())

e2=Employee('t',50,501)
print(e2.name,e2.age,e2.empid)
