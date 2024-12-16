
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

employee_dataset = pd.read_csv("ObesityDataSet.csv")
sns.set_palette('PuBu')
employee_dataset['NObeyesdad'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()

