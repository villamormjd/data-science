import pandas as pd
import numpy as np

from numpy.random import randn

np.random.seed(102)
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))

hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])

""" set index name of columns """
df.index.names = ['Groups', 'Num']

print(df)

dataB = df.loc['G2'].loc[2]['B']
print(df.xs(1, level='Num'))

