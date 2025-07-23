import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('data.csv')

df['TotalSales'] = df['UnitsSold'] * df['UnitPrice']

df['SalesCategory'] = df['TotalSales'].apply(lambda x: 'High' if x > 40000 else 'Low')

print(df)