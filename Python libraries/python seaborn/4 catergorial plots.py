import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
tips_head = tips.head(6)
print(tips_head)
#count_plot = sns.countplot(data=tips,x="smoker")
#point_plot = sns.pointplot(data=tips,x="total_bill",y ="day")
#cat_plot = sns.catplot(data=tips,x="total_bill",y="day",kind="box")# like point plot but with upgrades with kind=
#swarm_plot = sns.swarmplot(data=tips,x="total_bill",y="day",hue="time",palette="Blues")
#strip_plot = sns.stripplot(data=tips,x="total_bill",y="day")
box_plot = sns.boxplot(data=tips,x="total_bill",y="day",hue="sex")
#Also violin_plot...

plt.show()