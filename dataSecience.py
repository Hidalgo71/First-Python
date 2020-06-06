import numpy as np

# Numpy is a objects for multidimensional arrays and matrices
# No arithmetrical op.
x = np.array([9, 99, 999])
print(x[1])
x[0] = 90                           # Changed value[0]
print(x)
print(x.shape)                      # row x column, satır x sütun

print("==========================")

# 2 dimensional array
y = np.array([[1, 2, 3], [4, 5, 6]])
print("Array y: \n", y)
print(y.shape)
print(y[1, 0], y[1, 1], y[1, 2])

print("==========================")

# arrays zeros and ones
arrZ = np.zeros((2, 2))
print(arrZ)
arrO = np.ones((2, 1))
print(arrO)

print("==========================")

# Creating rank 2 constant array of all 9
a = np.full((2, 2), 9)
print(a)

print("==========================")
# identity matrix

b = np.eye(3)
print(b)

print("==========================")
# Rank 2 random values array

c = np.random.random((3, 3))
print(c)

