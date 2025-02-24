# coding=utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vec = TfidfVectorizer()#创建TfidfVectorizer类，一个TF-IDF计算器

documents = [
    'this is the bayes document',
    'this is the second second document',
    'and the third one',
    'is this the document'
]
tfidf_matrix = tfidf_vec.fit_transform(documents)#放入英文文档，存入一个list，正式计算TF-IDF

print('不重复的词:', tfidf_vec.get_feature_names())#输出特征

'''output
不重复的词: ['and', 'bayes', 'document', 'is', 'one', 'second', 'the', 'third', 'this']
'''
print('每个单词的 ID:', tfidf_vec.vocabulary_)#输出每个特征的ID

'''output
每个单词的 ID: {'this': 8, 'is': 3, 'the': 6, 'bayes': 1, 'document': 2, 'second': 5, 'and': 0, 'third': 7, 'one': 4}
'''
#tfidf_vec还有idf_,stop_words_这两个属性
print('每个单词的 tfidf 值:', tfidf_matrix.toarray())#4*9#4个文档，9个特征

'''output
每个单词的 tfidf 值: [[0.         0.63314609 0.40412895 0.40412895 0.         0.
  0.33040189 0.         0.40412895]
 [0.         0.         0.27230147 0.27230147 0.         0.85322574
  0.22262429 0.         0.27230147]
 [0.55280532 0.         0.         0.         0.55280532 0.
  0.28847675 0.55280532 0.        ]
 [0.         0.         0.52210862 0.52210862 0.         0.
  0.42685801 0.         0.52210862]]

'''