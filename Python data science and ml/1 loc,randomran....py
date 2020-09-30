import pandas as pd
import numpy as np
np.random.seed(101)
num1 = pd.DataFrame([1,2,3,],["usa","german","italy"])
num2 = pd.Series([1,2,3,],["usa","german","italy"])

df = pd.DataFrame(np.random.rand(3,3),["usa","ger","ita"],["x","y",'z'])
df["w"]= df["x"]+df["y"]
df.drop("x",axis=1,inplace=True)# axis = 0 means usa line,=1 means x,y,z,w|inplace=True means rly replace cuz it scares u accidentally lose info
only = df.loc["ger"]
#loc : only columns' name, iloc : by order (ex : 1,2,3,...)
print(only)
print(df)