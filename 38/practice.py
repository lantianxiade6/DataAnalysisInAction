import matplotlib
matplotlib.use('Qt4Agg')
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image

#对歌单做词云
#https://music.163.com/#/playlist?id=753776811
#http://music.163.com/api/playlist/detail?id=753776811


url='http://music.163.com/api/playlist/detail?id=753776811'
headers = {
  'Referer': 'http://music.163.com',
  'Host': 'music.163.com',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
res = requests.request('GET', url, headers=headers)#发起请求，得到响应
#print(res.json())

if 'result' in res.json():#用json解析，检查有没有result这个key
    if 'tracks' in res.json()['result']:
        songlist=[]
        for track in res.json()['result']['tracks']:
            songlist.append(track['name'])#将每一个歌名存入list

#print(songlist)

# 去掉停用词
def remove_stop_words(f):
  stop_words = ['作词', '作曲', '编曲', 'Arranger', '录音', '混音', '人声', 'Vocal', '弦乐', 'Keyboard', '键盘', '编辑', '助理',
                'Assistants', 'Mixing', 'Editing', 'Recording', '音乐', '制作', 'Producer', '发行', 'produced', 'and',
                'distributed','(必胜客新春版)']
  for stop_word in stop_words:
    f = f.replace(stop_word, '')
  return f

def plt_show():
  try:
    plt.show()
  except UnicodeDecodeError:
    plt_show()#报UnicodeDecodeError错就重试

# 生成词云
def create_word_cloud(songlist):
  cut_text=""
  for f in songlist:
    f = remove_stop_words(f)#调用函数remove_stop_words，去掉停词
    tempt = " ".join(jieba.cut(f, cut_all=False, HMM=True))#分词
    cut_text=cut_text+" "+tempt
  wc = WordCloud(
    font_path="./38/wc.ttf",
    collocations=False,#词语不重复
    max_words=100,
    width=2000,
    height=1200,
  )
  wordcloud = wc.generate(cut_text)#生成词云
  # 写词云图片
  wordcloud.to_file("./38/wordcloud2.jpg")
  # 显示词云文件
  plt.imshow(wordcloud)
  plt.axis("off")
  plt_show()#调用函数plt_show画图

create_word_cloud(songlist)