# 10. Use of super()

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

e = Employee("Vansh", 50000)
e.display()