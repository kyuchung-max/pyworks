#car class, taxi와 bus 자식

class Car:
    def drive(self):
        print('차가 주행')

class Taxi(Car):
    def drive(self):
        print('택시가 주행')

class Bus(Car):
    def drive(self):
        print('버스가 주행')

c=Car()
c.drive()

taxi=Taxi()
taxi.drive()

b=Bus()
b.drive()