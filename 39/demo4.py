# -*- coding: utf-8 -*-
# 信用卡违约率分析
import matplotlib
import pandas as pd
from sklearn.model_selection import learning_curve, train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import seaborn as sns

# 打印配置文件路径 我的是在个人文件夹
print(matplotlib.matplotlib_fname())

# 数据加载
data = data = pd.read_csv('./39/UCI_Credit_Card.csv')

# 数据探索
print(data.shape)  # 查看数据集大小 #(30000, 25)
print(data.describe())  # 数据集概览
'''
                 ID       LIMIT_BAL           SEX     EDUCATION  ...       PAY_AMT4       PAY_AMT5       PAY_AMT6  default.payment.next.month
count  30000.000000    30000.000000  30000.000000  30000.000000  ...   30000.000000   30000.000000   30000.000000                30000.000000
mean   15000.500000   167484.322667      1.603733      1.853133  ...    4826.076867    4799.387633    5215.502567                    0.221200
std     8660.398374   129747.661567      0.489129      0.790349  ...   15666.159744   15278.305679   17777.465775                    0.415062
min        1.000000    10000.000000      1.000000      0.000000  ...       0.000000       0.000000       0.000000                    0.000000
25%     7500.750000    50000.000000      1.000000      1.000000  ...     296.000000     252.500000     117.750000                    0.000000
50%    15000.500000   140000.000000      2.000000      2.000000  ...    1500.000000    1500.000000    1500.000000                    0.000000
75%    22500.250000   240000.000000      2.000000      2.000000  ...    4013.250000    4031.500000    4000.000000                    0.000000
max    30000.000000  1000000.000000      2.000000      6.000000  ...  621000.000000  426529.000000  528666.000000                    1.000000

[8 rows x 25 columns]
'''
# 查看下一个月违约率的情况
next_month = data['default.payment.next.month'].value_counts()
print(next_month)
'''
0    23364
1     6636
'''
df = pd.DataFrame({'default.payment.next.month': next_month.index, 'values': next_month.values})
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.figure(figsize=(6, 6))
plt.title(u'信用卡违约率客户\n (违约：1，守约：0)')
sns.set_color_codes("pastel")
sns.barplot(x='default.payment.next.month', y="values", data=df)#x是横坐标，y是纵坐标做条形图
locs, labels = plt.xticks()
plt.show()

# 特征选择，去掉ID字段、最后一个结果字段即可
data.drop(['ID'], inplace=True, axis=1)  # ID这个字段没有用
target = data['default.payment.next.month'].values
columns = data.columns.tolist()
columns.remove('default.payment.next.month')
features = data[columns].values

# 30%作为测试集，其余作为训练集
train_x, test_x, train_y, test_y = train_test_split(features, target, test_size=0.30, stratify=target, random_state=1)

# 构造各种分类器
classifiers = [
  SVC(random_state=1, kernel='rbf'),#SVM
  DecisionTreeClassifier(random_state=1, criterion='gini'),#决策树
  RandomForestClassifier(random_state=1, criterion='gini'),#随机森林
  KNeighborsClassifier(metric='minkowski'),#KNN
]
# 分类器名称
classifier_names = [
  'svc',
  'decisiontreeclassifier',
  'randomforestclassifier',
  'kneighborsclassifier',
]
# 分类器参数
classifier_param_grid = [
  {'svc__C': [1], 'svc__gamma': [0.01]},
  {'decisiontreeclassifier__max_depth': [6, 9, 11]},#最大深度
  {'randomforestclassifier__n_estimators': [3, 5, 6]},#决策树个数取值
  {'kneighborsclassifier__n_neighbors': [4, 6, 8]},#n的取值
]


# 对具体的分类器进行GridSearchCV参数调优
def GridSearchCV_work(pipeline, train_x, train_y, test_x, test_y, param_grid, score='accuracy'):
  response = {}
  gridsearch = GridSearchCV(estimator=pipeline, param_grid=param_grid, scoring=score)#模型，参数集，评价标准
  # 寻找最优的参数 和最优的准确率分数
  search = gridsearch.fit(train_x, train_y)#训练数据
  print("GridSearch最优参数：", search.best_params_)#得到最佳参数
  print("GridSearch最优分数： %0.4lf" % search.best_score_)#最佳分数（按评价标准最好的）
  predict_y = gridsearch.predict(test_x)#预测
  print("准确率 %0.4lf" % accuracy_score(test_y, predict_y))#准确率
  response['predict_y'] = predict_y#存入预测结果到response中
  response['accuracy_score'] = accuracy_score(test_y, predict_y)#存入准确率到response中
  return response


for model, model_name, model_param_grid in zip(classifiers, classifier_names, classifier_param_grid):
  pipeline = Pipeline([
    ('scaler', StandardScaler()),#先标准化
    (model_name, model)#再调用模型
  ])
  #遍历每一个模型，对数据集执行pipeline机制调参，参数为字典或列表
  result = GridSearchCV_work(pipeline, train_x, train_y, test_x, test_y, model_param_grid, score='accuracy')

'''outout(跑得比较慢，而已有很多FutureWarning)，但SVM的准确率最高
GridSearch最优参数： {'svc__C': 1, 'svc__gamma': 0.01}
GridSearch最优分数： 0.8174
准确率 0.8172

GridSearch最优参数： {'decisiontreeclassifier__max_depth': 6}
GridSearch最优分数： 0.8186
准确率 0.8113

GridSearch最优参数： {'randomforestclassifier__n_estimators': 6}
GridSearch最优分数： 0.7998
准确率 0.7994

GridSearch最优参数： {'kneighborsclassifier__n_neighbors': 8}
GridSearch最优分数： 0.8040
准确率 0.8036
'''