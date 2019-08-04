from sklearn.feature_extraction.text import TfidfVectorizer

#TF-IDF
train_contents=["I have a pen","I have an apple","today is a good day"]#如果为中文，应该先切词，再类似地变成空格间隔的list
tf = TfidfVectorizer(stop_words='english', max_df=0.8)#stop_words为'english'或list,并过滤掉超过max_df的词语
features = tf.fit_transform(train_contents)
print(features.todense())#得到文档词条矩阵（行是文档，列是词条）
print(tf.vocabulary_)#词对应在文档词条矩阵中的列