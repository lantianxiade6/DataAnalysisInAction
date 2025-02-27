import pandas as pd
from pandas import Series,DataFrame

x1 = Series([1,2,3,4])#用列表创建Series
x2 = Series(data=[1,2,3,4],index=['a','b','c','d'])#指定索引
d={'a':1,'b':2,'c':3,'d':4}
x3=Series(d)#用字典创建Series
print(x1)
print(x2)
print(x3)

''' output
0    1
1    2
2    3
3    4
dtype: int64
a    1
b    2
c    3
d    4
dtype: int64
'''