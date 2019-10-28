import seaborn as sns
import matplotlib.pyplot as plt


"""
 lmplot => allows to display linear model with seaborn.
 
 
"""

tips = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex")
sns.lmplot(x="total_bill", y="tip", data=tips, col="day", row="time", hue="sex")

plt.show()
