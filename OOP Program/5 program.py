#Enhance your coding skills, start writing your code here!!
class Student:
    def __init__(self):
        self.__name = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 5 <= age <= 100:
            self.__age = age
        else:
            print("Invalid age. Age must be between 5 and 100.")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


name = input()
age = int(input())

s = Student()
s.set_name(name)
s.set_age(age)

print(f"Student Name: {s.get_name()}, Age: {s.get_age()}")
