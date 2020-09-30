import numpy as np
import pandas as pd
df1 = pd.DataFrame({"key1":[2,3,4],"a":[5,6,7],"b":[1,2,4]})
df2 = pd.DataFrame({"key1":[1,2,9],"a":[5,8,9],"b":[1,2,3]})
merge = pd.merge(df1,df2, how = "inner",on="b")
outer = pd.merge(df1,df2, how = "outer",on="key1")#also left n right (in how)
print(merge,"\n")
print(outer)