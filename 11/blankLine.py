# encoding:utf-8

import pandas as pd
from pandas import Series, DataFrame

data = {
  'Chinese': [66, 95, 93, 90, None, None],
  'English': [65, 85, 92, 88, 90, None],
  'Math': [30, 98, 96, 77, 90, None],
  'name':['xiaoguan','xiaozhang','xiaozhao','xiaoma','xiaohuang', None]
}

data_frame2 = DataFrame(data, index=['guan', 'zhang', 'zhao', 'ma', 'huang','dummy'])
print(data_frame2)

data_frame2.dropna(how='all',inplace=True)#删除空行

print(data_frame2)

'''output
       Chinese  English  Math       name
guan      66.0       65    30   xiaoguan
zhang     95.0       85    98  xiaozhang
zhao      93.0       92    96   xiaozhao
ma        90.0       88    77     xiaoma
huang      NaN       90    90  xiaohuang
'''