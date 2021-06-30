#student class
class Student:
    def __init__(self,sid,name):
        self.sid=sid
        self.name=name
    def showinfo(self):
        print(self.sid, self.name)
if  __name__ == "__main__":
s1=Student(1001,'aa')
s1.showinfo()
s2=Student(1002, 'bb')
s2.showinfo()