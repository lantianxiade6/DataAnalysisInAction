# encoding=utf-8
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data1': range(5)})

##　 基于指定列进行连接（交集）
df3 = pd.merge(df1, df2, on='name')
print(df3)
print('\n')

## inner 连接(基于相同的键name做交集)
df4 = pd.merge(df1, df2, how='inner')
print(df4)
print('\n')

## 左连接
df5 = pd.merge(df1, df2, how='left')
print(df5)
print('\n')

## 右连接
df6 = pd.merge(df1, df2, how='right')
print(df6)
print('\n')

## 外连接（基于相同的键name做并集）
df7 = pd.merge(df1, df2, how='outer')
print(df7)
print('\n')

##


'''output
       name  data1_x  data1_y
0  ZhangFei        0        0
1    GuanYu        1        1


       name  data1
0  ZhangFei      0
1    GuanYu      1


       name  data1
0  ZhangFei      0
1    GuanYu      1
2         a      2
3         b      3
4         c      4


       name  data1
0  ZhangFei      0
1    GuanYu      1
2         A      2
3         B      3
4         C      4


       name  data1
0  ZhangFei      0
1    GuanYu      1
2         a      2
3         b      3
4         c      4
5         A      2
6         B      3
7         C      4
'''
