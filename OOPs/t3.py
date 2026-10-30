# Practice 1: Student Class
# Task: Student naam ki class banao.

# Requirements:
# 1. Constructor mein name, age aur grade receive karo.
# 2. self ke through values save karo.
# 3. show_details() method banao jo student ki details print kare.
# 4. Do objects banao:


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.grade)

b = Student("Sam",12,"A+")
n = Student("Saad", 32, "B")
m = Student("Saeed", 34, "A")

b.show_details()
n.show_details()
m.show_details()