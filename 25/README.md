## KNN
- 分类器  
`from sklearn.neighbors import KNeighborsClassifier`
- 回归  
`from sklearn.neighbors import KNeighborsRegressor`

## KNN分类器
`KNeighborsClassifier(n_neighbors=5,weights='uniform',algorithm='auto',leaf_size=30)`
- n_neighbors:K值，即邻居数量，默认是5
- weights权重   
1. uniform，代表邻居的权重相同   
2. distance，代表权重是距离的倒数   
3. 自定义函数，自定义不同距离所对应的权重  
- algorithm计算邻居的方法   
1. auto，根据数据情况自动选择合适的算法（默认为auto)   
2. kd_tree，也叫KD树，是多维空间的数据结构，方便对关键数据进行检索，不过KD树使用于维度少的情况，一般不超过20，否则效率会下降。   
3. ball_tree，也叫球树，也是多维空间的数据结构，它更适用于维度大的情况   
4. brute，也叫暴力搜索，采用线性扫描，训练集大的时候效率很低   
- leaf_size代表构建KD树或球树时的叶子数，它会影响树的构造和搜索速度，默认30。

## 手写识别

### 分析流程

![](WechatIMG82.jpeg)

1. 数据加载
2. 准备阶段
  - 样本的个数
  - 图像的形状
  - 识别结果
  - 可视化
  - 规范化
  - 生成特征矩阵
3. 分类阶段
  - 训练 -> 分类器
  - 测试集 准确率计算


## 代码
 [demo](./demo.py)  
 [knn](./knn.py)
