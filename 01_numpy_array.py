import numpy as np

# print(np.__version__)

my_list = [1, 2, 3, 4, 5]
my_list = my_list * 2
print(my_list)                            # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


# NUMPY ARRAYS
my_list = np.array([1, 2, 3, 4, 5])
my_list = my_list * 2
print(my_list)                            # [2 4 6 8 10]
print(type(my_list))                      #<class 'numpy.ndarray'>