# -*- coding: utf-8 -*-
# 使用K-means对图像进行聚类，并显示聚类压缩后的图像（k=16)
import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.image as mpimg
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
            # 得到点(x,y)的三个通道值（RGB）
            c1, c2, c3 = img.getpixel((x, y))
            data.append([(c1+1)/256.0, (c2+1)/256.0, (c3+1)/256.0])#和kmeans1/2不同，不做最大最小规范话，直接加1除256（0-255的数据转为0-1）
    f.close()
    return np.mat(data), width, height
# 加载图像，得到规范化的结果imgData，以及图像尺寸
img, width, height = load_data('./27/kmeans-master/weixin.jpg')
# 用K-Means对图像进行16聚类
kmeans =KMeans(n_clusters=16)
label = kmeans.fit_predict(img)
# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape([width, height])
# 创建个新图像img，用来保存图像聚类压缩后的结果
img=image.new('RGB', (width, height))
for x in range(width):
    for y in range(height):
        #cluster_centers_是一个2维数组： [n_clusters, n_features]，即第几个聚类中心，第几个特征。
        #所以这里是取了第label[x,y]个聚类中心，和第0、1、2个特征（即0-1版RGB）
        #即每个（x,y)点的C1,C2,C3都是对应聚类中心label[x,y]的第0、1、2个特征（即R，G，B值）
        c1 = kmeans.cluster_centers_[label[x, y], 0]
        c2 = kmeans.cluster_centers_[label[x, y], 1]
        c3 = kmeans.cluster_centers_[label[x, y], 2]
        img.putpixel((x, y), (int(c1*256)-1, int(c2*256)-1, int(c3*256)-1))#再乘回256减1（0-1转为1-255）
img.save('./27/kmeans-master/weixin_new.jpg')#一模一样！！！