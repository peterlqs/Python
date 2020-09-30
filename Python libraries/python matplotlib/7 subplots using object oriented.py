import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0,10,20)
y = x*x
z = x+y
fig , hey= plt.subplots(1,4)#rows , columns
hey[0].plot(x,y)
hey[1].plot(x,x)


plt.tight_layout()
plt.show()