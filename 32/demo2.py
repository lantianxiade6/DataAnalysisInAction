import numpy as np
#转移矩阵（等级沉没，转移矩阵的某行全是0，最后该网页的PR是0）
M=np.array([
    [0,0,1/2,1],
    [1,0,0,0],
    [0,0,0,0],
    [0,1,1/2,0]
])
#初始影响力
w0=np.array([1/4,1/4,1/4,1/4])
w=w0
for i in range(100):
    w=np.dot(M,w)
print(w)
'''[0.375 0.25  0.    0.375]'''