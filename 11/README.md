## 数据质量的准则
 1. 完整性
  - 单条数据是否存在空值，统计字段是否完善
 2. 全面性
  - 通过常识判断该列是否有问题（数据定义、单位标识、数值本身）
 3. 合法性
  - 类型、内容、大小的合法性
 4. 唯一性
  - 记录是否重复，行列数据不应重复

## 完整性
- [缺失值](./missingValue.py)  
删除：删除数据缺失的记录  
均值：使用当前列的均值填补  
```
df['Age'].fillna(df['Age'].mean(),inplace=True)
```  
高频：使用当前列出现频率最高的值填补  
```
age_maxf=train_features['Age'].value_counts.index[0]
train_features['Age'].fillna(age_maxf,inplace=True) 
```
- [空行](./blankLine.py)   
```
df.dropna(how='all',inplace=True)
```
## 全面性
  - 单位不统一 转换单位
```
#获取weight数据列中单位为lbs的数据
rows_with_lbs=df['weight'].str.contains('lbs').fillna(False)#weight带lbs的行
print(df[row_with_lbs])
#将lbs转换为kgs,2.2lbs=1kgs
for i,lbs_row in df[row_with_lbs].iterrows():#遍历lbs的行，i应该是行index，lbs_row就是整行数据
  #截取从头开始到倒数第三个字符之前，即去掉lbs
  weight=int(float(lbs_row['weight'][:3])/2.2)
  df.at[i,'weight']='{}kgs'.format(weight)

```
## 合理性
  - 删除非ASCII字符
```
df['first_name'].replace({r'[^\x00-\x7F]+':''},regex=True,inplace=True)
df['last_name'].replace({r'[^\x00-\x7F]+':''},regex=True,inplace=True)
```
## 唯一性
  - 将一列的多个参数拆分
  ```
  df[['first_name','last_name']]=df['name'].str.split(expand=True)#name拆开两列
  df.drop('name',axis=1,inplace=True)#删掉name
  ```
  - 删除重复数据行
  ```
  df.drop_duplicates(['first_name','last_name'],inplace=True)
  ```
[作业](./practice.py) 
