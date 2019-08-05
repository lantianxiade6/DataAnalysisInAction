from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# 加载数据
digits = load_digits()#内置数据集：手写数字数据集
data = digits.data
# 数据探索
print(data.shape)#(1797, 64)
# 查看第一幅图像，相当于x
print(digits.images[0])
'''[[ 0.  0.  5. 13.  9.  1.  0.  0.]
 [ 0.  0. 13. 15. 10. 15.  5.  0.]
 [ 0.  3. 15.  2.  0. 11.  8.  0.]
 [ 0.  4. 12.  0.  0.  8.  8.  0.]
 [ 0.  5.  8.  0.  0.  9.  8.  0.]
 [ 0.  4. 11.  0.  1. 12.  7.  0.]
 [ 0.  2. 14.  5. 10. 12.  0.  0.]
 [ 0.  0.  6. 13. 10.  0.  0.  0.]]'''
# 第一幅图像代表的数字含义，相当于y
print(digits.target[0])#0
# 将第一幅图像显示出来
plt.gray()
plt.imshow(digits.images[0])#见images[0].png
plt.show()