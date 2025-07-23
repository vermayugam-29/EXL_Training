import pandas as pd

df = pd.read_csv('data.csv')

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'])

df['DeliveryDays'] = (df['DeliveryDate'] - df['OrderDate']).dt.days

df['isDelayed'] = df['DeliveryDays'] > 4

print(df)