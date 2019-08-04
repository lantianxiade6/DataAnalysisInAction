# 多项式贝叶斯分类器
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups

news = fetch_20newsgroups(subset="all")#下载一个dataset
# print(news.target[0])
# print(len(news.data))
# print(news.data[0])
tf = TfidfVectorizer(stop_words='english', max_df=0.5)#stop_words为'english'或list,并过滤掉超过max_df的词语
train_features = tf.fit_transform(news.data)#转为文档词条矩阵，作为特征集
clf = MultinomialNB(alpha=0.001).fit(train_features, news.target)#多项式贝叶斯分类器