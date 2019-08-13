# coding=utf-8
import matplotlib

matplotlib.use('Qt4Agg')
# 手写数字分类
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# 加载数据
digits = load_digits()##内置数据集：手写数字数据集
data = digits.data
# 数据探索
print(data.shape)#(1797, 64)
# 查看第一幅图像的数据，相当于x
print(digits.images[0])
'''[[ 0.  0.  5. 13.  9.  1.  0.  0.]
 [ 0.  0. 13. 15. 10. 15.  5.  0.]
 [ 0.  3. 15.  2.  0. 11.  8.  0.]
 [ 0.  4. 12.  0.  0.  8.  8.  0.]
 [ 0.  5.  8.  0.  0.  9.  8.  0.]
 [ 0.  4. 11.  0.  1. 12.  7.  0.]
 [ 0.  2. 14.  5. 10. 12.  0.  0.]
 [ 0.  0.  6. 13. 10.  0.  0.  0.]]'''
# 第一幅图像代表的数字含义，相当于y
print(digits.target[0])#0
# 将第一幅图像显示出来(可视化)
plt.gray()
plt.imshow(digits.images[0])
plt.show()

# 分割数据，将25%的数据作为测试集，其余作为训练集
train_x, test_x, train_y, test_y = train_test_split(data, digits.target, test_size=0.25, random_state=33)

# 数据规范化一：采用Z-Score规范化（因为后面knn要算距离）
ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)#应该会有根据train_x变换的
print('------------train_ss_x')
print(train_ss_x)
print('------------test_ss_x')
print(test_ss_x)
print('------------train_y')
print(train_y)

'''
------------train_ss_x
[[ 0.         -0.32672314 -0.87554711 ... -1.11540424 -0.49709493
  -0.19054741]
 [ 0.         -0.32672314 -0.2423893  ... -1.11540424 -0.49709493
  -0.19054741]
 [ 0.         -0.32672314 -1.08659972 ... -1.11540424 -0.49709493
  -0.19054741]
 ...
 [ 0.         -0.32672314 -0.2423893  ... -1.11540424 -0.49709493
  -0.19054741]
 [ 0.         -0.32672314  1.44603155 ... -1.11540424 -0.49709493
  -0.19054741]
 [ 0.          0.75459398  0.39076852 ... -1.11540424 -0.49709493
  -0.19054741]]
------------test_ss_x
[[ 0.         -0.32672314 -0.2423893  ...  0.73926354 -0.49709493
  -0.19054741]
 [ 0.         -0.32672314 -0.4534419  ...  1.58229435  1.97553015
  -0.19054741]
 [ 0.         -0.32672314  0.39076852 ... -1.11540424 -0.49709493
  -0.19054741]
 ...
 [ 0.         -0.32672314  0.17971592 ...  0.90786971 -0.24983242
  -0.19054741]
 [ 0.         -0.32672314 -1.08659972 ...  0.73926354 -0.24983242
  -0.19054741]
 [ 0.         -0.32672314 -1.08659972 ...  1.58229435  2.22279266
  -0.19054741]]
  ------------train_y
[4 7 4 ... 1 5 5]'''
# 创建KNN分类器
knn = KNeighborsClassifier()
knn.fit(train_ss_x, train_y) 
predict_y = knn.predict(test_ss_x) 
print("KNN准确率: %.4lf" % accuracy_score(test_y,predict_y))#KNN准确率: 0.9756

# 创建SVM分类器
svm = SVC()
svm.fit(train_ss_x, train_y)
predict_y=svm.predict(test_ss_x)
print('SVM准确率: %0.4lf' % accuracy_score(test_y,predict_y))#SVM准确率: 0.9867

# 数据规范化二：采用Min-Max规范化[0,1]
mm = preprocessing.MinMaxScaler()
train_mm_x = mm.fit_transform(train_x)
test_mm_x = mm.transform(test_x)

# 创建Naive Bayes分类器(多项式朴素贝叶斯传入的数据不能有负数)
mnb = MultinomialNB()
mnb.fit(train_mm_x, train_y) 
predict_y = mnb.predict(test_mm_x) 
print("多项式朴素贝叶斯准确率: %.4lf" % accuracy_score(test_y,predict_y))#多项式朴素贝叶斯准确率: 0.8844

# 创建CART决策树分类器
dtc = DecisionTreeClassifier()
dtc.fit(train_mm_x, train_y) 
predict_y = dtc.predict(test_mm_x) 
print("CART决策树准确率: %.4lf" % accuracy_score(test_y,predict_y))#CART决策树准确率: 0.8644
