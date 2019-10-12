import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0.1, 0.2, 0.8, 0.7])

"""
Changing the appearance of plot
@:param: @color => String, color of the line
         linewidth(lw) => float, the thicknes of the line 
         alpha => float , transparency of the line 
         linestyle (ls) => string, style of line ('--'), ('..'), etc.
         marker => string, mark each point of x,y axes ('o')
         markersize => int, for size of marker
         
         ax.set_xlim([x,y]), set_ylim([x,y) => list as parameter
"""
ax.plot(x, y, color='#eac117')
plt.show()
