import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0,10,20)
y = x*x
z = x+y
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,1,1])# right top width height| width(right) and height should be equal
axes.plot(x,y)
plt.show()



