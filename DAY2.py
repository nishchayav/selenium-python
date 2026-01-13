"""
'''wap to check if you're eligible to vote'''

x=int(input("enter the number"))
if x>=18:
    print("you're eligible to vote")
else:
    print("you're not eligible to vote")



'''Arithmetic Operators'''

x=int(input("enter the number"))
y=int(input("enter the number"))
print("addition",x+y)
print("subtraction",x-y)
print("multiplication",x*y)
print("division",x/y)
print("exponent or power",x**y)
print("remainder",x%y)




'''Builtin Functions'''
import math
x=int(input("enter the number"))
print("square root of",x,"is :",math.sqrt(x))



'''Strings'''
x=input("enter youw own string")
print(x[0])
n=int(input("enter the number of places of where you want the letter"))
print(x[n])

a='''Hello
welcome
to
python'''
print(a[0])
print(a[-5])
print(a[-1])
print(a)

text="Python"
print(text[0:3])
print(text[2:])
print(text[:3])
print(a+text)

print("Hi" *3)

print(text.upper())
print(a.replace("python","java"))



'''Lists'''
num=[10,20,30,40,50]
name=['Nish','Vish','Sish','Tish']
mixed=[10,'Nish',20,'Vish']

num[1]=100
print(num)
print(name)
print(mixed)
for i in num:
    print(i)

if 10 in num:
    print("Found")

matrix=[[1,2,3],[4,5,6]]
print(matrix[1][2])

name.reverse()
print(name)

name.append("Hish")
print(name)

name.extend(["Xish","Bish"])
print(name)

name.remove("Hish")
print(name)

name.insert(3,"Kish")
print(name)


'''Tuples'''
tup1=(10,20,30,40,50,30)
tup2="apple","banana","lemon"
print(tup1[0])
print(tup2[1])
print(tup1[:2])
print(tup1[4:])
print(tup1)
print(tup1.count(30))
print(tup1.index(40))

#reverse num
b=10
a,b=b,a
print(a,b)

data=10,20,30
a,b,c=data
print(a,b,c)



'''Dictionary'''

student={
    "name": "Nishchaya",
    "age": 23,
    "course": "Python"
}

print(student)
print(student["name"])
print(student.get("age"))

student["marks"]=85
student["age"]=24
print(student)
print(student["name"])
print(student.get("age"))
student.pop("age")
print(student)
student.popitem()
print(student)

print(student.keys())
print(student.values())


for key in student:
    print(key,student[key])

if "name" in student:
    print("key exists")

employees={
    101:{"name":"xyz","salary":2000},
    102:{"name":"zyx","salary":2000},
}
print(employees[101]["name"])




'''Sets'''
myset={1,2,3,4,5,3,2,1,6}
print(myset)

for i in myset:
    print(i)
myset.add(100)
print(myset)


A={1,2,3}
B={3,4,5}

print(A|B)
print(A&B)
print(2 in A)

"""

'''if else elif conditions'''
num=int(input("enter the number"))
if num%2==0:
    print("Even")
else:
    print("Odd")


marks=int(input("enter your marks upto 100"))

if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")


j=0
while j<=5:
    print(j)
    j+=1
    if j==2:
        break

day=int(input("enter the day"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 4:
        print("Friday")
    case 4:
        print("Saturday")
    case 4:
        print("Sunday")
