import pandas as pd
from sklearn.model_selection import KFold
df = pd.read_csv('After_Feature_Sel.csv')
X = df.values
kf = KFold(n_splits=10, shuffle=True, random_state=42)