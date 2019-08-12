## 如何进行乳腺癌检测

### 如何使用 `SVM`
1. `SVM` 可以做回归
  - 使用 `SVR`或`LinearSVR`(Support Vector Regression)
2. 也可以做分类器
  - 使用 `SVC` -- 非线性(Support Vector Classification)。      
  - 或者 `LinearSVC` -- 线性分类器，用于处理线性可分数据，只能使用线性核函数
在SVC中，我们既可以使用到线性核函数（进行线性划分），也能使用高维的核函数（进行非线性划分）

### 如何创建一个SVC分类器
`model=svm.SVC(kernel='rbf',C=1.0,gamma='auto')`
- kernel: 核函数   
1. linear: 线性核函数。在线性可分的情况下使用，运算速度快，效果好。但不能处理线性不可分的数据。   
2. poly: 多项式核函数。可以将数据从低维空间映射到高维空间，但参数比较多，计算量大。   
3. rbf: 高斯核函数（默认）。同样可以将样本映射到高维空间，且参数比较少，通常性能不错。   
4. sigmoid: sigmoid核函数。多层神经网络
- C:惩罚系数，指分错样本时的惩罚程度。默认是1.0。C越大，分类器的准确性越高，但同样容错率会越低，泛化能力会变差。
- gamma代表核函数的系数，默认为特征数的倒数。

### 训练分类器
`model.fit(train_x,train_y)#train_x是特征矩阵，train_y是分类标识`
### 预测
`prediction=model.predict(text_X)`

## 实例

> 乳腺癌诊断数据集在本讲的根目录

### 肿瘤可以分为良性和恶性

### 数据表共32个字段

![](WechatIMG70.jpeg)

### 分类器执行流程

![](WechatIMG71.jpeg)

### 代码
- 探索

  [数据探索代码](./discover.py)

- [清洗](./dataClean.py)

  `id` 没有实际含义  去掉

  `diagnosis` 取值 为  `B || M` 替换为 `0 || 1`

  `mean` `se` `worst` 代表不同的度量方式

  [SVM代码](./breastCancerData/breast_svm.py)
