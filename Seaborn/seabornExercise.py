import seaborn as sns
import matplotlib.pyplot as plt


sns.set_style("whitegrid")
titanic = sns.load_dataset("titanic")

'''
Uncomment each line to see what each lines make.
'''
# sns.jointplot(x="fare", y="age", data=titanic)
# sns.distplot(titanic["fare"], kde=False, color="red", bins=30)

# sns.boxplot(x="class", y="age", data=titanic, palette="rainbow")

# sns.swarmplot(x="class", y="age", data=titanic)

# sns.countplot(titanic["sex"])

'''
sns.heatmap(titanic.corr(), cmap="coolwarm")
plt.title("titanic.corr")
'''

'''
g = sns.FacetGrid(data=titanic, col="sex")
g.map(plt.hist, "age")
'''

plt.show()
