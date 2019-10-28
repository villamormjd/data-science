import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")

sns.set_context("notebook")
sns.countplot(x="sex", data=tips)
sns.despine()

"""
scale and context

sns.set_style()
set_context(context="string")
"""
plt.show()
