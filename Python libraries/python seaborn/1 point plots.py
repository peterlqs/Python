import matplotlib.pyplot as plt
import seaborn as sns
diamond = sns.load_dataset("diamonds")
top = diamond.head(4)
print(top)
#line_and_column = sns.distplot(diamond["price"])
#bar = sns.rugplot(diamond["x"])#sort of like histogram but bar style
single_line = sns.kdeplot(diamond["price"])
plt.show()