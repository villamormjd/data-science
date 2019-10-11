import numpy as np
from numpy.random import rand, randn


"""
Create an array of 10 zeros
"""
print(np.zeros(10))

"""
Create an array of 10 ones
"""
print(np.ones(10))

"""
Create an array of 10 fives
"""

print(np.ones(10) * 5)

"""
Create an array of integers from 10 to 50
"""
print(np.arange(10, 51))

"""
Create an array of even integers from 10 to 50
"""
print(np.arange(10, 51, 2))

"""
Create 3x3 matrix with values ranging from 0 to 8
"""
arr_3 = np.arange(9)
print(arr_3.reshape(3, 3))

"""
Create 3x3 identity matrix
"""
print(np.eye(3))

"""
Generate a random number between 0 and 1
"""
print(rand(1))

"""
Generate array of 25 random number
* use randn from numpy
"""
print(randn(25))

"""
Create an array of 20 linear spaced
"""

print(np.linspace(0, 1, 20))

"""
get the sum of all values
"""

mat = np.arange(1, 26).reshape(5, 5)
print(mat.sum())

"""
Get the standard deviation of array
"""
print(np.std(mat))

"""
Get the sum of all columns
"""
print(mat.sum(axis=0))
