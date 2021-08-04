# https://numpy.org/doc/stable/reference/index.html

import numpy as np
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function
# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method,
# and it will be converted into an ndarray
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# An array that has 1-D arrays as its elements is called a 2-D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# The ndim attribute returns an integer that tells us how many dimensions an array has
print(arr_2d.ndim)

#An array can have any number of dimensions
#When the array is created, you can define the number of dimensions by using the ndmin argument
arr_1 = np.array([1, 2, 3, 4], ndmin=5)
print(arr_1)
print('number of dimensions :', arr_1.ndim)