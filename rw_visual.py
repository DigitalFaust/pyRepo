import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Building random walking and drawing it points and diagram

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Setting view field
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
#    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    
    # Highliting first and last point
    plt.scatter(0, 0, c='orange', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolor='none', s=100)

    # Removing axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
