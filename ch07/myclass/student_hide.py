#student class
class Student:
    def __init__(self,sid,name):
        self.__sid=sid
        self.__name=name

    def getsid(self):
        return self.__sid

    def getname(self):
        return self.__name

s1=Student(1,'a')
print(s1.getsid(), s1.getname())