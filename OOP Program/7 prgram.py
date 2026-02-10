#Enhance your coding skills, start writing your code here!!
class Student:
    def __init__(self, name):
        self.__name = name
        self.__marks = None

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            self.__marks = "Invalid"

    def get_marks(self):
        return self.__marks

    def display_info(self):
        print(self.__name)
        print(self.__marks)


name = input()
marks = int(input())

s = Student(name)
s.set_marks(marks)

if s.get_marks() == "Invalid":
    print("Invalid Marks")
else:
    s.display_info()
