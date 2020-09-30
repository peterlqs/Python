import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0,10,20)
y = x*x
z = x+y
"""
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.35,0.3,0.3,0.4])
axes2.set_title("Second")
axes2.set_xlabel("x-axis")
axes2.set_ylabel("y-axis")
axes.set_xlabel("x-axis")
axes.set_ylabel("y-axis")
axes.set_title("First")
axes.plot(x,z)
"""
fig,axes=plt.subplots(1,2)
axes[0].plot(x,y)
axes[1].plot(x,z)
axes[0].set_xlabel("x label")
axes[0].set_ylabel("y label")
axes[0].set_title("Title 1")
axes[1].set_xlabel("x label")
axes[1].set_ylabel("y label")
axes[1].set_title("Title 2")
plt.tight_layout()

plt.show()