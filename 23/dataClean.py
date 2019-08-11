# 加载数据集，你需要把数据放到目录中
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./23/breastCancerData/data.csv")
# 数据清洗
#将特征字段分成3组
feature_mean=list(data.columns[2:12])
feature_se=list(data.columns[12:22])
feature_worst=list(data.columns[22:32])
#ID列没有用，删掉ID列
data.drop("id",axis=1,inplace=True)
#将B良性替换为0,M恶性替换为1
data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})
#将肿瘤诊断结果可视化
#sns.countplot(data['diagnosis'],label='Count')
#plt.show()
#用热力图呈现feature_mean字段之间的相关性
corr=data[feature_mean].corr()
plt.figure(figsize=(14,14))
sns.heatmap(corr,annot=True)#annot=True则会显示每个方格数据
plt.show()
#特征选择：用少量特征代表数据的特性，增强分类器的泛化能力，避免数据过拟合
#feature_mean/se/worst是同一组内容的不同度量方式，只保留一个即可。
#相似性很高的那些字段，取一个有代表性的即可
feature_mean=['radius_mean','texture_mean','smoonthness_mean','compactness_mean','sym']
