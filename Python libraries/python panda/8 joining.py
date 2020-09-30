import pandas as pd
x1 = {'a':[1,2,3],'b':[5,6,7]}
y1 = {'c':[3,4,5],'d':[2,3,6]}
x = pd.DataFrame(x1,index=["p1","p2","p3"])
y = pd.DataFrame(y1,index=["p1","p4","p5"])
print(x,"\n")
print(y,"\n")
print(x.join(y,how="outer"))#if there isnt how=outer there wont be p4 p5| Also inner: both has(p1)
                            #right : all right side must has variables(a,b), left : the opposite(c,d)






