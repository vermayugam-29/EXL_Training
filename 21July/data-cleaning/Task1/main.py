import pandas as pd

df = pd.read_csv('data.csv')

#Count how many entries are missing.
cnt = df['Age'''].isnull().sum()
print(cnt)

#Impute missing ages using the mean.
print(df)
print()
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)