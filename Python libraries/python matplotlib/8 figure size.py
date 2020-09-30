import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0,10,20)
y = x*x
z = x+y
"""
fig = plt.figure(figsize=(3,3))#width,height
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)
"""
fig,axes = plt.subplots(2,1,figsize=(1,5))
axes[0].plot(x,y)
axes[1].plot(y,x)


plt.show()