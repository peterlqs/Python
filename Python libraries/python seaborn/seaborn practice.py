import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sale.csv")
print(data.head(6))

#sns.lmplot(data=data,x="Total Cost",y="Total Profit",hue="Item Type",palette="Blues")
sns.barplot(data=data,x="Country",y="Total Profit")
plt.show()





