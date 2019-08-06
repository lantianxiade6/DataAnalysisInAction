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

##作业
##在三科中的每个人的平均成绩，最小成绩，最大成绩，方差，标准差。总成绩排名。
#建立数组，表头为'姓名','语文','英语','数学'
persontype=np.dtype({
        'names':['姓名','语文','英语','数学'],
        'formats':['U32','f','f','f']
        })
person=np.array([
    ('张飞',66,65,30),
    ('关羽',95,85,98),
    ('赵云',93,92,96),
    ('黄忠',90,88,77),
    ('典韦',80,90,90)
]
,dtype=persontype)
#print(person)

#计算每个科目的每个人的平均成绩，最小成绩，最大成绩，方差，标准差
for subject in ['语文','英语','数学']:#遍历每个科目
    dat=person[:][subject]#取出对应科目的数据，用于后面计算
    print('科目:{}: 平均成绩:{:.2f}; 最小成绩:{:.2f}; 最大成绩:{:.2f}; 方差:{:.2f}; 标准差:{:.2f}'.format(subject,np.mean(dat),np.min(dat),np.max(dat),np.var(dat),np.std(dat)))

sum3=[]#计算每个人的三科总分
for p in person:
    sum3.append((p['姓名'],np.sum(list(p[['语文','英语','数学']]))))

ranking=np.array(sum3,dtype=[('姓名','U32'),('总成绩','f')])
#print(ranking)
result=np.sort(ranking,order='总成绩')#按总成绩排序
#print(result)
print('排名    姓名    总分')
i=1
for ele in result[::-1]:#倒数
    print('排名',i,ele)
    i+=1
