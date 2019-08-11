# 多项式贝叶斯分类器
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn import metrics

train_news = fetch_20newsgroups(subset="train")#下载一个dataset
test_news = fetch_20newsgroups(subset="test")
print('one data of train_news:',train_news.data[0])
print('target of train_news:',train_news.target)

tf = TfidfVectorizer(stop_words='english', max_df=0.5)#stop_words为'english'或list,并过滤掉超过max_df的词语
train_features = tf.fit_transform(train_news.data)#转为文档词条矩阵，作为特征集，注意用的是fit_transform,即训练+转换

clf = MultinomialNB(alpha=0.001).fit(train_features, train_news.target)#多项式贝叶斯分类器
#test_tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5, vocabulary=train_vocabulary)
test_features=tf.transform(test_news.data)#要用和训练集一样的词语作为特征集，注意用的是_transform,即仅转换
predicted_labels=clf.predict(test_features)#预测测试集
print('predicted_labels:',predicted_labels)
print('accuracy_score:',metrics.accuracy_score(test_news.target, predicted_labels))#计算准确率