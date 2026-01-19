"""
'''Inheritance'''
class Animal:
    def speak(self):
        print("it makes a sound")

class Dog(Animal):
    def bark(self):
        print("dog bark")
d=Dog()
d.speak()
d.bark()

'''Multiple inheritance'''

class Father():
    def Driving(self):
        print("Father Enjoys Driving")
class Mother():
    def Cooking(self):
        print("Mother Enjoys Cooking")
class Child(Father, Mother):
    def Playing(self):
        print("Child Loves Playing")
c = Child()
c.Driving()
c.Cooking()
c.Playing()


'''Multilevel inheritance'''
class A:
    def a(self):
        print("A")
class B(A):
    def b(self):
        print("B")
class C(B):
    def c(self):
        print("C")

obj=C()
obj.c()
obj.b()
obj.a()
"""

'''Hierarchical inheritance'''
class Parent:
    def parent1(self):
        print("Parent1")

class Child1(Parent):
    def c1(self):
        print("Child1")

class Child2(Parent):
    def c2(self):
        print("Child2")

c1=Child1()
c1.c1()
c1.parent1()

c2=Child2()
c2.parent1()
c2.c2()