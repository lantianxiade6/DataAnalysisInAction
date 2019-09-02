# -*- coding: utf-8 -*-
# 比特币走势预测，使用时间序列ARMA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA
import warnings
from itertools import product
from datetime import datetime

warnings.filterwarnings('ignore')
# 数据加载
df = pd.read_csv('./41/shanghai_1990-12-19_to_2019-2-28.csv')
# 将时间作为df的索引
df.Timestamp = pd.to_datetime(df.Timestamp)
df.index = df.Timestamp


# 数据探索
print(df.head())
'''
            Timestamp   Price
Timestamp
1990-12-19 1990-12-19   96.05
1990-12-20 1990-12-20  104.30
1990-12-21 1990-12-21  109.07
1990-12-24 1990-12-24  113.57
1990-12-25 1990-12-25  120.09
'''
# 按照月，季度，年来统计
df_month = df.resample('M').mean()#按月汇总数据的均值（共339个月）
df_Q = df.resample('Q-DEC').mean()#按季汇总数据的均值
df_year = df.resample('A-DEC').mean()#按年汇总数据的均值
# 按照天，月，季度，年来显示比特币的走势
fig = plt.figure(figsize=[15, 7])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.suptitle('沪市指数', fontsize=20)
plt.subplot(221)#子图
plt.plot(df.Price, '-', label='按天')#输入数据，线的类型，标签
plt.legend()#图例

plt.subplot(222)
plt.plot(df_month.Price, '-', label='按月')
plt.legend()

plt.subplot(223)
plt.plot(df_Q.Price, '-', label='按季度')
plt.legend()

plt.subplot(224)
plt.plot(df_year.Price, '-', label='按年')
plt.legend()
plt.show()#根据可视化结果觉得用按月的数据，即df_month（降维，降低模型训练时间）


# 设置参数范围
ps = range(0, 3)
qs = range(0, 3)
parameters = product(ps, qs)#笛卡尔积（得到所有组合）
parameters_list = list(parameters)
print(parameters_list)
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 寻找最优ARMA模型参数，即best_aic最小
results = []
best_aic = float("inf")  # 正无穷
for param in parameters_list:#遍历每一个p,q组合
  try:
    model = ARMA(df_month.Price, order=(param[0], param[1])).fit()#ARMA模型
  except ValueError:
    print('参数错误:', param)
    continue
  aic = model.aic#得到模型AIC
  if aic < best_aic:#只要得到的AIC比上一个AIC小就替换成为新的结果
    best_model = model
    best_aic = aic
    best_param = param
  results.append([param, model.aic])#存放所有结果

#所有结果
result_table = pd.DataFrame(results)
result_table.columns = ['parameters', 'aic']
print('所有结果：')
print(result_table)
'''
所有结果：
  parameters          aic
0     (0, 0)  5691.864041
1     (0, 1)  5286.493355
2     (1, 0)  4474.736875
3     (1, 1)  4441.799571
4     (1, 2)  4433.184458
5     (2, 0)  4434.885915
6     (2, 1)  4436.779538
7     (2, 2)  4428.219099
'''
# 输出最优模型
print('最优模型: ', best_model.summary())#可见最优模型是ARMA(2, 2)
'''
最优模型:                                ARMA Model Results
==============================================================================
Dep. Variable:                  Price   No. Observations:                  339
Model:                     ARMA(2, 2)   Log Likelihood               -2208.110
Method:                       css-mle   S.D. of innovations            162.159
Date:                Mon, 02 Sep 2019   AIC                           4428.219
Time:                        15:37:07   BIC                           4451.175
Sample:                    12-31-1990   HQIC                          4437.367
                         - 02-28-2019
===============================================================================
                  coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------
const        1841.5061    489.610      3.761      0.000     881.888    2801.124
ar.L1.Price     0.5137      0.130      3.959      0.000       0.259       0.768
ar.L2.Price     0.4501      0.128      3.508      0.001       0.199       0.702
ma.L1.Price     0.8480      0.121      6.985      0.000       0.610       1.086
ma.L2.Price     0.3796      0.062      6.095      0.000       0.258       0.502
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
'''

# 比特币预测
df_month2 = df_month[['Price']]#取出数据Price
date_list = [datetime(2019, 3, 31), datetime(2019, 4, 30), datetime(2019, 5, 31), datetime(2019, 6, 30), 
             datetime(2019, 7, 31), datetime(2019, 8, 31), datetime(2019, 9, 30), datetime(2019, 10, 31), 
             datetime(2019, 11, 30), datetime(2019, 12, 31)]#要预测未来10个月的数据
future = pd.DataFrame(index=date_list, columns=df_month2.columns)#索引是date_list，列名同df_month2的列名
df_month2 = pd.concat([df_month2, future])#合并数据（其中有339行同旧数据，10行新的空数据，共349行数据）以上这4句仅画图用，不是预测用的

df_month2['forecast'] = best_model.predict(start=0, end=350)#直接用best_model模型预测数据，共349个月，从第一个月预测到第349个月，数据存入df_month2
#print(df_month2)

# 比特币预测结果显示
plt.figure(figsize=(20, 7))
df_month2.Price.plot(label='实际')#画上Price
df_month2.forecast.plot(color='r', ls='--', label='预测')#画上forecast，且为红色线
plt.legend()#画图例
plt.title('沪市指数')#标题
plt.xlabel('时间')#横坐标标签
plt.ylabel('沪市指数')#纵坐标标签
plt.show()
