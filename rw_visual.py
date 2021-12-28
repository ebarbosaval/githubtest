import matplotlib.pyplot as plt

from randomwalk import RandomWalk


while True:
    # Make a random walk, plot the points
    rw = RandomWalk()
    rw.fill_walk()

    # Visualization
    plt.scatter(rw.x_values, rw.y_values, s=10)
    plt.show()

    # Keep making new walks, as long as the program is active
    keep_running = input("Make another walk (y/n): ")
    if keep_running == 'n':
        break