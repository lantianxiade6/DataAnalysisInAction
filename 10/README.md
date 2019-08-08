1. 打开网页
2. 提取数据   
HTML页面->XPath   
JSON数据->JSON解析   
3. 保存数据

实例：爬取豆瓣上面的王祖贤图片  
豆瓣首页-在搜索框输入王祖贤-选择图片-查看开发者工具-Network-XHR  
可以查看Headers和Preview
https://www.douban.com/j/search_photo?q=%E7%8E%8B%E7%A5%96%E8%B4%A4&limit=20&start=0  
滚动到网页最底会发现出现新的链接：
https://www.douban.com/j/search_photo?q=%E7%8E%8B%E7%A5%96%E8%B4%A4&limit=20&start=20
