import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
tips.head()

sns.set_context("notebook")
sns.countplot(x="sex", data=tips)
sns.despine()
plt.show()

sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", palette="seismic")
plt.show()
