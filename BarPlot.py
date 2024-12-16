import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dp= pd.read_csv("ObesityDataSet.csv")
data = dp['NObeyesdad']
sns.set_palette('PuBu')
plt.figure(figsize=(10,5))
sns.countplot(x=data , data=dp)
plt.show()
