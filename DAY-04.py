
'''Constructors & Destructors'''
class employee:
    def __init__(self,name):
        self.name=name
        print("Contructor is called")

    def __del__(self):
        print("Destructor is called")

e=employee("Nish")


'''Class'''
class student:
    def display(self):
        print("This is student class")

s1 = student()
s1.display()

class calculator:
    def add(self, a, b):
        print("sum:", a + b)

c = calculator()
c.add(100, 300)



'''Abstract Class'''

from abc import ABC,abstractmethod

class shape(ABC):
    def display(self):
        print("normal method")
    @abstractmethod
    def area(self):
        pass

class reactangle(shape):
    def area(self):
        print("area method implemented")


r=reactangle()
r.area()
r.display()



'''Abstract Based Class constructor'''
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print(self.name, "Salary is 350000")

m=Manager("Nish")
m.salary()



'''Multiple Abstract Class constructor'''
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass
class SBI(Bank):
    def interest(self):
        print("Interest is 6%")
    def loan(self):
        print("Loan is available")

s=SBI()
s.interest()
s.loan()
