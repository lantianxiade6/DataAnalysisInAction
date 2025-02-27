# coding=utf-8
# 使用 LeNet 模型对 Mnist 手写数字进行识别
import keras
from keras.datasets import mnist
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten
from keras.models import Sequential

# 数据加载
(train_x, train_y), (test_x, test_y) = mnist.load_data()# 输入数据为 mnist 数据集
print(train_x.shape)
print(train_y.shape)
print(test_x.shape)
print(test_y.shape)
print(train_y)
'''
(60000, 28, 28)
(60000,)
(10000, 28, 28)
(10000,)
[5 0 4 ... 5 6 8]
'''
train_x = train_x.reshape(train_x.shape[0], 28, 28, 1)#应该是重新改成4维数据
test_x = test_x.reshape(test_x.shape[0], 28, 28, 1)
train_x = train_x / 255#应该是除以最大值
test_x = test_x / 255
train_y = keras.utils.to_categorical(train_y, 10)#应该是类似转为factor
test_y = keras.utils.to_categorical(test_y, 10)

# 【1】创建序贯模型
model = Sequential()
# 【2】第一层卷积层：6 个卷积核，大小为 5∗5, relu 激活函数
model.add(Conv2D(6, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)))
# 【3】第二层池化层：最大池化
model.add(MaxPooling2D(pool_size=(2, 2)))
# 【4】第三层卷积层：16 个卷积核，大小为 5*5，relu 激活函数
model.add(Conv2D(16, kernel_size=(5, 5), activation='relu'))
# 【5】第二层池化层：最大池化
model.add(MaxPooling2D(pool_size=(2, 2)))
# 【6】将参数进行扁平化，在 LeNet5 中称之为卷积层，实际上这一层是一维向量，和全连接层一样
model.add(Flatten())
model.add(Dense(120, activation='relu'))
# 【7】全连接层，输出节点个数为 84 个
model.add(Dense(84, activation='relu'))
# 【8】输出层 用 softmax 激活函数计算分类概率
model.add(Dense(10, activation='softmax'))
# 【9】设置损失函数和优化器配置
model.compile(loss=keras.metrics.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])

# 传入训练数据进行训练，epochs控制训练次数
model.fit(train_x, train_y, batch_size=128, epochs=2, verbose=1, validation_data=(test_x, test_y))
# 对结果进行评估
score = model.evaluate(test_x, test_y)
print('误差:%0.4lf' % score[0])
print('准确率:', score[1])


'''output
Using TensorFlow backend.
Train on 60000 samples, validate on 10000 samples
Epoch 1/2
2019-09-06 18:03:37.521908: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX AVX2
2019-09-06 18:03:37.555469: I tensorflow/core/common_runtime/process_util.cc:69] Creating new thread pool with default inter op setting: 8. Tune using inter_op_parallelism_threads for best performance.
60000/60000 [==============================] - 21s 352us/step - loss: 0.3409 - acc: 0.8971 - val_loss: 0.1212 - val_acc: 0.9622
Epoch 2/2
60000/60000 [==============================] - 18s 293us/step - loss: 0.1025 - acc: 0.9676 - val_loss: 0.0688 - val_acc: 0.9778
10000/10000 [==============================] - 1s 137us/step
误差:0.0688
准确率: 0.9778
'''