import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.random.randn(100)
s = pd.Series(a)

##使用Matplotlib画图
plt.hist(s,bins=10)#bins是组数
plt.show()

#使用Seaborn画折线图
import seaborn as sns
sns.distplot(s,bins=10,kde=True)#kde=True是添加核密度估计
plt.show()