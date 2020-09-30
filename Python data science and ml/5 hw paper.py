import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import cufflinks as cf
cf.go_offline()
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.iplot(kind='bar')
