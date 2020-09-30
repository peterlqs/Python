import pandas as pd
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,0,1,2]
d=[3,4,5,6]
e=[7,8,9,0]
df = pd.DataFrame([a,b,c,d,e],['a','b','c','d','e'],['W','X',"Y","Z"])
print(df)
df['P']=df["Y"]+df["X"]#attach new datafrane
print(df) 
print(df.drop('e'))#delete row
print(df.drop('Z',axis=1))#delete column