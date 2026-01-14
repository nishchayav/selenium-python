'''Question: Iterators & Generators
1. Create a custom iterator class that iterates over numbers from 1 to N
2. Create a generator function that yields the first N Fibonacci numbers
3. Demonstrate the difference between using the iterator and generator by printing values using a for loop'''

"""
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

print("Using Iterator:")
for num in NumberIterator(10):
    print(num)



def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nUsing Generator:")
for num in fibonacci(10):
    print(num)
"""

'''Question: Descriptors	
Create a class Employee with attributes:	
name	
salary	
Implement a descriptor that:		
1. Ensures salary is always a positive number		
2. Raises a ValueError if a negative salary is assigned		
3. Demonstrates the descriptor by creating multiple Employee objects	'''

class SalaryDescriptor:
    def __get__(self, instance, owner):
        return instance._salary

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance._salary = value

class Employee:
    salary = SalaryDescriptor()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Nish", 50000)
emp2 = Employee("Vish", 65000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)


