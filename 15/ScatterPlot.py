# encoding:utf-8
import matplotlib
matplotlib.use('Qt4Agg')#设置展示图片的后端
import matplotlib.pyplot as plt

## 散点图

plt.scatter(200,200,marker='x')#(200,200)坐标点画一个“x”，marker可以是"x",">""o"等
plt.show()#需手动关掉图片

