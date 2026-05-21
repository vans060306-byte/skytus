# 5. Polymorphism with Shapes

class Circle:
    def area(self):
        print("Area of Circle")

class Rectangle:
    def area(self):
        print("Area of Rectangle")

def find_area(shape):
    shape.area()

c = Circle()
r = Rectangle()

find_area(c)
find_area(r)