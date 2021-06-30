#class
class Person:
    def __init__(self):
        self.__name='강나'
        self.__age=30

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

p=Person()
#p.name='박바다'
print(p.getname(), p.getage())

