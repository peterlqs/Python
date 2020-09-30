import pandas as pd
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,0,1,2]
d=[3,4,5,6]
e=[7,8,9,0]
df = pd.DataFrame([a,b,c,d,e],['a','b','c','d','e'],['W','X',"Y","Z"])
print(df)
cf = df[df['W']>5][["W","X"]]#row(s) that has value greater than 5 only|And only W X column
print(cf)
ko = df[(df["W"]>3)&(df["Z"]>2)]
print(ko)