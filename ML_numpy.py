import numpy as np

arr = np.array([[1,2,3],[4,2,5],])
print("array is of type:",type(arr))
print("no. of dinesion:",arr.ndim)
print("space of array:",arr.shape)
print("size of array:",arr.size)
print("array stores elemest of type:",arr.dtype)

#matrix manipulation in numpy
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print("The elementwise addition of matrix")
print(np.add(x,y))
print(np.subtract(x,y))
print(np.divide(x,y))
print(np.multiply(x,y))
print(x.T)
