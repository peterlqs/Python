import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("dots")
tip = sns.load_dataset("tips")
print(tip.head(6))
#pair_plot = sns.pairplot(data,hue = "choice")#hue = "choice" will put legends according to datas in "choice"
pair_tips = sns.pairplot(tip,hue = "sex")
pair_tips.map_diag(sns.distplot)#add a distplot diagonally
#pair_tips.map_upper(sns.kdeplot)#add a kdeplot
pair_tips.map_lower(sns.kdeplot)#if you want the kdeplot at lower edge

plt.show()