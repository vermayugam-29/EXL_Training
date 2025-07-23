import pandas as pd

df = pd.read_csv('data.csv')

df['LoginTime'] = pd.to_datetime(df['LoginTime'])

df['Hour'] = df['LoginTime'].dt.hour

df['TimeOfDay'] = df['Hour'].apply(
    lambda x : 'Morning' if x <= 11 else 'Afternoon' if x <= 17 else 'Evening'
)

print(df)