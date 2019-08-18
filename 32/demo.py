import numpy as np
#转移矩阵
M=np.array([
    [0,1/2,1,0],
    [1/3,0,0,1/2],
    [1/3,0,0,1/2],
    [1/3,1/2,0,0]
])
#初始影响力
w0=np.array([1/4,1/4,1/4,1/4])
w=w0
for i in range(100):
    w=np.dot(M,w)
print(w)