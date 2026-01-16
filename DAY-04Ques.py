'''Question – Introduction to OOPs, Classes & Objects
Create a class Student that:
1. Has attributes name and roll_no
2. Has a method display_details() to print student information
3. Create at least two objects of the class and display their details'''


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)


stu1 = Student("Nish", 101)
stu2 = Student("Vish", 102)

stu1.display_details()
print()
stu2.display_details()
