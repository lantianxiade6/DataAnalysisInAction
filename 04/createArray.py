# encoding:utf-8
import numpy as np

#创建数组
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 10#修改数据
print(a.shape)#数据维度
print(b.shape)
print(a.dtype)#数据属性
print(b)

'''
output::
(3,)
(3, 3)
int64
[[ 1  2  3]
 [ 4 10  6]
 [ 7  8  9]]

'''