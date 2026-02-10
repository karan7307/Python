#Enhance your coding skills, start writing your code here!!
class Student:
    def __init__(self):
        self.__grade = None

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
            print(f"Grade set to: {self.__grade}")
        else:
            print("Grade must be between 0 and 100.")

    def get_grade(self):
        return self.__grade


grade = int(input())

s = Student()
s.set_grade(grade)
