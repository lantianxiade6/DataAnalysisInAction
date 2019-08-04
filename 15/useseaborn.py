# encoding:utf-8
import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = 1000
x = np.random.randn(N)#生成N个随机数
y = np.random.rand(N)

## use matplotlib
# plt.scatter(x, y, marker='x')
# plt.show()

## use seaborn
import seaborn as sns
sns.set(style="darkgrid")

df = pd.DataFrame({'x': x, 'y': y})

sns.jointplot(x='x', y='y', data=df, kind='scatter')#比正常散点图多了频数直方图
plt.show()
