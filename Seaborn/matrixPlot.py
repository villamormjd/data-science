import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")

tc = tips.corr()
fp = flights.pivot_table(index="month", columns="year", values="passengers")

sns.heatmap(fp, cmap="coolwarm", linecolor="white", linewidths=1)
sns.clustermap(fp, cmap="coolwarm")
plt.show()
