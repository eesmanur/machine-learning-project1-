import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('After_Feature_Sel.csv')
sampled_df = df.sample(frac=0.50, random_state=42)

train_df, test_df = train_test_split(sampled_df, test_size=0.25, random_state=42)

train_df.to_csv('train_set.csv', index=False)
test_df.to_csv('test_set.csv', index=False)

print("Veri başarıyla örneklendi, ayrıldı ve kaydedildi.")


