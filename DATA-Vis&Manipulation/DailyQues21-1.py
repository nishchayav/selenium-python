"""Question: Given the following dataset of monthly sales:
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]
Plot a line chart of monthly sales using Matplotlib.
Using Seaborn, create a bar plot for the same dataset.
Customize the plots with title, x - axis label, y-axis label, and grid lines."""

import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]
plt.plot(months,sales, marker="o",linestyle="--")
plt.xlabel("x- Axis")
plt.ylabel("y- Axis")
plt.title("Line Chart")
plt.grid(True)
plt.show()
