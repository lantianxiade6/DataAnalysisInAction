import matplotlib.pyplot as plt
import seaborn as sns

car=sns.load_dataset('car_crashes')
print(car.head(10))

sns.pairplot(car)#成对关系
plt.show()

#二元变量分布
sns.jointplot(x='total',y='speeding',data=car,kind='scatter')
sns.jointplot(x='total',y='speeding',data=car,kind='kde')
sns.jointplot(x='total',y='speeding',data=car,kind='hex')
plt.show()