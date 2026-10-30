import numpy as np

# NUMPY ARRAYS ARITHMETIC OPERATIONS
array = np.array([1, 2, 3, 4, 5])

print(array < 3)                             # [ True  True False False False]
print(array[array < 3])                      # [1 2]
array[array < 3] = 0
print(array)                                 # [0 0 3 4 5]


# BROADCASTING - Either rows and columns should match or either of them should be 1. 
array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)                          # (1, 4)
print(array2.shape)                          # (4, 1)
print(array1 * array2)                       # (4, 4)