# encoding=utf-8

# import pandas as pd
# from pandas import DataFrame
# from pandasql import sqldf, load_meat, load_births

# df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})

# pysqldf = lambda sql: sqldf(sql, globals())
# sql = "select * from df1 where name='ZhangFei'"#直接用SQL语句对dataframe进行操作
# print(pysqldf(sql))

'''output
   data1      name
0      0  ZhangFei
'''
#作业：用DataFrame创建数据，并进行清洗，最后新增一列三科成绩总和
import pandas as pd
import numpy as np
from pandas import DataFrame
data={
   '姓名':['张飞','关羽','赵云','黄忠','典韦','典韦'],
   '语文':[66,95,95,90,80,80],
   '英语':[65,85,92,88,90,90],
   '数学':[None,98,96,77,90,90]
}

df=DataFrame(data)
print(df)

#删除重复的行
df=df.drop_duplicates()
print(df)

#填补缺失值
#print(df.isnull().any())
#print(df.columns[df.isnull().any()])#找到有空值的列
for col in df.columns[df.isnull().any()]:#遍历每个有空值的列
   df[col]=df[col].fillna(df[col].mean())#用列均值填补每列的缺失值
print(df)

#新增一列三科成绩总和
def plus(df):
       df['总成绩'] = df['语文']+df['英语']+df['数学']
       return df

df=df.apply(plus,axis=1)#调用plus函数，计算总成绩
print(df)