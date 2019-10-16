import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10)
y = x * 2
z = x ** 2

"""
• Create a figure object callef 'fig' using plt.figure()
• Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.
• Plot(x,y) on that axes and set the labels and titles to match the plot.
"""

fig = plt.figure()
ax = fig.add_axes([0.1, 0.2, 0.8, 0.75])
ax2 = fig.add_axes([0.2, 0.6, 0.3, 0.3])

# large Plot
ax.plot(x, z)
ax.set_xlabel('x Label')
ax.set_ylabel('y label')
ax.set_title('Title')

# Insert plot
ax2.plot(x, y)
ax2.set_title('zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xlim([2.0, 2.2])
ax2.set_ylim([3.0, 5.0])

"""
Craeting sublots (nrows=1,ncols=2)
"""
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))

axes[0].plot(x, y, color='blue', ls="--")
axes[1].plot(x, z, color='red', lw=3)

plt.show()
