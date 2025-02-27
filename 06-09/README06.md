# 数据分析的基本概念
关联分析：Apriori算法-》商品捆绑销售  

数据仓库（Data Warehouse)  
数据挖掘（Data Mining)  
商业智能（Business Intelligence，简称BI）  

## 数据仓库
数据元Data Element:最小数据单位  
元数据MetaData:描述其他数据的数据，也称为“中介数据”  

## 数据挖掘  
1. 分类  
通过训练集得到一个分类模型，然后用这个模型对其他数据进行分类  
2. 聚类  
将数据自动聚类成几个类别，聚在一起的相似度大，不在一起的差异性大  
3. 预测  
通过当前和历史数据来预测未来趋势  
4. 关联
发现数据中的关联规则，它被广泛应用在购物篮分析或事务数据分析中  

数据挖掘的一般步骤：  
输入数据->数据预处理->数据挖掘->后处理->信息  
数据预处理（特征选择、维规约、规范化、选择数据子集）  
1. 数据清洗：去除重复数据，去噪声（干扰数据），填充缺失值  
2. 数据集成：多个数据源的数据存放在一个统一的数据存储中  
3. 数据变换：将数据转化适合数据挖掘的形式  
后处理（模式过滤、可视化模式表示）
