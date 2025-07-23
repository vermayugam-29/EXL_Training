import pandas as pd

df = pd.read_csv('data.csv')

df['Words'] = df['ReviewText'].apply(
    lambda x : len(x.strip().split(" "))
)

words = ['good', 'loved', 'excellent', 'friendly']

df['isPositive'] = df['ReviewText'].apply(
    lambda x : any(word in x.lower() for word in words)
)

print(df)