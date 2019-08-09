import matplotlib.pyplot as plt
import seaborn as sns

#数据准备
#tips记录了不同顾客在餐厅的消费账单及小费情况。
tips=sns.load_dataset("tips")
print(tips.head(10))

#散点图
sns.jointplot(x="total_bill",y="tip",data=tips,kind='scatter')
#核密度图
sns.jointplot(x="total_bill",y="tip",data=tips,kind='kde')
#Hexbin图（直方图的二维模拟）
sns.jointplot(x="total_bill",y="tip",data=tips,kind='hex')
plt.show()