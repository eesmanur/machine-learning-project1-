import pandas as pd

df = pd.read_csv("ObesityDataSet.csv")

categorical_cols = df.select_dtypes(include=['object', 'category']).columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

Q1 = df[numeric_cols].quantile(0.25)
Q3 = df[numeric_cols].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

for col in numeric_cols:
    min_val = df[col].min()
    max_val = df[col].max()
    lower_limit = lower_bound[col]
    upper_limit = upper_bound[col]


    df.loc[df[col] < lower_limit, col] = lower_limit

    df.loc[df[col] > upper_limit, col] = upper_limit

upper_limit_ncp = 3.50

df.loc[df['NCP'] > upper_limit_ncp, 'NCP'] = upper_limit_ncp
df.to_csv('Outlier_Detection.csv', index=False)











