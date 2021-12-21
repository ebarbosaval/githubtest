# Graphed cubes for 5, up to 5000 values, and added a colormap to the plot

import matplotlib.pyplot as plt

# Initialize axis vales
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Set up graph stylization
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

# Set chart title and axes labels
plt.title('Cube Numbers', fontsize=40)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

# Set range of axes
#Set the range for each axis.
plt.axis([0, 5000, 0, 50000000000])

plt.show()
