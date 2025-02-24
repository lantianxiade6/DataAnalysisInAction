# -*- coding: utf-8 -*-
import matplotlib

matplotlib.use('Qt4Agg')
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

# 数据加载，避免中文乱码问题
data_ori = pd.read_csv('./29/heros.csv', encoding='gb18030')

# 数据探索
print(data_ori.columns)#打印所有表头
print(data_ori.head())
features = [u'最大生命', u'生命成长', u'初始生命', u'最大法力', u'法力成长', u'初始法力', u'最高物攻', u'物攻成长', u'初始物攻', u'最大物防', u'物防成长', u'初始物防',
            u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血', u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']#其他的都是中文，不需要放进来
data = data_ori[features]#只提取部分字段

# 特征选择
# 对英雄属性之间的关系进行可视化分析
# 设置 plt 正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 用热力图呈现 features_mean 字段之间的相关性
corr = data[features].corr()
plt.figure(figsize=(14, 14))
# annot=True 显示每个方格的数据
sns.heatmap(corr, annot=True)#热图
plt.show()

# 相关性大的属性保留一个，因此可以对属性进行降维，详见“特征选择分析过程.PNG”，阈值可以是0.8或0.9（'最大攻速', u'攻击范围'是字符串型）
features_remain = [u'最大生命', u'初始生命', u'最大法力', u'最高物攻', u'初始物攻', u'最大物防', u'初始物防', u'最大每5秒回血', u'最大每5秒回蓝',
                   u'最大攻速', u'攻击范围']
data = data_ori[features_remain]

# 数据清洗（非数值型需要转化为数值类型才能做聚类）
data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%')) / 100)
data[u'攻击范围'] = data[u'攻击范围'].map({'远程': 1, '近战': 0})
# 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
ss = StandardScaler()
data = ss.fit_transform(data)

# 模型
# 构造 GMM 聚类
gmm = GaussianMixture(n_components=30, covariance_type='full')#高斯混合模型，30个类
gmm.fit(data)#训练数据
# 测试数据
prediction = gmm.predict(data)
print(prediction)
# 将分组结果输出到 CSV 文件中
data_ori.insert(0, '分组', prediction)#插入一列数据
data_ori.to_csv('./29/hero_out.csv', index=False, sep=',')#导出数据到csv文件

# 评估聚类结果
from sklearn.metrics import calinski_harabaz_score
print(calinski_harabaz_score(data,prediction))
