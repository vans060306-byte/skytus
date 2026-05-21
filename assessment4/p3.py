# 3. Student Class

class Student:
    def __init__(self, marks):
        self.marks = marks

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        print("Average:", avg)

s = Student([80, 90, 70])
s.average()