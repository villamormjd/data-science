import matplotlib.pyplot as plt
import numpy as np


"""
plt.show() to show the visual graphs
"""
x = np.linspace(0, 5, 11)
y = x ** 2

"""
Functional Method
"""
# plt.plot(x, y)
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')

"""
OOP Method
plt.figure()
"""

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
axes.set_ylabel('My Y Label')
axes.set_xlabel('My X Label')
axes.set_title('Axes Title')

"""
Canvas within canvas 
"""
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.4, 0.2, 0.4, 0.3])
axes2.plot(x, y)
axes1.plot(y, x)
plt.show()
