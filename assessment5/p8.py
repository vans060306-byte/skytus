# 8. Teacher and Student Inheritance

class Teacher:
    def teach(self):
        print("Teaching")

class Student(Teacher):
    def study(self):
        print("Studying")

s = Student()
s.teach()
s.study()