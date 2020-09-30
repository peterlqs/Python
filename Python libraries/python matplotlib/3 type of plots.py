import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(0,10,20)
print(x)
y = x*x
print(y)
z = x+x

#plt.scatter(x,y)# Scatter : instead of straight line,its a scattered line
#plt.bar(x,y)
#plt.hist(x,y)# hist : histogram
#plt.fill(x,y)
#plt.pie(x,y)

plt.subplot(3,2,1) #column length,row lenght(smaller=longer), Number of graphs,only change the third one
plt.plot(x,y)

plt.subplot(3,2,2)
plt.hist(x,y)

plt.subplot(3,2,4)
plt.plot(x,y)

plt.subplot(3,2,5)
plt.bar(x,y)

plt.subplot(3,2,6)
plt.fill(x,y)

plt.tight_layout()
plt.show()

plt.polar(x,y)
plt.show()