# coding=utf-8
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

# 数据加载
data = pd.read_csv('./19/Titanic_Data/train.csv')#训练集，包括特征信息和存活与否标签 #若报错，先检查路径，再将csv编码改为‘UTF-8’

# 数据清洗
# 使用平均年龄来填充年龄中的 nan 值
data['Age'].fillna(data['Age'].mean(), inplace=True)#inplace=True就是会将na替换
# 使用票价的均值填充票价中的 nan 值
data['Fare'].fillna(data['Fare'].mean(), inplace=True)
print(data['Embarked'].value_counts())
'''
S    644
C    168
Q     77
'''
# 使用登录最多的港口来填充登录港口的 nan 值
data['Embarked'].fillna('S', inplace=True)

# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']#Cabin有大量缺失，就不要了
# 拆分训练集和测试集
train_features, test_features, train_labels, test_labels = train_test_split(data[features], data['Survived'], test_size=0.3, random_state=33)

dvec = DictVectorizer(sparse=False)#可以将分类变量变成0-1变量
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))#注意：训练集要用fit_transform,训练+转换
test_features = dvec.transform(test_features.to_dict(orient='record'))#测试集的特征矩阵 #注意：测试集要用transform即可,即只转换
print(dvec.feature_names_)#查看转化后的特征属性

'''output
['Age', 'Embarked=C', 'Embarked=Q', 'Embarked=S', 'Fare', 'Parch', 'Pclass', 'Sex=female', 'Sex=male', 'SibSp']
'''

# 构造 ID3 决策树
clf = DecisionTreeClassifier(criterion='entropy')#决策树分类器，分类标准是信息熵
# 决策树训练
clf.fit(train_features, train_labels)#放入训练集的特征和分类标识进行训练
# 决策树预测
pred_labels = clf.predict(test_features)

# 得到决策树准确率
acc_decision_tree = round(clf.score(test_features, test_labels), 6)
print(u'score 准确率为 %.4lf' % acc_decision_tree)
'''output
score 准确率为 0.9820
'''
# AdaBoost 分类器
dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
ada = AdaBoostClassifier(base_estimator=dt_stump, n_estimators=300)#对弱分类器进行迭代
ada.fit(train_features, train_labels)
pred_labels = ada.predict(test_features)
print(pred_labels)
acc_adaboost = round(ada.score(test_features, test_labels), 6)
print(u'score 准确率为 %.4lf' % acc_adaboost)