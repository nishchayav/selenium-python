from functools import reduce

for i in range(1,21):
    print(i)

num=range(1,21)
print(num)
for i in range(1,21):
    print(i)



'''Write a Python program that:
1. Uses range() to generate numbers from 1 to 20
2. Uses filter() with a lambda to select only even numbers
3. Uses map() with a lambda to square the filtered numbers
4. Uses reduce() to calculate the sum of squared even numbers
5. Uses enumerate() to print the index and value of the final result list'''


num=range(1,21)
print(num)

evenum=filter(lambda x: x%2==0,num)

sqrnum=list(map(lambda x: x**2,evenum))
print(sqrnum)

totsum=reduce(lambda x,y: x+y,sqrnum)

for index, value in enumerate(sqrnum):
    print(f"Index {index},Value {value}")

print("sum of squared even numbers: ",totsum)





'''	Given a list:	data = [1, 2, 3, 4, 5, 6, 2, 4]
Write a program to:
1. Create a list comprehension to store squares of all numbers
2. Create a set comprehension to store only unique even numbers
3. Create a dictionary comprehension where the key is the number and the value is its cube'''


data=[1,2,3,4,5,6,2,4]
sqrlist= [x**2 for x in data]
print(sqrlist)

evenset={
    x for x in data if x%2 ==0
}
print(evenset)

cubedic={
    x: x**3 for x in data
}
print(cubedic)
