import pandas
from pandas import DataFrame
import numpy as np
data={
    'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','pastrami','honey ham','nova lox'],
    'ounces':[4.0,3.0,None,6.0,7.5,8.0,-3.0,5.0,6.0],
    'animal':['pig','pig','pig','cow','cow','pig','cow','pig','salmon']
}
df=DataFrame(data)
print(df)
print('\n')
df['food']=df['food'].str.lower()#food全部变成小写
df=df.dropna()#直接删掉至少有1个na的行（这里其实是为了删掉第2行，因为bacon有很多行，删掉就行了）
df=df[df['ounces']>=0]#删掉ounces为负的行，因为pastrami有很多行，删掉就行了
df['ounces'][df['food']=='bacon']=df['ounces'][df['food']=='bacon'].mean()#bacon有两行，将bacon的ounces替换为两者均值
df=df.drop_duplicates()#删除重复的行
df.index=range(len(df))#重新调整index
print(df)
