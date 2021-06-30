class Calculator:
    def __init__(self):
        self.value=0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
        return self.value

class MaxLimitCalculato(Calculator):
    def add(self, val):
        self.value += val
        if self.value >100:
            self.value=100
        return self.value

c= Calculator()
c.add(10)
print(c.value)

cal2=MaxLimitCalculato()
print( cal2.add(50))
cal2.add(60)
print(cal2.value)