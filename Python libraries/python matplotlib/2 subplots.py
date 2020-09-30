import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x*x
z = x+x

plt.subplot(3,2,1) #column length,row lenght(smaller=longer), Number of graphs,only change the third one
plt.plot(x,z)

plt.subplot(3,2,2)
plt.plot(x,y)

plt.subplot(3,2,4)
plt.plot(x,x)

plt.subplot(3,2,5)
plt.plot(y,x)
plt.xlabel("im a label")
plt.ylabel("another label")

plt.tight_layout()# to separate plots from each other


plt.show()