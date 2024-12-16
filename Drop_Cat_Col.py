import pandas as pd
data = pd.read_csv("Normalization.csv")

categorical_columns = data.select_dtypes(include='object').columns

data.drop(categorical_columns, axis=1, inplace=True)
data.drop("Unnamed: 0", axis=1, inplace=True)
data.to_csv('Before_Feature_Sel.csv', index=False)