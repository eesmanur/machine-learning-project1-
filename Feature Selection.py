import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Before_Feature_Sel.csv")

target_column = ['NObeyesdad_Obesity_Type_I']

X = data.drop(target_column, axis=1)
y = data[target_column]

correlation_matrix = X.corr().abs()

plt.figure(figsize=(10, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Özellik Korelasyon Matrisi")
plt.show()

low_correlation_threshold = 0.01
low_correlated_features = {}

for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if -low_correlation_threshold < correlation_matrix.iloc[i, j] < low_correlation_threshold:
            colname = correlation_matrix.columns[i]
            low_correlated_features[colname] = correlation_matrix.iloc[i, j]

print('Düşük korelasyona sahip özellikler ve korelasyon değerleri:')
for feature, corr_value in low_correlated_features.items():
    print(f"{feature}: {corr_value}")

X_selected = X.drop(low_correlated_features.keys(), axis=1)

X_selected[target_column] = y

X_selected.to_csv('After_Feature_Sel.csv', index=False)

print("Düşük Korelasyona Sahip Özelliklerin Çıkarıldığı Özellikler:")
print(X_selected.columns)
