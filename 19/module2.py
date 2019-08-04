# coding=utf-8
import pandas as pd

# 数据加载
train_data = pd.read_csv('./19/Titanic_Data/train.csv')
test_data = pd.read_csv('./19/Titanic_Data/test.csv')
# 数据探索
print(train_data.info())#发现Age/Cabin/Embarked有缺失
print(test_data.info())#发现Age/Fare/Cabin有缺失
# 使用平均年龄来填充年龄中的 nan 值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)#inplace就是替换na处
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)

print(train_data['Embarked'].value_counts())#查看每个Embarked的值的个数
print(test_data['Embarked'].value_counts())#查看每个Embarked的值的个数
'''output
S    644
C    168
Q     77
Name: Embarked, dtype: int64

'''

# 使用登录最多的港口来填充登录港口的 nan 值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S',inplace=True)

print(train_data.info())
print(test_data.info())