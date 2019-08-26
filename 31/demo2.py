# -*- coding: utf-8 -*-
from efficient_apriori import apriori
from lxml import etree
import time
from selenium import webdriver
import csv

#需安装Chrome和ChromeDriver（http://npm.taobao.org/mirrors/chromedriver/），两者版本要对应，
#chromedriver.exe 要放在 Python或Anaconda 的 Scripts 目录下
driver = webdriver.Chrome()#会模拟一个chrome浏览器进行访问

# 设置想要下载的导演 数据集
director = u'宁浩'
# 写 CSV 文件
file_name = './30/' + director + '.csv'#csv文件路径
base_url = 'https://movie.douban.com/subject_search?search_text=' + director + '&cat=1002&start='#网址
out = open(file_name, 'w', newline='', encoding='utf-8-sig')#以写入为目的打开文件，utf-8-sig可以解决中文乱码问题
csv_write = csv.writer(out, dialect='excel')#将csv.writer方法包装为csv_write

#关于如何获取一个html元素的xpath
#打开chrome-右上角更多工具-扩展程序-左上角扩展程序-打开Chrome网上应用店（需翻墙）-搜索“xpath helper"-添加至chrome
#快捷键Ctrl+Shift+X，并将鼠标点击或悬在目标（如第一个电影名字）上，就会出现黑色框显示目标的xpath,如
#/html/body/div[@id='wrapper']/div[@id='root']/div[@class='sc-gqjmRU koaMsN']/div[@class='_tl97eqioz']/div[@class='_4q0n0wup2']/div[1]/div[@class='sc-bZQynM lCDjx sc-bxivhb hRIaFd'][1]/div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']
#寻找XPath是一个找规律的过程，一般以//开头，
#再找如class='item-root'的节点或id='root'等等
#尝试去掉某些内容(特别是中间），会得到所有电影名字的xpath
#导演演员表：/html/body/div[@id='wrapper']/div[@id='root']/div[@class='sc-gqjmRU koaMsN']/div[@class='_tl97eqioz']/div[@class='_4q0n0wup2']/div[1]/div[@class='sc-bZQynM lCDjx sc-bxivhb hRIaFd'][1]/div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']

# 下载指定页面的数据
def download(request_url):
  driver.get(request_url)#请求request_url
  time.sleep(1)#暂停1秒，确保html数据完全返回
  html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")#？？
  html = etree.HTML(html)#用lxml提取html内容
  # 设置电影名称，导演演员 的 XPATH
  movie_lists = html.xpath(
    "/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
  name_lists = html.xpath(
    "/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")
  # 获取返回的数据个数
  num = len(movie_lists)
  if num > 15:  # 第一页会有 16 条数据
    # 默认第一个不是，所以需要去掉
    movie_lists = movie_lists[1:]
    name_lists = name_lists[1:]
  for (movie, name_list) in zip(movie_lists, name_lists):
    # 会存在数据为空的情况，如果为空，则不执行本循环后面的代码，直接进入下一个循环
    if name_list.text is None:
      continue
    # 显示下演员名称
    print(name_list.text)
    names = name_list.text.split('/')#按/分割
    # 判断导演是否为指定的 director，不是的话不会存入csv
    if names[0].strip() == director:
      # 将第一个字段设置为电影名称
      names[0] = movie.text
      csv_write.writerow(names)#写入csv
  print('OK')  # 代表这页数据下载成功
  if num >= 15:
    # 继续下一页
    return True
  else:
    # 没有下一页
    return False


# 开始的 ID 为 0，每页增加 15
start = 0
while start < 10000:  # 最多抽取 1 万部电影
  request_url = base_url + str(start)#将start拼接到base_url里面
  # 下载数据，并返回是否有下一页
  flag = download(request_url)#调用download函数
  if flag:#如果调用download成功
    start = start + 15
  else:
    break
out.close()#关闭csv
print('finished')

## 直接请求是请求不到的，必须用模拟浏览器的做法（Selenium）
# import requests
# response=requests.get('https://movie.douban.com/subject_search?search_text=%E5%AE%81%E6%B5%A9&cat=1002&start=0')
# print(response.text)