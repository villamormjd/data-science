import numpy as np


'''
arr = np.arange(0, 11)

print(arr[8:11]) #prints element between range
print(arr[:5]) #prints all elements before
print(arr[5:]) #print all element beyond
'''

#arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

"""
*****************************
arr_2d[0, 0] is same as arr_2d[0][0] 
both will return 5

****************************

@params: arr_2d[:2,1:]
return: [[10,15],
        [25,30]]

returns first two rows and columns form staring index

"""

array_2d = np.arange(50).reshape(5,10)
print(array_2d[1:3, 3:5])
