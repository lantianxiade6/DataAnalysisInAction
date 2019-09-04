# coding=utf-8
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import pylab
import cv2#pip install opencv-python
import numpy as np
from scipy import signal

# 读取灰度图像
img = cv2.imread("./43/haibao.jpeg", 0)
print(img)
'''
[[190 190 190 ... 198 198 198]
 [190 190 190 ... 198 198 198]
 [190 190 190 ... 198 198 198]
 ...
 [185 185 185 ... 193 193 193]
 [190 190 190 ... 198 198 198]
 [211 211 211 ... 219 219 219]]
'''
# 显示灰度图像
plt.imshow(img, cmap="gray")
pylab.show()
# 设置卷积核
fil = np.array(
  [
    [-1, -1, 0],
    [-1, 0, 1],
    [0, 1, 1]
  ]
)
# 卷积操作
res = signal.convolve2d(img, fil, mode='valid')
print(res)
'''
[[  0   0   0 ...   0   0   0]
 [  0   0   0 ...   0   0   0]
 [  0   0   0 ...   0   0   0]
 ...
 [  2   2   2 ...   6   6   6]
 [  0   0   0 ...   2   2   2]
 [-52 -52 -52 ... -52 -52 -52]]
'''
# 显示卷积后的图片
plt.imshow(res, cmap="gray")
pylab.show()
