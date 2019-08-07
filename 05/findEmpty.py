# encoding:utf-8

import pandas as pd
from pandas import Series, DataFrame

data = {
  'name':['zhangfei','guanyu','zhaoyun','huangzhong','dianwei'],
  'Chinese': [66, 95, 95, 90, 80],
  'English': [65, 85, 92, 88, 90],
  'Math': [None, 98, 96, 77, 90]
}

data_frame2 = DataFrame(data, index=['zhang', 'guan', 'zhao', 'huang', 'dian'])

print(data_frame2)

print(data_frame2.isnull())#查看哪里有空值
print('\n')
'''output
        name  Chinese  English   Math
zhang  False    False    False   True
guan   False    False    False  False
zhao   False    False    False  False
huang  False    False    False  False
dian   False    False    False  False
'''

print(data_frame2.isnull().any())#查看哪一列有空值

'''output
name       False
Chinese    False
English    False
Math        True
dtype: bool
'''

##use apply function

data_frame2['name'] = data_frame2['name'].apply(str.upper)#整列调用函数，如转大写

print(data_frame2)

'''output
             name  Chinese  English  Math
zhang    ZHANGFEI       66       65   NaN
guan       GUANYU       95       85  98.0
zhao      ZHAOYUN       95       92  96.0
huang  HUANGZHONG       90       88  77.0
dian      DIANWEI       80       90  90.0
'''

## 使用函数

def double_df(x):
  return 2*x

data_frame2['Chinese'] = data_frame2['Chinese'].apply(double_df)
print('\n')
print(data_frame2)

'''
             name  Chinese  English  Math
zhang    ZHANGFEI      132       65   NaN
guan       GUANYU      190       85  98.0
zhao      ZHAOYUN      190       92  96.0
huang  HUANGZHONG      180       88  77.0
dian      DIANWEI      160       90  90.0
'''

## 使用更加复杂的函数

def plus(df,n,m):
  df['new1'] = (df['Chinese']+df['English'])*m
  df['new2'] = (df['Chinese']+df['English'])*n
  return df

print('\n')
df1 = data_frame2.apply(plus,axis=1,args=(2,3,))#axis=1表示列操作，args=(2,3,)表示n=2,m=3
print(df1)

'''output
             name  Chinese  English  Math  new1  new2
zhang    ZHANGFEI      132       65   NaN   591   394
guan       GUANYU      190       85  98.0   825   550
zhao      ZHAOYUN      190       92  96.0   846   564
huang  HUANGZHONG      180       88  77.0   804   536
dian      DIANWEI      160       90  90.0   750   500
'''

#统计
df1=DataFrame({'name':['Zhangfei','GuanYu','a','b','c'],'data1':range(5)})
print(df1.describe())