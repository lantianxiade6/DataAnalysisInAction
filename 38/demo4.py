# -*- coding:utf-8 -*-

# 网易云音乐 通过歌手 ID，生成该歌手的词云
import matplotlib
matplotlib.use('Qt4Agg')
import requests
import sys
import re
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
from lxml import etree

# plt.figure()

headers = {
  'Referer': 'http://music.163.com',
  'Host': 'music.163.com',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'User-Agent': 'Chrome/10'
}

# 去掉停用词
def remove_stop_words(f):
  stop_words = ['作词', '作曲', '编曲', 'Arranger', '录音', '混音', '人声', 'Vocal', '弦乐', 'Keyboard', '键盘', '编辑', '助理',
                'Assistants', 'Mixing', 'Editing', 'Recording', '音乐', '制作', 'Producer', '发行', 'produced', 'and',
                'distributed']
  for stop_word in stop_words:
    f = f.replace(stop_word, '')
  return f

def plt_show():
  try:
    plt.show()
  except UnicodeDecodeError:
    plt_show()#报UnicodeDecodeError错就重试

# 生成词云
def create_word_cloud(f):
  print('根据词频，开始生成词云!')
  f = remove_stop_words(f)#调用函数remove_stop_words，去掉停词
  jieba.add_word("毛不易")#增加词语
  cut_text = " ".join(jieba.cut(f, cut_all=False, HMM=True))#分词
  wc = WordCloud(
    font_path="./38/wc.ttf",
    collocations=False,#词语不重复
    max_words=100,
    width=2000,
    height=1200,
  )
  #print(cut_text)
  wordcloud = wc.generate(cut_text)#生成词云
  # 写词云图片
  wordcloud.to_file("./38/wordcloud.jpg")
  # 显示词云文件
  plt.imshow(wordcloud)
  plt.axis("off")
  plt_show()#调用函数plt_show画图


# 得到指定歌手页面 热门前 50 的歌曲 ID，歌曲名
def get_songs(artist_id):
  page_url = 'https://music.163.com/artist?id=' + artist_id
  # 获取网页 HTML
  res = requests.request('GET', page_url, headers=headers)#请求网页，得到html
  # 用 XPath 解析 前 50 首热门歌曲
  html = etree.HTML(res.text)#用xpath解析
  hrefs = html.xpath("//*[@id='hotsong-list']//a/@href")#？
  names = html.xpath("//*[@id='hotsong-list']//a/text()")#？
  # 设置热门歌曲的 ID，歌曲名称
  song_ids = []
  song_names = []
  for href, name in zip(hrefs, names):
    song_ids.append(href[9:])#如“/song?id=569213220”，不用前面的字符
    song_names.append(name)
    print(href, '  ', name)
  return song_ids, song_names


# 得到某一首歌的歌词
def get_song_lyric(headers, lyric_url):
  res = requests.request('GET', lyric_url, headers=headers)#发起请求，得到响应
  if 'lrc' in res.json():#用json解析，检查有没有lrc这个key
    lyric = res.json()['lrc']['lyric']#直接取lrc这个key里面的lyric这个key的值
    new_lyric = re.sub(r'[\d:.[\]]', '', lyric)#去掉数字，冒号和[]和.
    return new_lyric
  else:
    #print(res.json())
    return ''

# 设置歌手 ID，毛不易为 12138269
artist_id = '12138269'
[song_ids, song_names] = get_songs(artist_id)#调用函数get_songs，得到歌曲id和歌名列表
# 所有歌词
all_word = ''
# 获取每首歌歌词
for (song_id, song_name) in zip(song_ids, song_names):
  # 歌词 API URL
  lyric_url = 'http://music.163.com/api/song/lyric?os=pc&id=' + song_id + '&lv=-1&kv=-1&tv=-1'#？不知道在网页上怎么找到的，但的确是对的
  lyric = get_song_lyric(headers, lyric_url)#函数调用get_song_lyric，获取歌词
  all_word = all_word + ' ' + lyric#全部歌词拼接在一起
  print(song_name)

# 根据词频 生成词云
create_word_cloud(all_word)#调用函数create_word_cloud，生成词云
