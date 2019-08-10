## 泰坦尼克号逃生预测

`sklearn` 自带的决策树模型(只能做ID3和CART决策树)

## 分类器

```python
clf = DecisionTreeClassifier(criterion='entropy')

```
## 参数列表
criterion='entropy'即为ID3算法  
criterion='gini'即为CART算法（默认参数）

![参数列表](./WechatIMG16.jpeg)

## 分类器方法

- 使用 `fit` 方法 数据拟合
- 使用 `predict` 方法 数据预测
- 使用 `score` 方法 得到准确率

表格：

![分类器方法](./WechatIMG18.jpeg)

### 流程：
#### 准备阶段：
1. 对训练集、测试集的数据进行探索，分析数据质量   
infro()，了解数据表的基本情况，行数、列数、每列的数据类型、数据完整度   
describe(),了解数据表的统计情况，总数、平均数、标准差、最小值、最大值   
describe(include=['O'])，查看字符串类型的整体情况   
head(n)，看前n行数据
tail(n)，看后n行数据

2. 并对数据进行清洗，
数据类型不对的转化数据类型
数值型数据缺失值用均值填补：df['某列'].fillna(df['某列'].mean(),inplace=True)
字符型数据缺失值用众数填补：df['某列'].fillna('某值',inplace=True)
3. 然后通过特征选择对数据进行降维，方便后续分类运算；
删减：无意义字段：ID，样本名字，缺失值过多的字段，过于混乱无规律字段

#### 分类阶段：
首先通过训练集的特征矩阵、分类结果得到决策树分类器，   
然后将分类器用于测试集。   
然后我们对决策树分类器的准确性进行分析，   
并对决策树模型进行可视化。

- [模型1代码](module1.py)
- [模型2代码](module2.py)
- [模型3代码](module3.py)
- [模型4代码](module4.py)
- [模型5代码](module5.py)
- [模型6代码](module6.py)
-直接看modele6.py即可
