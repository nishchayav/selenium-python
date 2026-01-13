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




'''Built in Functions'''
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
"""


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