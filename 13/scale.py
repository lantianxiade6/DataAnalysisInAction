#coding:utf-8
from sklearn import preprocessing
import numpy as np
#初始化数据，每一行是一个样本，每一列是一个特征
x=np.array([
    [0.,-3.,1.],
    [3.,1.,2.],
    [0.,1.,-1.]
])

#将数据进行[0,1]规范化（min-max规范化）
min_max_scaler=preprocessing.MinMaxScaler()
minmax_x=min_max_scaler.fit_transform(x)
print(minmax_x)

#z-score规范化
scaled_x=preprocessing.scale(x)
print(scaled_x)

#小数定标规范化
j=np.ceil(np.log10(np.max(abs(x))))#算最大绝对值是几位数的
jscaled=x/(10**j)#10的j次方
print(jscaled)
