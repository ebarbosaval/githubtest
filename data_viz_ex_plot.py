import matplotlib.pyplot as plt

#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#plt.plot(input_values, squares, linewidth=5)
#plt.scatter(input_values, squares, s=100)
#plt.scatter(x_values, y_values, edgecolors='none', s=40)
plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
#plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)

#Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

#Set the rtange for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()
