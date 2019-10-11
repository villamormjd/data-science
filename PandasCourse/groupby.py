import pandas as pd
import numpy as np


data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'SArah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)

"""
GroupBy DataFrame by 'Compnay' and perfrom aggregate function (mean(), sum(), etc)
"""
byComp = df.groupby('Company')
print(df)
print(byComp.sum().loc['FB'])
