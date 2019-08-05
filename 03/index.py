# encoding:utf-8

# #输入和输出
# name=input("what's your name: ")
# sum=100+10
# print("hello, %s" %name)#s表字符串
# print('sum=%d' %sum)#d表数值

# #判断语句：if else
# score=56
# if score>=90:
#   print('Excellent')
# else:
#   if score<60:
#     print('Fail')
#   else:
#     print('Good Job')

# #循环语句：for in
# sum=0
# for number in range(1,10,2):
#   print(number)
#   sum=sum+number
# print('sum is ',sum)

# #循环语句while
# sum=0
# number=1
# while number<11:
#   sum=sum+number
#   number+=1
# print(sum)

#数据类型：列表、元组、字典、集和
# #列表[]
# lists=['a','b','c']
# lists.append('d')#在尾部添加元素
# print(lists)
# print(len(lists))#元素个数
# lists.insert(0,'mm')#在指定位置插入元素
# print(lists)
# lists.pop()#在尾部删除元素
# print(lists)

# #元组()
# tuples=('tupleA','tupleB')
# print(tuples[0])

# #字典{dictionary}，key:value对
# score={'guanyu':95,'zhangfei':96}
# score['zhaoyun']=98#添加元素
# print(score)
# score.pop('zhangfei')#删除元素
# print('guanyu' in score)#某个key是否存在
# print('liu',60)#某个key对应的值，如无则默认为60

# #集和set，是key的集和
# s=set(['a','b','c'])
# s.add('d')#添加元素
# print(s)
# s.remove('b')#删除元素
# print(s)
# print('c' in s)#某个key是否存在

#注释一行
'''注释
多行'''
"""注释
多行"""

#import module1               #导入一个模块
#import module1,module2       #导入多个模块
#from package import module1  #导入某包中的模块
#from package import *        #导入某包中所有模块
#module的实质是一个.py文件，package是一个文件夹，里面带有__init__.py文件

# def addone(score):
#   return score+1
# print(addone(99))

#浙江大学在线答题系统
#http://acm.zju.edu.cn/onlinejudge/submit.do?problemId=1

#作业1
#在终端或cmd跑pip install scikit-learn，再
import sklearn

#作业2
sum=0
for i in range(1,100,2):
  print(i)
  sum=sum+i
print(sum)
