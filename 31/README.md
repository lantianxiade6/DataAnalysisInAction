## 使用工具 
- 打开https://pypi.org/，搜索apriori，可以找到可以实现apriori的包，但不用下载，点进去可以看到具体pip怎么写
- 然后直接pip install efficient-apriori即可
- efficient-apriori 会把每一条数据中的项（item）放到一个集合（篮子）里来处理，不考虑项之间的先后顺序
- 一般来说最小支持度的常见取值有0.5,0.1，0.05。最小置信度的常见取值有1.0,0.9，0.8。然后再观察关联结果调整最小支持度和最小置信度的取值。
```python
itemsets, rules = apriori(data, min_support,  min_confidence)

```

- data 
  - 数据集，一个list数组类型，里面的值可以是集合也可以是列表
- min_support
  - 最小支持度，为0-1的数值，如0.5代表50%支持度
- min_confidence
  - 最小置信度，数值，1代表100%置信度
  

## 挖掘频繁集和规则 ` demo ` 上一讲的超市案例

[代码](demo1.py)

## 导演挖掘演员

流程

1. https://movie.douban.com/
2. 输入 名称，如宁浩，直接请求这个页面网址，观察网址规律和页面数据的规律
 - https://movie.douban.com/subject_search?search_text=宁浩&cat=1002
 - https://movie.douban.com/subject_search?search_text=宁浩&cat=1002&start=15
 - 在network里面第一条就是了，并发现返回结果是一个html, 但返回的html内容无法得知电影信息
 - 这就只能用selenium来模拟浏览器行为了

3. [抓取数据代码-xpath版](demo2.py)
4. [挖掘](demo3.py)
5. 总结

![总结](data_dig.png)

 