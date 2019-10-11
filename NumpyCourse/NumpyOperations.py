import numpy as np


arr = np.arange(0., 11)
"""
Array with Array
"""
print(arr + arr)
print(arr * arr)

"""
Array with Scalars
"""

print(arr + 100)
print(arr * 2)

# print(arr / arr)  # RuntimeWarning: invalid value encountered in true_divide

"""
Universal Array Functions
"""
print(np.sqrt(arr))
