# encoding=utf-8

######CART分类树
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
clf = DecisionTreeClassifier(criterion='gini')#初始化决策树分类器，以基尼系数为分类指标
# 拟合构造 CART 分类树
clf = clf.fit(train_features, train_labels)#放入训练集，包括特征集和分类标识，进行训练
# 用 CART 分类树做预测
test_predict = clf.predict(test_features)#放入测试集的特征集，进行预测
# 预测结果与测试集结果作比对
score = accuracy_score(test_labels, test_predict)#计算准确率
print("CART 分类树准确率 %.4lf" % score)
# 可视化
from sklearn import tree
import graphviz
dot_data=tree.export_graphviz(clf,out_file=None)#输出DOT格式的决策树
graph=graphviz.Source(dot_data)
#graph.view()
#输出分类树图示，比如里面有个叶节点:X[3]<=0.75，它表示以属性x[3]<=0.75为条件划分，当true时就让左子树，false时进入右子树
#gini就是当前节点的gini系数。samples就是当前节点的样本数
#value=[34,0,0],是指在0/1/2这三类上的样本数，这里刚好全部在类别0上。
graph.render("分类树","./18/")#会在目录下生成一个pdf
'''output
CART 分类树准确率 0.9800
'''

'''关于决策树可视化
需下载graphviz-2.38.msi，下载路径是：
https://graphviz.gitlab.io/_pages/Download/Download_windows.html
然后安装，将bin的路径放入系统变量path中，然后重启VScode，再正常先在终端跑pip install graphviz，再import即可
# 参考：https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html
# 参考：https://graphviz.readthedocs.io/en/stable/
'''

######CART回归树
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeRegressor

# 准备数据集
boston=load_boston()#波士顿房价数据
print(boston.keys())
'''
dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])
'''
#boston有5个key:data特征矩阵,target目标结果，feature_names就是data的特征名，DESCR是数据集描述，filename的boston在本地存放路径
# 探索数据
print(boston.feature_names)
# 获取特征集和分类标识
features = boston.data
prices = boston.target
# 随机抽取 33% 的数据作为测试集，其余为训练集
train_features, test_features, train_price, test_price = train_test_split(features, prices, test_size=0.33, random_state=0)
print(train_features)#全是数值
print(train_price)#房价，是数值
# 创建 CART 回归树
dtr = DecisionTreeRegressor()#初始化
# 拟合构造 CART 回归树
dtr = dtr.fit(train_features, train_price)#放入训练集，包括特征集和房价，进行训练
# 用 CART 回归树做预测
predict_price = dtr.predict(test_features)#放入测试集的特征集，进行预测
# 预测结果与测试集结果作比对
print('回归树二乘偏差均值',mean_squared_error(test_price,predict_price))
print('回归树绝对值偏差均值',mean_absolute_error(test_price,predict_price))
# 可视化
from sklearn import tree
import graphviz#先在终端跑pip install graphviz
dot_data=tree.export_graphviz(dtr,out_file=None)
graph=graphviz.Source(dot_data)
# graph.view()#输出分类树图示
graph.render("回归树","./18/")#会在目录下生成一个pdf
'''output:
回归树二乘偏差均值 25.81395209580838
回归树绝对值偏差均值 3.237724550898203
'''

# ######CART分类树-作业
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.datasets import load_digits
# # 准备数据集
# digits=load_digits()
# # 获取特征集和分类标识
# features = digits.data
# labels = digits.target
# # 随机抽取 33% 的数据作为测试集，其余为训练集
# train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
# print(train_features)#全是数值
# print(train_labels)#0、1、2...8
# # 创建 CART 分类树
# clf = DecisionTreeClassifier(criterion='gini')#初始化决策树分类器，以基尼系数为分类指标
# # 拟合构造 CART 分类树
# clf = clf.fit(train_features, train_labels)#放入训练集，包括特征集和分类标识，进行训练
# # 用 CART 分类树做预测
# test_predict = clf.predict(test_features)#放入测试集的特征集，进行预测
# # 预测结果与测试集结果作比对
# score = accuracy_score(test_labels, test_predict)#计算准确率
# print("CART 分类树准确率 %.4lf" % score)
# # 可视化
# from sklearn import tree
# import graphviz
# dot_data=tree.export_graphviz(clf,out_file=None)#输出DOT格式的决策树
# graph=graphviz.Source(dot_data)
# #graph.view()
# #输出分类树图示，比如里面有个叶节点value=[34,0,0],应该就是判为第0类的意思了
# graph.render("分类树-作业","./18/")#会在目录下生成一个pdf
'''output
CART 分类树准确率 0.8636
'''