# encoding:utf-8

import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.normal(size=(10, 4))
labels = ['A', 'B', 'C', 'D']

#matplotlib画图
plt.boxplot(data, labels=labels)
plt.show()

#seaborn画图
import seaborn as sns
df=pd.DataFrame(data,columns=labels)
sns.boxplot(data=df)
plt.show()