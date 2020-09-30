import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0,10,20)
y = x*x
z = x+y

fig = plt.figure()
x1 = fig.add_axes([0.1,0.1,0.8,0.8])
x1.plot(x,y)
x2 = fig.add_axes([0.5,0.3,0.3,0.3])
x2.plot(y,x) #Becareful placing cuz it might overlap
plt.show()