# -*- coding:utf-8 -*-
# 使用SVC对信用卡欺诈进行分类
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_recall_curve
from sklearn.preprocessing import StandardScaler
import warnings
from sklearn import svm

warnings.filterwarnings('ignore')


# 混淆矩阵可视化
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix"', cmap=plt.cm.Blues):
  plt.figure()
  plt.imshow(cm, interpolation='nearest', cmap=cmap)#画矩阵
  plt.title(title)#标题
  plt.colorbar()#颜色渐变标尺？
  tick_marks = np.arange(len(classes))#0-1
  plt.xticks(tick_marks, classes, rotation=0)#坐标轴刻度标签
  plt.yticks(tick_marks, classes)

  thresh = cm.max() / 2.#计算cm矩阵的最大值的一半，即为thresh
  for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):#遍历矩阵中每一个元素
    plt.text(j, i, cm[i, j],#标上矩阵的数值
             horizontalalignment='center',#居中
             color='white' if cm[i, j] > thresh else 'black')#字体颜色

  plt.tight_layout()
  plt.ylabel('True label')#坐标轴标签
  plt.xlabel('Predicted label')
  plt.show()


# 显示模型评估结果
def show_metrics(cm):
  tp = cm[1, 1]
  fn = cm[1, 0]
  fp = cm[0, 1]
  tn = cm[0, 0]
  P=tp / (tp + fp)
  R=tp / (tp + fn)
  F1=2*P*R/(P+R)
  print('精确率: {:.3f}'.format(P))
  print('召回率: {:.3f}'.format(R))
  print('F1值: {:.3f}'.format(F1))

# 数据加载
#data = pd.read_csv('./40/creditcard.csv')#由于GitHub限制文件不得大于100M,所以这里直接读取本地csv，GitHub上只保留rar压缩版
data = pd.read_csv(r'D:\Lisa\学习2\python\creditcard.csv')

# 数据探索
print(data.describe())
# 设置plt正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制类别分布
plt.figure()
ax = sns.countplot(x='Class', data=data)#出class的条形图
plt.title('类别分布')
plt.show()

# 显示交易笔数，欺诈交易笔数
num = len(data)
num_fraud = len(data[data['Class'] == 1])
print('总交易笔数: ', num)
print('诈骗交易笔数：', num_fraud)
print('诈骗交易比例：{:.6f}'.format(num_fraud / num))

# 欺诈和正常交易可视化
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(15, 8))#2行1列的组合图，共用横坐标
bins = 50
ax1.hist(data.Time[data.Class == 1], bins=bins, color='deeppink')#数据为欺诈数据，50格，颜色为粉色
ax1.set_title('诈骗交易')
ax2.hist(data.Time[data.Class == 0], bins=bins, color='deepskyblue')#数据为正常数据，50格，颜色为蓝色
ax2.set_title('正常交易')
plt.xlabel('时间')
plt.ylabel('交易次数')
plt.show()

# 对Amount进行数据规范化（加入了一列Amount_Norm）
data['Amount_Norm'] = StandardScaler().fit_transform(data['Amount'].values.reshape(-1, 1))

#特征选择
y = np.array(data.Class.tolist())#将data的class这个字段转为list
data = data.drop(['Time', 'Amount', 'Class'], axis=1)#删掉这三个字段
X = np.array(data.as_matrix())#转为矩阵
print(y[:6])
print(X[:6])

# 准备训练集和测试集
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.1, random_state=33)

# SVC分类(跑得很慢,5min)
model = svm.LinearSVC()#SVM
model.fit(train_x, train_y)#训练
predict_y = model.predict(test_x)#预测（0或1）
# 计算混淆矩阵，并显示
cm = confusion_matrix(test_y, predict_y)#得到一个矩阵
class_names = [0, 1]
# 显示混淆矩阵
plot_confusion_matrix(cm, classes=class_names, title='SVC 混淆矩阵')#调用函数plot_confusion_matrix，画混淆矩阵图
# 显示模型评估分数
show_metrics(cm)#调用show_metrics函数，显示模型评估分数
'''
精确率: 0.837
召回率: 0.683
F1值: 0.752
'''