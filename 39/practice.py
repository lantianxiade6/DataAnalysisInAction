# 信用卡违约率分析
import matplotlib
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.pipeline import Pipeline
from matplotlib import pyplot as plt
import seaborn as sns

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

# AdaBoost 分类器
ada=AdaBoostClassifier(random_state=1)#随机种子为1
# 参数，主要key名：如果直接用AdaBoostClassifiert调参就n_estimators即可，如果用pipeline要加上pipeline的key名
parameters={'adaboostclassifier__n_estimators':[10,50,100]}#参数，注意key要和模型参数一致

# pipeline
pipeline=Pipeline([
    ('scaler',StandardScaler()),#先标准化
    ('adaboostclassifier',ada)#在adaboost
])
# 使用 GridSearchCV 进行参数调优
gridsearch = GridSearchCV(estimator=pipeline, param_grid=parameters)
# 对 iris 数据集进行分类
gridsearch.fit(train_x, train_y)#训练
print(" 最优分数： %.4lf" %gridsearch.best_score_)#得到最优参数
print(" 最优参数：", gridsearch.best_params_)#得到最优的评价标准结果
predict_y = gridsearch.predict(test_x)#预测
print("准确率 %0.4lf" % accuracy_score(test_y, predict_y))#准确率

'''output
 最优分数： 0.8187
 最优参数： {'adaboostclassifier__n_estimators': 10}
 准确率 0.8129
'''