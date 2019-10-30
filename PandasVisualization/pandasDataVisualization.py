import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df1 = pd.read_csv("../FolderFile/df1", index_col=0)
df2 = pd.read_csv("../FolderFile/df2")

print(df1.head())
print(df2.head())

'''
other way to plot a column using pandas
df1["A"].plot(kind='hist',bins=30)
df1["A"].hist(bins=30)
df1["A"].plot.hist()

'''
df1["A"].plot.line(x=df1.index, y="B", lw=1)
df2.plot.bar(stacked=True)
df1.plot.scatter(x="A", y="B", cmap="coolwarm")

plt.show()
