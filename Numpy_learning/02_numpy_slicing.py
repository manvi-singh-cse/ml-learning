import numpy as np

# ARRAY DIMENSIONS
array0 = np.array(1)
print(array0.ndim)                                          #0

array1 = np.array([1])
print(array1.ndim)                                          #1

array2 = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
print(array2.ndim)                                          #2

array3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(array3.ndim)                                          #3


# INDEXING
print(array3.shape)                                         #(2, 3, 3)
print(array3[0][2][0])                                      #7 - Chained Indexing
print(array3[0, 2, 0])                                      #7 - Multidimensional Indexing (faster)

print(array3[0, 2, 0] + array3[1, 2, 0])                    #14


# ROW SELECTION
print("Row Selection")
print(array2[-1])                                           #[7 8 9] - first row from last
print(array2[0:2])                                          #0th to 1st row
print(array2[0:4:2])                                        #0th to 3rd row with step=2


# COLUMN SELECTION
print("Column Selection")
print(array2[:, 0])                                         #[1 4 7] - first column
print(array2[:, -1])                                        #[3 6 9] - first column from last
print(array2[:, 0:2])                                       #0th to 1st column
print(array2[:, 0:4:2])                                     #0th to 3rd column with step=2

# PARTITION SELECTION
print(array2[0:2, 0:2])                                     #0th to 1st row and 0th to 1st column