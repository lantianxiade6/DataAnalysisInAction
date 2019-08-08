# coding:utf-8

#批量下载豆瓣上的王祖贤图片
import requests
import json
query='王祖贤'
'''下载图片'''
def download(src,id):
    dir='./10/photo/'+str(id)+'.jpg'#图片保存路径
    log=open('./10/photo/error_log.txt','a')#报错用的日志文件
    try:
        pic=requests.get(src,timeout=10)#设置超时10秒
        fp=open(dir,'wb')#新建一张空图片
        fp.write(pic.content)#写入图片内容
        fp.close()#关闭图片
    #except requests.exceptions.ConnectionError:
    except:
        print(id,'图片无法下载')
        print(id+'\n',log)#如果报错，写入到log，后面可以重新或手动下载

'''for 循环 请求全部的url'''
for i in range(0,100,20):#本来是0,24919,20 下100张图片就够了(但实际我只保留两张到Github)
    url='https://www.douban.com/j/search_photo?q='+query+'limit=20&start='+str(i)#每20一个路径
    html=requests.get(url).text#请求结果
    response=json.loads(html,encoding='utf-8')#将JSON格式转换为Python对象(JSON格式很好处理)
    for image in response['images']:
        print('成功下载',image['src'])#查看当前下载的图片的路径
        download(image['src'],image['id'])#调用download函数，下载图片