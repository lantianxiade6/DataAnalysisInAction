import numpy as np

# 10个训练数据和分类结果
X=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Y=[ 1, 1, 1,-1,-1,-1, 1, 1, 1,-1]

# 3个基础分类器(弱分类器)
def f1(x):
    if x<=2.5:
        return 1
    else:
        return -1

def f2(x):
    if x<=5.5:
        return -1
    else:
        return 1

def f3(x):
    if x<=8.5:
        return 1
    else:
        return -1

# 自定义函数，计算分类器的错误率
def error(f,x,y,w):
    err=0
    for i in range(len(x)):
        if(f(x[i])!=y[i]):
            err=err+(1*w[i])
    return err

# 自定义函数，计算分类器的权重a_k
def a_k(e):
    return np.log((1-e)/e)/2

# 自定义函数，计算每个样本的权重
def w_k_1(w_k,a_k,y,f,x):
    result=[]
    for i in range(len(x)):
        result.append(w_k[i]*np.exp(-1*a_k*y[i]*f(x[i])))
    return result/sum(result)
    

print('第1轮---------------')
# 第1轮训练的权重 
w1=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

print(error(f1,X,Y,w1),error(f2,X,Y,w1),error(f3,X,Y,w1))
#0.30000000000000004 0.4 0.30000000000000004
#->选f1作为第一轮训练的分类器

# 分类器的权重a_k
a1=a_k(error(f1,X,Y,w1))
print(a1)#0.4236489301936017


print('第2轮---------------')
# 第2轮的权重
w2=w_k_1(w1,a1,Y,f1,X)
print(w2)
#[0.07142857 0.07142857 0.07142857 0.07142857 0.07142857 0.07142857
# 0.16666667 0.16666667 0.16666667 0.07142857]
print(error(f1,X,Y,w2),error(f2,X,Y,w2),error(f3,X,Y,w2))
#0.4999999999999999 0.2857142857142857 0.21428571428571427
#->选f3作为第二轮训练的分类器

# 分类器的权重a_k
a2=a_k(error(f3,X,Y,w2))
print(a2)#0.6496414920651304


print('第3轮---------------')
# 第3轮的权重
w3=w_k_1(w2,a2,Y,f3,X)
print(w3)
#[0.04545455 0.04545455 0.04545455 0.16666667 0.16666667 0.16666667
# 0.10606061 0.10606061 0.10606061 0.04545455]
print(error(f1,X,Y,w3),error(f2,X,Y,w3),error(f3,X,Y,w3))
#0.3181818181818182 0.18181818181818185 0.5
#->选f2作为第三轮训练的分类器

# 分类器的权重a_k
a3=a_k(error(f2,X,Y,w3))
print(a3)#0.752038698388137


print('最终强分类器---------------')
def G(x):
    result=[]
    for i in x:
        result.append(a1*f1(i)+a2*f3(i)+a3*f2(i))
    return result

print(G(X))
#[0.3212517238705951, 0.3212517238705951, 0.3212517238705951, -0.5260461365166083, -0.5260461365166083, -0.5260461365166083, 0.9780312602596657, 0.9780312602596657, 0.9780312602596657, -0.3212517238705951]
# 由于f1-3的结果只能是1或-1，那么G(x)的结果是正数就判为1，是负就判为-1

def accuracy(y,predict):
    acc=0
    for i in range(len(y)):
        if y[i]*predict[i]>=0:#y和预测值同为正或同为负数
            acc+=1#则认为预测正确
    return acc/len(y)*100#正确率

print(accuracy(Y,G(X)))#100.0