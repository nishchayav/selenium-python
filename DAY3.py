"""
'''Functions'''

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

print(add(20,40))                   #print shows output, return gives output back to the caller
print(sub(20,40))

def sub2(a,b):
    return a-b,a
print(sub2(20,40))



def hello(greeting="Hello", name="world"):
    print('%s,%s'%(greeting,name))

hello()
hello('greetings','nish')


def printpara(*para):            #*args collects all positional arguments
    print(para)                    #Stores them in a tuple: “I don’t know how many values the user will pass.”

printpara('testing')
printpara(1,2,3,4,5)

def printpara1(**para):            #**kwargs collects key=value arguments
    print(para)                     #Stores them in a dictionary

printpara1(x=1,y=2,z=3)




'''Modules'''
import math as m

print(m.pi)
print(m.sqrt(90))



'''Class'''
class Student:
    name='nish'
    age=23

s1=Student()
print(s1.name)
print(s1.age)


class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

e1=Employee('nish',23)
print(e1.name,e1.age)


from itertools import count

'''Iterator'''
data=[1,2,3,4,5,6,7,8,9]
it=iter(data)
print(next(it))
print(next(it))


class count:
    def __init__(self,limit):
        self.limit=limit
        self.current=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<self.limit:
            val = self.current
            self.current+=1
            return val
        else:
            raise StopIteration

object=count(20)

for num in object:
    print(num)




''Generators''

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4

gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))


'''Files'''

#TXT
file=open("nishchayavishwakarma.txt","r")
content=file.readline()
print(content)
file.close()

file=open("nishchayavishwakarma.txt","a")
file.write("adding something init")
file.close()

file=open("nishchayavishwakarma.txt","w")
file.write("Hello guys\n")
file.write("This is my write example")
file.close()

#CSV
import csv
with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","ID","Age"])
    writer.writerow(["Nish",1,20])
    writer.writerow(["Vish", 2, 21])
    writer.writerow(["Shish", 3, 22])

#JSON
import json
data = {
    "Name": "Nish",
    "Age": "23",
    "Location": "Bhopal",
    "Skills": ['SQL', 'Python', 'HTML']
}
with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)


#XML
import xml.etree.ElementTree as ET

root=ET.Element("employee")
emp1=ET.SubElement(root,"emp")
ET.SubElement(emp1,"id").text="101"
ET.SubElement(emp1,"Name").text="Nish"
ET.SubElement(emp1,"Salary").text="300000"
emp2=ET.SubElement(root,"emp")
ET.SubElement(emp2,"id").text="102"
ET.SubElement(emp2,"Name").text="Vish"
ET.SubElement(emp2,"Salary").text="200000"

tree=ET.ElementTree(root)
tree.write("employee.xml")
print("xml file written successfully")



'''Decorators'''
def mydecorator(func):
    def wrapper():
        print("Before Function Call")
        func()
        print("After Function Call")
    return wrapper

@mydecorator
def sayhello():
    print("Hello")
sayhello()



'''Descriptors'''
class mydescriptor:
    def __get__(self, object, owner):
        print("Getting Value")
        return object._x
    def __set__(self, object, value):
        print("Setting Value")
        object._x = value

class Test:
    x=mydescriptor
t=Test()
t.x=10
print(t.x)

"""

'''Enumurators'''
fruits=['apple','banana','orange','papaya','lemon']
for index, value in enumerate(fruits):
    print(index, value)
