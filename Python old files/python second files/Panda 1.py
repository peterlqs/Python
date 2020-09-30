import pandas as pd
from matplotlib import pyplot as plt
y="""x = [1,2,3]
y = [1,4,9]
z = [10,5,0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("HI WORLD")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y","this is z"])
plt.show()"""

data = pd.read_csv("countries.csv")
us = data[data.country =="United States"]
china = data[data.country =="China"]
plt.plot(us.year,us.population / us.population.iloc[0]*100)
plt.plot(china.year,china.population / china.population.iloc[0]*100)
plt.xlabel("Year")
plt.ylabel("Population Growth ( First year = 100 )")
plt.legend(["United States","China"])
plt.show()