import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("Min_Before_Norm.csv")

categorical_cols = [col for col in df.columns if df[col].dtype.name == "object"]
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

scaler = MinMaxScaler()

df_norm = scaler.fit_transform(df[numeric_cols])
df.loc[:, numeric_cols] = df_norm

df.to_csv("Normalization.csv", index=False)