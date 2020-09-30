import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
head = data.head(6)
print(head)
sns.set_style("darkgrid")
#set_style options : white, dark, whitegrid, darkgrid, ticks
#set_style must be place before countplot
sns.countplot(x="smoker",data = data)
# styling chart(not a kind of chart) (down)
# paper: normal, poster: less number ????
sns.set_context("notebook")
#sns.despine(bottom=True,left=True,right=False,top=False)#remove line in graph



plt.show()