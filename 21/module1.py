import nltk
#英文切词
#nltk.download()#跑一次即可，至少要安装里面的all-nltk
text="Sentiment analysis is a challenging subject in machine learning.\
 People express their emotions in language that is often obscured by sarcasm,\
  ambiguity, and plays on words, all of which could be very misleading for \
  both humans and computers. There's another Kaggle competition for movie review \
  sentiment analysis. In this tutorial we explore how Word2Vec can be applied to \
a similar problem.".lower()
word_list = nltk.word_tokenize(text) # 分词
# print(word_list)
print(nltk.pos_tag(word_list)) # 标注单词的词性