import pandas as pd

df = pd.read_csv('data.csv')

#CustomerSatisfaction has missing values. Fill them using the most frequent response.
print(df)
print()
df['Category'] = df['Category'].fillna(df['Category'].mode()[1])
print(df)