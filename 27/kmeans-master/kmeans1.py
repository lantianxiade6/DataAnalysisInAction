# -*- coding: utf-8 -*-
# 使用K-means对图像进行聚类，显示分割标识的可视化（k=2)
import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans
from sklearn import preprocessing

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
            # 得到点(x,y)的三个通道值（RGB，数据均在0-255之间），并存入data
            c1, c2, c3 = img.getpixel((x, y))
            data.append([c1, c2, c3])
    f.close()
    # 采用Min-Max规范化每个通道的数值
    mm = preprocessing.MinMaxScaler()
    data = mm.fit_transform(data)
    return np.mat(data), width, height#np.mat是转矩阵

# 加载图像，得到规范化的结果img，以及图像尺寸
img, width, height = load_data('./27/kmeans-master/weixin.jpg')

# 用K-Means对图像进行2聚类
kmeans =KMeans(n_clusters=2)
kmeans.fit(img)
label = kmeans.predict(img)
print(label)
# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape([width, height])#因为是2聚类，所以结果是一个0-1的向量，需转矩阵
print(label)
# 创建个新图像pic_mark，用来保存图像聚类的结果，并设置不同的灰度值
pic_mark = image.new("L", (width, height))
for x in range(width):
    for y in range(height):
        # 根据类别设置图像灰度, 类别0 灰度值为255（=256/（0+1）-1）， 类别1 灰度值为127（=256/（1+1）-1）
        pic_mark.putpixel((x, y), int(256/(label[x][y]+1))-1)
pic_mark.save("./27/kmeans-master/weixin_mark.jpg", "JPEG")