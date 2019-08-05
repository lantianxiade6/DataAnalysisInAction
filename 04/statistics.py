# encoding:utf-8

import numpy as np

# #统计函数
# a = np.array([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ])

# print(np.amin(a))#求数组中所有元素的最小值
# print(np.amin(a, 0))#求数组0轴中的每组的最小值([1,4,7],[2,5,8],[3,6,9])
# print(np.amin(a, 1))#求数组1轴中的每组的最小值
# #总之axis=0就是跨行，axis=1就是跨列

# print(np.amax(a))#求最大值
# print(np.amax(a, 0))
# print(np.amax(a, 1))
# ''' output
# 最小值
# 1
# [1 2 3]
# [1 4 7]
# 最大值
# 9
# [7 8 9]
# [3 6 9]

# '''

# print(np.ptp(a))#极差
# print(np.ptp(a, 0))
# print(np.ptp(a, 1))

# '''
# 最大值和最小值的差
# 8
# [6 6 6]
# [2 2 2]

# '''
# #百分位数
# print(np.percentile(a,50))#50%分位数
# print(np.percentile(a,50,axis=0))
# print(np.percentile(a,50,axis=1))

# # 中位数
# print(u"中位数:")
# print(np.median(a))
# print(np.median(a, axis=0))
# print(np.median(a, axis=1))

# '''
# 中位数:
# 5.0
# [4. 5. 6.]
# [2. 5. 8.]

# '''

# # 求平均数
# print(u"平均数:")
# print(np.mean(a))
# print(np.mean(a, axis=0))
# print(np.mean(a, axis=1))

# # 加权平均数
# print(u"加权平均数:")
# b = np.array([1, 2, 3, 4])

# wts = np.array([1, 2, 3, 4])
# print(np.average(b))#(1+2+3+4)/4=2.5
# print(np.average(b, weights=wts))#(1*1+2*2+3*3+4*4)/(1+2+3+4)=3

# # 标准差
# print(u"标准差:")
# c = np.array([1, 2, 3, 4])

# print(np.std(c))

# # 方差
# print(u"方差:")

# c = np.array([1, 2, 3, 4])
# print(np.var(c))

# print(u'排序')

# d = np.array(
#   [
#     [4, 3, 2],
#     [2, 4, 1]
#   ]
# )
# print(np.sort(d))#默认按最后一个轴排序
# print(np.sort(d, axis=None))#扁平化成1维的向量排序
# print(np.sort(d, axis=0))#按轴0排序
# print(np.sort(d, axis=1))#按轴1排序

#作业
persontype=np.dtype({
    'names':['name','Chinese','English','Math'],
    'formats':['S32','i','i','i']
})

person=np.array(
    [
        ('张飞',66,65,30),
        ('关羽',95,85,98),
        ('赵云',93,92,96),
        ('黄忠',90,88,77),
        ('典韦',80,90,90)
    ],
    dtype=persontype
)

print(person)

#未解决