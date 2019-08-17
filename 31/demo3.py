# -*- coding: utf-8 -*-
from efficient_apriori import apriori
import csv
director = u'宁浩'
file_name = './31/'+director+'.csv'
lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))
# 数据加载
data = []
for names in lists:#遍历每一行
     name_new = []
     for name in names:#遍历每一个名字，注csv就是以逗号间隔的
           # 去掉演员数据中的空格
           name_new.append(name.strip())
     data.append(name_new[1:])#不要第一个
# 挖掘频繁项集和关联规则
itemsets, rules = apriori(data, min_support=0.5,  min_confidence=1)#找到支持度大于50%，置信系数为1的频繁项集和关联规则
print(itemsets)
'''itemsets
{1: {('徐峥',): 5, ('黄渤',): 6}, 2: {('徐峥', '黄渤'): 5}}
'''
print('\r')
print(rules)

'''rules
[{徐峥} -> {黄渤}]
'''
#宁浩导演喜欢用徐峥和黄渤，并且有徐峥的情况下，一般都会用黄渤