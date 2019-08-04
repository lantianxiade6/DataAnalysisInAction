# encoding=utf-8
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
# 准备数据集
iris=load_iris()
# 获取特征集和分类标识
features = iris.data
labels = iris.target
# 随机抽取 33% 的数据作为测试集，其余为训练集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
print(train_features)#全是数值
print(train_labels)#0、1、2
# 创建 CART 分类树
clf = DecisionTreeClassifier(criterion='gini')#决策树分类器，以基尼系数为分类指标
# 拟合构造 CART 分类树
clf = clf.fit(train_features, train_labels)#放入训练集，包括特征集和分类标识，进行训练
# 用 CART 分类树做预测
test_predict = clf.predict(test_features)#放入测试集的特征集，进行预测
# 预测结果与测试集结果作比对
score = accuracy_score(test_labels, test_predict)#计算准确率
print("CART 分类树准确率 %.4lf" % score)

'''output
CART 分类树准确率 0.9800
'''