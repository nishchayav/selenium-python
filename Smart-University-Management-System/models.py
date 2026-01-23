from abc import ABC, abstractmethod
from descriptors import MarksDescriptor, SalaryDescriptor
from decorators import log_execution, time_it


class Person(ABC):
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Cleaning up {self.name}")


class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def get_details(self):
        return f"Name : {self.name}\nRole : Student\nDepartment: {self.department}"

    @log_execution
    @time_it
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def __gt__(self, other):
        return self.calculate_performance()[0] > other.calculate_performance()[0]


class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary, is_admin=False):
        super().__init__(fid, name, department)
        self._salary = salary
        self.is_admin = is_admin

    def get_details(self):
        return f"Name : {self.name}\nRole : Faculty\nDepartment: {self.department}"


class HeadOfDepartment(Faculty):
    """Multilevel Inheritance: HeadOfDepartment inherits from Faculty (which inherits from Person)"""
    def __init__(self, hid, name, department, salary, years_experience):
        super().__init__(hid, name, department, salary, is_admin=True)
        self.years_experience = years_experience

    def get_details(self):
        return f"Name : {self.name}\nRole : Head of Department\nDepartment: {self.department}\nExperience : {self.years_experience} years"


class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits
