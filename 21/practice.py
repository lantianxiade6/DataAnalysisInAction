import os
import jieba
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn import metrics

def cut_words(file_path):
    """
    对文档进行切词
    :param file_path: txt文档路径
    :return: 用空格分割的字符串
    """
    text=open(file_path,'r',encoding='gb18030').read()#读入txt
    textcut=jieba.cut(text)#jieba分词
    text_with_spaces=' '.join(textcut)#用空格串连
    return text_with_spaces

def loadfile(file_dir,label):
    """
    加载路径下的所有文件
    :param file_dir: txt文件目录
    :param label: 文档标签
    :return: 分词后的文档列表和标签
    """
    file_list=os.listdir(file_dir)#目录下的所有文件
    words_list=[]
    label_list=[]
    for file in file_list:#遍历每一个文件
        file_path=file_dir+'/'+file#路径+文件名
        words_list.append(cut_words(file_path))#调用cut_words进行切词
        label_list.append(label)
    return words_list,label_list

#读取训练集
train_words1,train_labels1=loadfile('./21/text classification/train/女性','女性')#读取训练集
train_words2,train_labels2=loadfile('./21/text classification/train/体育','体育')
train_words3,train_labels3=loadfile('./21/text classification/train/文学','文学')
train_words4,train_labels4=loadfile('./21/text classification/train/校园','校园')
train_words=train_words1+train_words2+train_words3+train_words4#合并训练集
train_labels=train_labels1+train_labels2+train_labels3+train_labels4
print(len(train_words))
# print(train_words1[0])

#读取测试集
test_words1,test_labels1=loadfile('./21/text classification/test/女性','女性')#读取测试集
test_words2,test_labels2=loadfile('./21/text classification/test/体育','体育')
test_words3,test_labels3=loadfile('./21/text classification/test/文学','文学')
test_words4,test_labels4=loadfile('./21/text classification/test/校园','校园')
test_words=test_words1+test_words2+test_words3+test_words4#合并测试集
test_labels=test_labels1+test_labels2+test_labels3+test_labels4
print(len(test_words))

#读取停词
stop_words=[line.strip() for line in open('./21/text classification/stop/stopword.txt','r',encoding='utf-8-sig').readlines()]
print(stop_words[:5])

# 多项式贝叶斯分类器
tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)#stop_words为'english'或list,并过滤掉超过max_df的词语
train_features = tf.fit_transform(train_words)#转为文档词条矩阵，作为特征集，注意用的是fit_transform,即训练+转换

clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)#多项式贝叶斯分类器
test_features=tf.transform(test_words)#要用和训练集一样的词语作为特征集，注意用的是_transform,即仅转换
predicted_labels=clf.predict(test_features)#预测测试集
print('accuracy_score:',metrics.accuracy_score(test_labels, predicted_labels))#计算准确率

'''output
accuracy_score: 0.91
'''