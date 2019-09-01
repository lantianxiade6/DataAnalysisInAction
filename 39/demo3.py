# -*- coding: utf-8 -*-
# 使用 RandomForest 对 IRIS 数据集进行分类
# 利用 GridSearchCV 寻找最优参数, 使用 Pipeline 进行流水作业
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

rf = RandomForestClassifier()
parameters = {"randomforestclassifier__n_estimators": range(1,11)}#1-10
iris = load_iris()
pipeline = Pipeline([
        ('scaler', StandardScaler()),#先标准化
        ('randomforestclassifier', rf)#再做随机森林
])
# 使用 GridSearchCV 进行参数调优
clf = GridSearchCV(estimator=pipeline, param_grid=parameters)
# 对 iris 数据集进行分类
clf.fit(iris.data, iris.target)
print(" 最优分数： %.4lf" %clf.best_score_)
print(" 最优参数：", clf.best_params_)
# 运行结果：（每次跑的结果都不一样）
# 最优分数： 0.9667
# 最优参数： {'randomforestclassifier__n_estimators': 9}
