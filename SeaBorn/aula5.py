import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

sns.lmplot(
    x="total_bill",
    y="tip",
    data=tips,
    hue="sex",
    markers=["o", "v"],
    
)
plt.show()
