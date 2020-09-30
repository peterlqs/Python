import numpy as np
x = np.arange(1,21)
print(x)
print(x[2:5])
print(x[5:])
x[5:15]=40
print(x)
y=x.copy()
print(y)
