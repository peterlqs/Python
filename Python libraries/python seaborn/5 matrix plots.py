import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#Matrix plots(heat,cluster,...) can only be use for corr,pivot_table(as for now) only not raw load_dataset
data = sns.load_dataset("flights")
head = data.head(6)
print(head)
data2 = data.corr()
print(data2)
#heat_map = sns.heatmap(data=data2,annot=True,linewidths=5,linecolor="black",cmap="Blues")#higher linewidths the smaller it becomes
flights2 = data.pivot_table(index="month",columns="year",values="passengers")
print(flights2)
#flights2_heat = sns.heatmap(data=flights2,lw = 1,cmap="cool")
cluster_map = sns.clustermap(data=flights2,cmap="cool")


plt.show()
