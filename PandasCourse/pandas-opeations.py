import pandas as pd
import numpy as np


df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [444, 555, 666, 444],
    'col3': ['abc', 'def', 'ghi', 'xyz']
})

"""
finding unique values in DataFrames
df['col_name'].unique() =>
df['col_name'].nunique() => return how many unique values
df['col_name'].value_counts() => return numbers of every values


"""

df['col2'].unique()

"""
df.apply() => params of function.
"""


def times2(x):
    return x * 2

df['col1'].apply(lambda x: x * x)

"""
Removing columns
df.drop(col_name, inplace = True)
"""

"""
sorting DataFrames based on values
"""
sortByCol2 = df.sort_values('col2')


"""
privot_table(value, index, columns)
"""

print((df.pivot_table(values='col2', index='col1', columns='col3')))