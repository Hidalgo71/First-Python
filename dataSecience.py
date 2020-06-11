import numpy as np

# Numpy is a objects for multidimensional arrays and matrices
# No arithmetrical op.
x = np.array([9, 99, 999])
print(x[1])
x[0] = 90  # Changed value[0]
print(x)
print(x.shape)  # row x column, satır x sütun

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
c = c + 1
print(c)

print("==========================")

# Array multiplication

c = c * c
print(c)

c.dot(c)
print(c)
print("==========================")
# matrix multiplication
d = np.array([1, 2, 3, 4])
e = np.array([4, 2, 2, 4])

print("d == e ?: ", d == e)
print("d array multiplication: ", d * d)
print("d matrix multiplication: ", d.dot(d))
print("d values > e ?\n", d > e)
print("==========================")
# Boll arrays and LOGICAL OR
k = np.array([1, 1, 0, 0], dtype=bool)
l = np.array([1, 0, 1, 0], dtype=bool)
print("k OR l:", np.logical_or(k, l))
print("k AND l:", np.logical_and(k, l))
print("==========================")
# Transcendental(Üstün) functions
y = np.array([[1, 2, 3], [4, 5, 6]])
print("Sin: ", np.sin(y))
print("Log: ", np.log(y))
print("Exp:%.2f ", np.exp(y))  # %.2f Not working

print("==========================")
# Rank 2 array shape (3,4) and slicing to pull out the subarray 1st 2 rows and colm 1 and 2 which shape(2,2)
o = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
p = o[:2, 1:2]
print(p)

print("==========================")
# Access to the data in the middle row of the array
rowR1 = o[1, :]
rowR2 = o[1:2, :]
print(rowR1, rowR1.shape)
print(rowR2, rowR2.shape)
























