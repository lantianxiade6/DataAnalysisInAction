# encoding:utf-8

import matplotlib

matplotlib.use('Qt4Agg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
## 准备数据
x = range(2010,2020,1)#x轴数据需递增
y = [5,3,6,20,17,16,19,30,32,35]

#使用Matplotlib画折线图
plt.plot(x,y)
plt.show()

#使用Seaborn画折线图
import seaborn as sns
df=pd.DataFrame({'x':x,'y':y})
sns.lineplot(x='x',y='y',data=df)#图是有x,y label的
plt.show()