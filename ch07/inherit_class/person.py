class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #def showinfo(self):
class Employee(Person):
    pass

if __name__=='__main__':
    p1=Person('a',25)
    print(p1.name,p1.age)

    e1=Employee('b',30)
    print(e1.name,e1.age)

    e2=Employee('c',33)
    print(e2.name,e2.age)