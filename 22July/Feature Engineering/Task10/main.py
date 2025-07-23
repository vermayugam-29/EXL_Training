import pandas as pd

df = pd.read_csv('data.csv')

df['SpenderType'] = df['MonthlySpend'].apply(
    lambda x : 'Low' if x < 1000 else 'Medium' if x < 2000 else 'High'
)

print(df)