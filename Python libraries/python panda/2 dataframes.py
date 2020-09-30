import pandas as pd
a=['😎',4]
b=[5,6,7,8]
c=[9,0,1,2]
d=[3,4,5,6]
e=[7,8,9,0]
df = pd.DataFrame([a,b,c,d,e],['a','b','c','d','e'],['W','X',"Y","Z"])
print(df)
