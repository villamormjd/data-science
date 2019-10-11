import pandas as pd
import numpy as np

from numpy.random import randn


"""
np.random.seed(101)

* seed() returns the same random numbers
"""
np.random.seed(101)

"""
DataFrames: a group of Series that share an index
"""
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

"""
indexing in DataFrame to grab a specific data.

df['column_name']
"""
df['new'] = df['W'] * df['Z']

""" 
Removing a column from DataFrame
df.drop(column_name, axis = 1, inplace = True)
* axis = 0  for rows
inplace = True to remove the column permanently

df.loc('row_names'), loc() label based location
df.iloc(row_number)  iloc() integer based location
"""

df.drop('new', axis=1, inplace=True)

z_col = df[df['Y'] > 0]['Z']
x_col = df[df['W'] > 0]['Y']
df['new'] = z_col + x_col

"""
df.reset_index() to resset the index into default index ( integer based index)
df.set_index('column_name') 
"""

newind = 'CA NY WY OR CO'.split()
df['States'] = newind  # adding new Column name 'States'
df.set_index('States', inplace=True)

