import matplotlib.pyplot as plt
import seaborn as sns

#数据准备
iris=sns.load_dataset('iris')
print(iris.head(10))
sns.pairplot(iris)
plt.show()