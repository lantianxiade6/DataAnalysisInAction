![](./EM下2.png)

## 代码
```
from sklearn.mixture import GaussianMixture
gmm=GaussianMixture(n_components=1,covariance_type='full',max_iter=100)
```
 - n_components：高斯混合模型的个数，也就是聚类个数，默认为1.
 - covariance_type：协方差类型。一个高斯混合模型的分布是有均值向量和协方差矩阵决定的。
   1. full:完全协方差，也就是元素都不为0  
   2.  

[pipenv 环境](em.py)

[官方源码](here_em.py)

