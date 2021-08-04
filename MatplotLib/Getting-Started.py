import matplotlib.pyplot as plt
import numpy as np
import math

xpoints = np.array([0, 3, 6])
ypoints = np.array([0, 7, 10])
plt.plot(xpoints, ypoints)

xpoints = np.array([0, 3, 5, 6])
ypoints = np.array([10, 9, 7, 5])
plt.plot(xpoints, ypoints, marker = 'o')
#https://www.w3schools.com/python/matplotlib_markers.asp

plt.legend(["Positive Slope", "Negative Slope"])
plt.title("Graph", loc="left", fontdict={"family": "serif", "size": 9})

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)

plt.show()
