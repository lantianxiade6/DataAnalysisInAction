from selenium import webdriver
import time

browser = webdriver.Chrome()


#【1】登录微博
def weibo_login(username, password):
  # 打开微博登录页
  browser.get('https://passport.weibo.cn/signin/login')#打开网页
  browser.implicitly_wait(5)#超时5秒
  time.sleep(1)#等待1秒
  # 填写登录信息：用户名、密码
  browser.find_element_by_id("loginName").send_keys(username)#往id=loginName的网页元素中输入文字
  browser.find_element_by_id("loginPassword").send_keys(password)#往id=loginPassword的网页元素中输入文字
  time.sleep(1)
  # 点击登录按钮
  browser.find_element_by_id("loginAction").click()#点击id=loginAction的网页元素
  time.sleep(1)

# 设置用户名、密码
username = 'xxx@sina.cn'
password = "xxx"
weibo_login(username, password)#登录微博


# #【2】添加指定的用户（加关注）
# def add_follow(uid):
#   browser.get('https://m.weibo.com/u/' + str(uid))#打开网页
#   time.sleep(1)
#   # browser.find_element_by_id("follow").click()
#   follow_button = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')#找到指定xpath的网页元素
#   follow_button.click()#点击该元素
#   time.sleep(1)
#   # 选择分组
#   #group_button = browser.find_element_by_xpath('//div[@class="m-btn m-btn-white m-btn-text-black"]')
#   group_button = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/footer/div[2]/a')#用ctrl+Shift+X测试得出来即可
#   group_button.click()
#   time.sleep(1)


# # 每天学点心理学 UID
# uid = '1890826225'
# add_follow(uid)


# #【3】给指定某条微博添加内容（写评论）
# def add_comment(weibo_url, content):
#   browser.get(weibo_url)#打开网页
#   browser.implicitly_wait(5)
#   #对于并列的classname而言，如“class="m-box-center-a main-text m-text-cut focus"”，需要去掉空格，并且加点
#   #可以自己在console里面用js找，如：window.document.getElementsByClassName('textarea')
#   browser.find_element_by_css_selector('.m-box-center-a.main-text.m-text-cut.focus').click()#要先点击“发表评论”后面的元素才会渲染出来
#   content_textarea = browser.find_element_by_css_selector(".textarea")#找到输入评论的框
#   content_textarea.clear()#清空
#   content_textarea.send_keys(content)#输入文字
#   time.sleep(2)
#   browser.find_element_by_css_selector(".btn-send").click()#点击“发送”按钮
#   time.sleep(1)

# add_comment('https://m.weibo.cn/detail/4410580809437623','Love Kobe forever again')


#【4】发文字微博（发微博）
def post_weibo(content):
  # 跳转到用户的首页
  browser.get('https://weibo.com')#打开网页
  browser.implicitly_wait(5)
  # 点击右上角的发布按钮
  post_button = browser.find_element_by_css_selector("[node-type='publish']").click()
  # 在弹出的文本框中输入内容
  content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
  time.sleep(2)
  # 点击发布按钮
  post_button = browser.find_element_by_css_selector("[node-type='submit']").click()
  time.sleep(1)


# # 给指定的微博写评论
# weibo_url = 'https://weibo.com/1890826225/HjjqSahwl'
# content = 'Gook Luck! 好运已上路！'
# # 自动发微博
# content = '每天学点心理学'
# post_weibo(content)
