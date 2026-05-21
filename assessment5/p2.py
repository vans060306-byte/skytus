# 2. Vehicle -> Car -> ElectricCar

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Electric car charging")

e = ElectricCar()
e.start()
e.drive()
e.charge()