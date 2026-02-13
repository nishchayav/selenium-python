import matplotlib.pyplot as plt


plt.plot([1,2,3],[4,5,6])
plt.show()



x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
plt.plot(x,y, marker="o",linestyle="--")
plt.xlabel("x- Axis")
plt.ylabel("y- Axis")
plt.title("Line Chart")
plt.grid(True)
plt.show()



names=["A","B","C","D","E","F"]
scores=[10,20,30,40,50,60]
plt.bar(names,scores)
plt.title("Bar Chart")
plt.show()
#horizontal
plt.barh(names,scores)
plt.show()


plt.scatter(x,y)
plt.show()



marks=[60, 65, 70, 75, 80, 85, 90, 95]
plt.hist(marks,bins=20)
plt.title("Histogram")
plt.show()



labels=["Chrome", "Edge", "Firefox"]
sizes=[20, 30, 40]
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()