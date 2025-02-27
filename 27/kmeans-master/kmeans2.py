# -*- coding: utf-8 -*-
# 使用K-means对图像进行聚类，显示分割标识的可视化(k=16)
import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans
from sklearn import preprocessing
from skimage import color#如果报错，需要更新一下包pip install --upgrade scikit-image

# 加载图像，并对数据进行规范化
def load_data(filePath):
    # 读文件
    f = open(filePath,'rb')
    data = []
    # 得到图像的像素值
    img = image.open(f)
    # 得到图像尺寸
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # 得到点(x,y)的三个通道值（RGB)
            c1, c2, c3 = img.getpixel((x, y))
            data.append([c1, c2, c3])
    f.close()
    # 采用Min-Max规范化
    mm = preprocessing.MinMaxScaler()
    data = mm.fit_transform(data)
    return np.mat(data), width, height

# 加载图像，得到规范化的结果img，以及图像尺寸
img, width, height = load_data('./27/kmeans-master/weixin.jpg')

# 用K-Means对图像进行16聚类
kmeans =KMeans(n_clusters=16)
kmeans.fit(img)
label = kmeans.predict(img)
print(label)#结果为类别0-15
# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape([width, height])
print(label)
# 将聚类标识矩阵转化为不同颜色的矩阵
label_color = (color.label2rgb(label)*255).astype(np.uint8)#转为rgb
label_color = label_color.transpose(1,0,2)#各轴数据互换
images = image.fromarray(label_color)#通过矩阵生成图片
images.save('./27/kmeans-master/weixin_mark_color.jpg')