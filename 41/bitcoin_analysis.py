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
df = pd.read_csv('./41/bitcoin_2012-01-01_to_2018-10-31.csv')
# 将时间作为df的索引
df.Timestamp = pd.to_datetime(df.Timestamp)
df.index = df.Timestamp


# 数据探索
print(df.head())
'''
            Timestamp      Open      High       Low     Close  Volume_(BTC)  Volume_(Currency)  Weighted_Price
Timestamp
2011-12-31 2011-12-31  4.465000  4.482500  4.465000  4.482500     23.829470         106.330084        4.471603
2012-01-01 2012-01-01  4.806667  4.806667  4.806667  4.806667      7.200667          35.259720        4.806667
2012-01-02 2012-01-02  5.000000  5.000000  5.000000  5.000000     19.048000          95.240000        5.000000
2012-01-03 2012-01-03  5.252500  5.252500  5.252500  5.252500     11.004660          58.100651        5.252500
2012-01-04 2012-01-04  5.200000  5.223333  5.200000  5.223333     11.914807          63.119578        5.208159
'''
# 按照月，季度，年来统计
df_month = df.resample('M').mean()#按月汇总数据的均值（共82个月）
df_Q = df.resample('Q-DEC').mean()#按季汇总数据的均值
df_year = df.resample('A-DEC').mean()#按年汇总数据的均值
# 按照天，月，季度，年来显示比特币的走势
fig = plt.figure(figsize=[15, 7])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.suptitle('比特币金额（美金）', fontsize=20)
plt.subplot(221)#子图
plt.plot(df.Weighted_Price, '-', label='按天')#输入数据，线的类型，标签
plt.legend()#图例

plt.subplot(222)
plt.plot(df_month.Weighted_Price, '-', label='按月')
plt.legend()

plt.subplot(223)
plt.plot(df_Q.Weighted_Price, '-', label='按季度')
plt.legend()

plt.subplot(224)
plt.plot(df_year.Weighted_Price, '-', label='按年')
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
    model = ARMA(df_month.Weighted_Price, order=(param[0], param[1])).fit()#ARMA模型
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
0     (0, 0)  1574.941439
1     (0, 1)  1485.999944
2     (1, 0)  1388.133930
3     (1, 1)  1385.522304
4     (1, 2)  1387.219778
5     (2, 0)  1386.505577
6     (2, 1)  1387.318991
7     (2, 2)  1395.624768
'''
# 输出最优模型
print('最优模型: ', best_model.summary())#可见最优模型是ARMA(1, 1)
'''
最优模型:                                ARMA Model Results
==============================================================================
Dep. Variable:         Weighted_Price   No. Observations:                   83
Model:                     ARMA(1, 1)   Log Likelihood                -688.761
Method:                       css-mle   S.D. of innovations            957.764
Date:                Mon, 02 Sep 2019   AIC                           1385.522
Time:                        14:53:05   BIC                           1395.198
Sample:                    12-31-2011   HQIC                          1389.409
                         - 10-31-2018
========================================================================================
                           coef    std err          z      P>|z|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                 2103.6096   1567.542      1.342      0.183    -968.717    5175.936
ar.L1.Weighted_Price     0.9251      0.042     22.042      0.000       0.843       1.007
ma.L1.Weighted_Price     0.2681      0.116      2.311      0.023       0.041       0.495
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.0809           +0.0000j            1.0809            0.0000
MA.1           -3.7302           +0.0000j            3.7302            0.5000
-----------------------------------------------------------------------------
'''

# 比特币预测
df_month2 = df_month[['Weighted_Price']]#取出数据Weighted_Price
date_list = [datetime(2018, 11, 30), datetime(2018, 12, 31), datetime(2019, 1, 31), datetime(2019, 2, 28),
             datetime(2019, 3, 31), datetime(2019, 4, 30), datetime(2019, 5, 31), datetime(2019, 6, 30)]#要预测未来8个月的数据
future = pd.DataFrame(index=date_list, columns=df_month2.columns)#索引是date_list，列名同df_month2的列名
df_month2 = pd.concat([df_month2, future])#合并数据（其中有82行同旧数据，8行新的空数据，共90行数据）以上这4句仅画图用，不是预测用的

df_month2['forecast'] = best_model.predict(start=0, end=91)#直接用best_model模型预测数据，共90个月，从第一个月预测到第90个月，数据存入df_month2
#print(df_month2)

# 比特币预测结果显示
plt.figure(figsize=(20, 7))
df_month2.Weighted_Price.plot(label='实际金额')#画上Weighted_Price
df_month2.forecast.plot(color='r', ls='--', label='预测金额')#画上forecast，且为红色线
plt.legend()#画图例
plt.title('比特币金额（月）')#标题
plt.xlabel('时间')#横坐标标签
plt.ylabel('美金')#纵坐标标签
plt.show()
