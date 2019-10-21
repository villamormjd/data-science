import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

"""
distplot() returns a histogram and KDE graph.
to removew KDE, add arguments kde = False.
to modify how many bins to show, bins = int
"""
sns.distplot(tips['tip'], kde=False, bins=100)

"""
joinplot() allows to matchup distplot variate data. You can combine two distplot()
@:parameter: (x='col_name',y='col_name',dataset=)
optional @parameter: kind => change or modify what kind of plot to be used. 
    default: scatter plot
    other options: kde, hex, reg
"""
sns.jointplot(x='total_bill', y='tip', data=tips)

"""
pairplot() plot paralyze relationship across dataframe atleast for numerical cols.
@:argument: hue => color dataset base on catagorized columns
            palette => for color of dataset
"""

sns.pairplot(tips, hue='smoker')
plt.show()
