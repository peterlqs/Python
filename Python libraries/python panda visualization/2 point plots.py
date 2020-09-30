import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data1 = pd.read_csv("ece.csv")
data2 = pd.read_csv("tips.csv")
x1 = np.random.rand(100,5)# rows, columns
x2 = np.random.rand(10,5)
data3 = pd.DataFrame(x1,columns=['a','b','c','d','e'])
print(data2.head())
#data2.plot.scatter(x="total_bill",y="tip")
#data2["total_bill"].plot.line() for individual information
#data2.plot.line()
#data2.plot.kde() for density like histogram
#data2.hist() histogram for each individual value
##data2.plot.hist()
# also data2.plot(kind="hist") is similar to the upper code line
#also bar,area,box(with area u can place alpha in () function as transparency)
data2.plot.hexbin(x="total_bill",y="tip",gridsize=15,cmap="cool")# the smaller gridsize the larger it will be(?!)
plt.show()