import pandas as pd

df = pd.read_csv('data.csv')

df['FuelEfficiency'] = df['Distance_KM'] / df['FuelUsed_L']

df['AverageSpeed'] = df['Distance_KM'] / df['Duration_Hours']

print(df)