import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 5, 11)
y = x ** 2

"""
Figure Size and DPI

figsize = () tuple of width and height
"""

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))
axes[0].plot(x, y)

axes[1].plot(y, x)

"""
save figure to file
fig.savefig('.png/ .jpg/ .pdf')
"""

# fig.savefig('my_fig.png')

"""
Legend: 
ax.plot(x,x**2, label = " label_name")

ax.legend()

ax.legend(loc=0) puts legend to best location
"""

plt.tight_layout()
plt.show()
