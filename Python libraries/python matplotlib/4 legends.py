import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x = np.linspace(0,10,20)
y = x*x
z = x+y
plt.plot(x,y,y,z,label=" Sample")

plt.legend(loc=1)
"""
loc:
1-top right
2-top left
3-down left
4-down right
5-middle right
6-middle left
7-middle right
8-middle down
9-middle up
10-middle
"""
plt.show()