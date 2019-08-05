# encoding:utf-8
import numpy as np
#连续数组的创建
x1 = np.arange(1,11,2) # 初始值，终值，步长（默认不包含最终值）
x2 = np.linspace(1,9,5) # 初始值，终值，元素个数（默认包含最终值）

print(x1)
print(x2)

''' output:
[1 3 5 7 9]
[1. 3. 5. 7. 9.]

'''