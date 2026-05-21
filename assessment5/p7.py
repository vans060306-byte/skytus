# 7. Private Attributes with Getter and Setter

class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(90)
print(s.get_marks())