## K-Means

1. 类型： 非监督学习
2. 目的 ： 解决聚类问题
3. `K` == `K` 类
4. `Means` 代表的是 中心
5. 本质： 确定 `K` 类的中心点

### 工作原理

1. 选择 `K` 个点作为初始的类中心点
2. 将每个点分配到最近的类中心点，这就形成了k个类，然后重新计算每个类的中心点
3. 重复第二部 直到类不发生变化，或达到最大迭代次数

### 数据

根目录下面的 `kmeans-master`文件夹

### 流程
1. 数据规范化  
2. 创建k-means代码  
```
from sklearn.cluster import KMeans
Kmeans(n_cluster=8,init='K-means++',n_init=10,max_iter=300,tol=0.0001,precompute_distance='auto',verbose=0,random_state=None,copy_x=True,n_jobs=1,algorithm='auto')
```
n_cluster:K值  
max_iter：最大迭代次数，避免聚类很难收敛运行时间过长  
n_init：初始化中心点的运算次数，默认为10。运行n_init次，取其中最好的作为初始的中心点。  
init：初始值选择的方式
algorithm：k-means的实现算法，默认是auto
3. fit(data)对data数据进行聚类
4. predict(data)针对data的每一个样本，计算最近的类

### K-means和KNN的区别
K-Means|KNN
---|---
聚类算法|分类算法
非监督学习|有监督学习
K代表K类|K代表K个最近的邻居