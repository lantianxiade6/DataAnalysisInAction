## sklearn 包

- 三个方法
  - 高斯朴素贝叶斯
   - 适应于 特征变量是连续变量 符合高斯分布 例如身高
  - 多项式朴素贝叶斯
   - 适应于 特征变量是离散变量 符合多项分布 例如单词出现的概率
  - 伯努利朴素贝叶斯
   - 适应于 特征变量是布尔变量 符合0/1分布 例如单词是否出现

## TF-IDF
用于评估某个词语对于一个文件集或文档库的其中一份文件的重要程度
- 词频 Term Frequency
  - 单词在文档中的次数
- 逆向文档频率 Inverse Document Frequency
  - 单词在文档中的区分度，一个单词出现在的文档数越少，就越能通过这个单词把该文档和其他文档区分开。

### 计算方法

- TF

![TF](WechatIMG41.jpeg)
- IDF

![IDF](WechatIMG42.jpeg)


```公式
TF-IDF = TF * IDF
```
使用TfidfVectorizer计算TF-IDF
`TfidfVectorizer(stop_words=stop_words,token_pattern=token_pattern`  
stop_words为停用词，一个list  
token_pattern为过滤规则，是一个正则表达式  

## 示例代码

[示例代码](./demo.py)

## 文档分类
- 基于分词的数据准备，包括分词、单词权重计算、去掉停用词  
- 应用朴素贝叶斯分类进行分类，首先通过训练集得到朴素贝叶斯分类器，然后将分类器应用于测试集，并与实际结果做对比，最终得到测试集的分类准确率。
![文档分类](WechatIMG49.jpeg)

- 英文分词
  - `nltk`
- 中文分词
  - `jieba`
  
## 直接看module5.py即可
[英文分词module1](./module1.py)  
[中文分词module2](./module2.py)  
加载停词  
`stop_words=[line.strip().decode('utf-8') for line in io.open('stop_words.txt').readlines()]`  
计算单词权重（即特征矩阵）  
```
tf=TfidfVectorizer(stop_words=stop_words,max_df=0.5)
#一个单词如果在50%的文档上都出现过了，那么它只携带了非常少的信息，就不作为分词统计了
features=tf.fit_transform(train_contents)
```
[单词权重module3](./module3.py)  
生成朴素贝叶斯分类器
```
#多项式贝叶斯分类器
from sklearn.naive_bayes import MultinominalNB
clf=MultinomialNB(alpha=0.001).fit(train_features,train_labels)
alpha=1是Laplace平滑  
0<alpha<1是Lidstone平滑，alpha越小，迭代次数越多，精度越高
```
[生成朴素贝叶斯分类器module4](./module4.py)  
使用生成的分类器做预测  
计算准确率  
[module5](./module5.py)  
[作业](./practice.py) 
