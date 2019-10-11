import numpy as np
from numpy.random import rand


my_list = [1, 2, 3]

arr = np.array(my_list)
print(arr)

"""
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat_array = np.array(my_mat)
print(mat_array)

print(np.zeros((3, 3)))

print(np.eye(5))

print(np.random.randint(1,100))
"""

print(rand(5,5))
