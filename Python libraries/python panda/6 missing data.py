import numpy as np
import pandas as pd
a={"a":[1,2,3,4,5],"b":[6,7,8,9,np.nan],"c":[0,1,2,np.nan,np.nan],"d":[3,4,np.nan,np.nan,np.nan],"e":[5,np.nan,np.nan,np.nan,np.nan]}
hah = pd.DataFrame(a)
print(hah,"\n")
gh = hah.dropna()#remove rows with NaN
print(gh,"\n")
jk = hah.dropna(thresh=2)#delete rows but backward
print(jk,"\n")
io = hah["b"].fillna(value=hah['b'].mean())#mean means average of all the value in that column
print(io,"\n")
