from ch07.myclass.calculator import Calculator

class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y

    def div(self):
        if self.y==0:
            return 0
        else:
            return self.x/self.y

cal=MoreCalculator(3,0)
print(cal.add())
print(cal.div())
print( cal.pow())
