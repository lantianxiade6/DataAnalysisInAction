![](./EM下2.png)

## 代码
```
from sklearn.mixture import GaussianMixture
gmm=GaussianMixture(n_components=1,covariance_type='full',max_iter=100)
```
 - n_components：高斯混合模型的个数，也就是聚类个数，默认为1.
 - covariance_type：协方差类型。一个高斯混合模型的分布是有均值向量和协方差矩阵决定的。
   1. full:完全协方差，也就是元素都不为0  
   2. tied:相同的完全协方差  
   3. diag:对角协方差，也就是对角不为0，其余为0
   4. spherical,代表球面协方差，非对角为0，对角完全为0，呈现球面的特性
- max_iter：代表最大迭代次数，默认100

## 原理：
通过聚类算法把特征值相近的数据归为一类，不同类之间的差异较大  

[pipenv 环境](em.py)

[官方源码](here_em.py)

