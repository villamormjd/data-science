import pandas as pd
import numpy as np


labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
my_dictionary = {'a': 10, 'b': 20, 'c': 30}

"""
Pandas Series Lesson. 
"""
series = pd.Series(data=my_data, index=labels)

"""
Ways to create a Series
"""
series = pd.Series(my_dictionary)  # Series that holds dictionary

"""
grab information from series
"""
ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])

"""
Adding TWO Series
Return: If index are match will add the Data, if Index no match returns NaN

ser1 + ser2 will return:
    Germany    4.0
    Italy      NaN
    Japan      8.0
    USA        2.0
    USSR       NaN

as Italy, and USSR has no match in another series
"""

print(ser1 + ser2)
