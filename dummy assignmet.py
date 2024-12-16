import pandas as pd
df = pd.read_csv('Outlier_Detection.csv')

df['G_Male'] = df['Gender'].apply(lambda x: 1 if x == 'Male' else 0)
df['G_Female'] = df['Gender'].apply(lambda x: 1 if x == 'Female' else 0)

df['FHWO_Yes'] = df['family_history_with_overweight'].apply(lambda x: 1 if x == 'yes' else 0)
df['FHWO_No'] = df['family_history_with_overweight'].apply(lambda x: 1 if x == 'no' else 0)

df['FAVC_Yes'] = df['FAVC'].apply(lambda x: 1 if x == 'yes' else 0)
df['FAVC_No'] = df['FAVC'].apply(lambda x: 1 if x == 'no' else 0)

df['CAEC_Sometimes'] = df['CAEC'].apply(lambda x: 1 if x == 'Sometimes' else 0)
df['CAEC_Frequently'] = df['CAEC'].apply(lambda x: 1 if x == 'Frequently' else 0)
df['CAEC_Always'] = df['CAEC'].apply(lambda x: 1 if x == 'Always' else 0)
df['CAEC_No'] = df['CAEC'].apply(lambda x: 1 if x == 'no' else 0)

df['SMOKE_Yes'] = df['SMOKE'].apply(lambda x: 1 if x == 'yes' else 0)
df['SMOKE_No'] = df['SMOKE'].apply(lambda x: 1 if x == 'no' else 0)

df['SCC_Yes'] = df['SCC'].apply(lambda x: 1 if x == 'yes' else 0)
df['SCC_No'] = df['SCC'].apply(lambda x: 1 if x == 'no' else 0)

df['CALC_Sometimes'] = df['CALC'].apply(lambda x: 1 if x == 'Sometimes' else 0)
df['CALC_Frequently'] = df['CALC'].apply(lambda x: 1 if x == 'Frequently' else 0)
df['CALC_Always'] = df['CALC'].apply(lambda x: 1 if x == 'Always' else 0)
df['CALC_No'] = df['CALC'].apply(lambda x: 1 if x == 'no' else 0)

df['MTRANS_Automobile'] = df['MTRANS'].apply(lambda x: 1 if x == 'Automobile' else 0)
df['MTRANS_Public_Transportation'] = df['MTRANS'].apply(lambda x: 1 if x == 'Public_Transportation' else 0)
df['MTRANS_Walking'] = df['MTRANS'].apply(lambda x: 1 if x == 'Walking' else 0)
df['MTRANS_Motorbike'] = df['MTRANS'].apply(lambda x: 1 if x == 'Motorbike' else 0)
df['MTRANS_Bike'] = df['MTRANS'].apply(lambda x: 1 if x == 'Bike' else 0)

df['NObeyesdad_Insufficient_Weight'] = df['NObeyesdad'].apply(lambda x: 1 if x == 'Insufficient_Weight' else 0)
df['NObeyesdad_Normal_Weight'] = df['NObeyesdad'].apply(lambda x: 1 if x == 'Normal_Weight' else 0)
df['NObeyesdad_Obesity_Type_I'] = df['NObeyesdad'].apply(lambda x: 1 if x == 'Obesity_Type_I' else 0)
df['NObeyesdad_Obesity_Type_II'] = df['NObeyesdad'].apply(lambda x: 1 if x == 'Obesity_Type_II' else 0)
df['NObeyesdad_Obesity_Type_III'] = df['NObeyesdad'].apply(lambda x: 1 if x == 'Obesity_Type_III' else 0)
df['NObeyesdad_Overweight_Level_I'] = df['NObeyesdad'].apply(lambda x: 1 if x == 'Overweight_Level_I' else 0)
df['NObeyesdad_Overweight_Level_II'] = df['NObeyesdad'].apply(lambda x: 1 if x == 'Overweight_Level_II' else 0)

df.to_csv('Dummy_Values.csv', index=False)




