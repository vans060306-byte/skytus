# 8. Laptop Class

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, percent):
        self.price -= self.price * percent / 100
        print("New Price:", self.price)

l = Laptop("HP", 50000)
l.discount(10)