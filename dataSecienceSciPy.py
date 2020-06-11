import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt

# 2D array
x = np.array([[0, 1],
              [1, 0],
              [2, 0]])
print(x)

print("==========================")
# Compute Euclidean Distance between all rows of x as new array d
d = squareform(pdist(x, 'euclidean'))
print(d)

print("==========================")
# Compute x and y coordinates
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
# plt.show()
ySin = np.sin(x)
yCos = np.cos(x)
plt.plot(x, ySin)
plt.plot(x, yCos)
plt.xlabel("X axis")
plt.ylabel('Y axis')
plt.title("Sin & Cos")
plt.legend(["Sine", 'Cos'])
# plt.show()
