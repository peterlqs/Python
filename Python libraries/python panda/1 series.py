import pandas as pd
x=['a','b','c','d','e']
x2=['a','b','c','d','f']
y=[1,2,3,4,5]
z={1:'a',2:'b',3:'c',4:'d',5:'e'}
a=pd.Series(y,x)
b=pd.Series(y,x2)
print(a)
print(a+b)
print(a["c":"d"])

