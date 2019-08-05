# coding=utf-8
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 输入数据
data = pd.read_csv('./26/demo/data.csv', encoding='gbk')
print(data.head(5))
print(data.columns)
train_x = data[["2019年国际排名", "2018世界杯", "2015亚洲杯"]]#只取部分字段
df = pd.DataFrame(train_x)
kmeans = KMeans(n_clusters=3)#kmeans聚类，3个聚类中心
# 规范化到 [0,1] 空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
# kmeans 算法
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)#聚类结果
# 合并聚类结果，插入到原数据中
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
print(result.head(5))
result.rename({0: u'聚类'}, axis=1, inplace=True)#将0这个字段名修改为“聚类”
print(result)
