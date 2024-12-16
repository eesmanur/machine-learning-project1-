import pandas as pd
from prettytable import PrettyTable

df = pd.read_csv("ObesityDataSet.csv")

data_types = df.dtypes

categorical_columns = data_types[data_types == 'object'].index

table = PrettyTable()
table.field_names = ["Sütun", "Veri Tipi"]

for column in categorical_columns:
    table.add_row([column, data_types[column]])

print(table)
