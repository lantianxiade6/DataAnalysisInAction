# encoding:utf-8
import numpy as np

#指定结构数组的类型
persontype = np.dtype({
  'names': ['name', 'age', 'chinese', 'math', 'english'],
  'formats': ['S32', 'i', 'i', 'i', 'f']#U32是Unicode格式，S32是ascii格式
})

peoples = np.array(
  [
    ('zhangfei', 32, 75, 100, 90),
    ('guanyu', 24, 85, 96, 88.5),
    ('zhaoyun', 28, 85, 92, 96.5),
    ('huangzhong', 29, 65, 85, 100)
  ],
  dtype=persontype
)

print(peoples)

ages = peoples[:]['age']#年龄
chineses = peoples[:]['chinese']
math = peoples[:]['math']
english = peoples[:]['english']
print(ages)
print(np.mean(ages))#平均年龄
print(np.mean(chineses))
print(np.mean(math))
print(np.mean(english))

'''output:
28.25
77.5
93.25
93.75
'''
