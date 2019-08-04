# coding=utf-8
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.model_selection import cross_val_score

# 数据加载
train_data = pd.read_csv('./19/Titanic_Data/train.csv')#若报错，先检查路径，再将csv编码改为‘UTF-8’
test_data = pd.read_csv('./19/Titanic_Data/test.csv')
# 数据探索
print(train_data.info())
print(test_data.info())
# 使用平均年龄来填充年龄中的 nan 值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)#inplace=True就是会将na替换
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

print(train_data['Embarked'].value_counts())

'''output
S    644
C    168
Q     77
Name: Embarked, dtype: int64

'''

# 使用登录最多的港口来填充登录港口的 nan 值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']#Cabin有大量缺失，就不要了
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]
#test_labels = test_data['Survived']#test_data里面没有它

dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))#会将字符型题目变换一下
print(dvec.feature_names_)

'''output
['Age', 'Embarked=C', 'Embarked=Q', 'Embarked=S', 'Fare', 'Parch', 'Pclass', 'Sex=female', 'Sex=male', 'SibSp']
'''

# 构造 ID3 决策树
clf = DecisionTreeClassifier(criterion='entropy')#决策树分类器，分类标准是信息熵
# 决策树训练
clf.fit(train_features, train_labels)#放入训练集的特征和分类标识进行训练
test_features = dvec.transform(test_features.to_dict(orient='record'))#会将字符型题目变换一下
# 决策树预测
pred_labels = clf.predict(test_features)

# 得到决策树准确率
#本来要用test_features, test_labels的(准确率也没这么高)，但test_data里面没有它
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score 准确率为 %.4lf' % acc_decision_tree)
'''output
score 准确率为 0.9820
'''

# 使用 K 折交叉验证 统计决策树准确率
print(u'cross_val_score 准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))

'''output
cross_val_score 准确率为 0.7847
'''
