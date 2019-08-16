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

[官方源码-没有跑](here_em.py)

## 评估聚类结果
```
from sklearn.metrics import calinski_harabaz_score
print(calinski_harabaz_score(data,prediction))
```
- 指标分数越高，代表聚类效果越好，也就是相同类中的差异越小，不同类之间的差异性大。
- 但聚类的结果含义，即具体每个类代表的含义，需要人工来分析。
- 聚类算法也可以作为其他数据挖掘算法的预处理阶段，这样我们就可以将数据进行降维。