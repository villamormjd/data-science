import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")
print(tips.head())

"""
barplot() returns the average of categorical column
optional @argument: estimator => default (mean)
"""
# sns.barplot(x="day", y="total_bill", data=tips, estimator=np.std)

sns.boxenplot(x="day", y="total_bill", data=tips)
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)

plt.show()
