# 1. Car Class

class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed:", self.speed)

    def brake(self):
        self.speed -= 10
        print("Speed:", self.speed)

car = Car("Toyota", "Fortuner")
car.accelerate()
car.brake()