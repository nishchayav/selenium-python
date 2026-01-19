'''Question – Class Types & Inheritance
1.Create a base class Vehicle with a method start()
2. Create a derived class Car that inherits from Vehicle
3.Add a class variable to track the number of vehicles created
4.Demonstrate single inheritance and multilevel inheritance with appropriate classes'''

class Vehicle:
    veh_count = 0

    def __init__(self):
        Vehicle.veh_count += 1

    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def drive(self):
        print("Car is being driven")
class ElectricCar(Car):
    def __init__(self):
        super().__init__()

    def charge(self):
        print("Electric car is charging")
v = Vehicle()
c = Car()
e = ElectricCar()

v.start()
c.start()
c.drive()
e.start()
e.drive()
e.charge()
print("Total vehicles created:", Vehicle.veh_count)



'''Question – Polymorphism(Method & Operator Overloading)
1. Create a class Calculator that demonstrates method overriding
2. Create another class AdvancedCalculator that overrides a method from Calculator
3. Implement operator overloading by overloading the + operator to add two objects of a custom class'''

class Calculator:
    def calculate(self, a, b):
        return a + b

class AdvCalculator(Calculator):
    def calculate(self, a, b):
        return a * b

c = Calculator()
ac = AdvCalculator()

print(c.calculate(5, 3))    # Parent version
print(ac.calculate(5, 3))   # Child overridden version
