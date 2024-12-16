import pandas as pd

df = pd.read_csv("ObesityDataSet.csv")

for col in df.columns:
    missing_values = df[col].isnull().sum()
    print( f"There are {missing_values} missing values in {col} column")

