import pandas as pd
import numpy as np


d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)

print(df)

"""
dropna() method: drops rows with one or more missing values.
default axis = 0 ( for rows)
acis = 1 (for columns)

dropna(thresh=2) : drops rows with 2 NaN values
"""

print(df.dropna(thresh=1))

"""
fillna() fill NaN values
"""

print(df.fillna(value=df.mean()))  # replace NaN values with the mean values of each column
