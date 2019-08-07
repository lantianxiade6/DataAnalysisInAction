#数据清洗常见做法
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
data={'Chinese':[66,95,93,90,80],'English':[65,85,95,88,90],'Math':[30,98,96,77,90]}
df2=DataFrame(data,index=['Zhangfei','GuanYu','ZhaoYun','HuangZhong','Dianwei'],columns=['English','Math','Chinese'])#指定了列的顺序
print(df2)

#1.删除dataframe中不必要的列或行
# print(df2.drop(columns=['Chinese']))
# print(df2.drop(index=['Zhangfei']))

#2.重命名列名columns
# print(df2.rename(columns={'Chinese':'Yuwen'}))

#3.去重复的值
# print(df2.drop_duplicates())#不太清楚怎么个去重法

#4.更改数据格式
# print(df2['Chinese'].astype('str'))#转字符串类型(object)
# print(df2['Chinese'].astype(np.int64))#转整数类型

#5.删除空格
# data3={'Chinese':['66',' 95 ','93 ',' 90','$80'],'English':[65,85,95,88,90],'Math':[30,98,96,77,90]}
# df3=DataFrame(data3,index=['Zhangfei','GuanYu','ZhaoYun','HuangZhong','Dianwei'],columns=['English','Math','Chinese'])#指定了列的顺序
# print(df3)
# print(df3['Chinese'].map(str.strip))
# print(df3['Chinese'].map(str.lstrip))#删除左边空格
# print(df3['Chinese'].map(str.rstrip))#删除右边空格
# print(df3['Chinese'].str.strip('$'))#删除某个字符

#6.大小写转换
print(df2.columns.str.upper())#全部大写
print(df2.columns.str.lower())#全部小写
print(df2.columns.str.title())#首字母大写