import pandas as pd

df = pd.read_csv('data.csv')

#You have a time-ordered record of monthly income. If data is missing in a month, use last known value.
print(df)
df['Location'] = df['Location'].ffill()
print(df)