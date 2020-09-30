import pandas as pd
p = {'item':['apple','apple','orange','orange','guns','guns'],'days':["mon","tue","wed","thur","fri","sat"],"sales":[100,80,200,100,5,10]}
df = pd.DataFrame(p)
print(df,"\n")
x = df.groupby('item')
print(x.mean(),"\n")#also sum,max...
print(x.describe().transpose(),"\n")#.transpose() means change from horizontal to vertical







