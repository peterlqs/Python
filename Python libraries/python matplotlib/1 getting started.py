import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.linspace(0,10,10)
y = x*x
z = x+y
print(x)
print(y)
print(z,"\n")
plt.plot(x,y,x,x,x,z)# 2 first labels is 1 line
plt.xlabel("Hi im X")
plt.ylabel("Hi im Y")
plt.title("Example")
plt.show()
