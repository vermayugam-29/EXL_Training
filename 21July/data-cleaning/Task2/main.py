import pandas as pd

df = pd.read_csv('data.csv')

#Show rows where MembershipLevel is null.
missing_memberships = df['MembershipLevel'].isnull()
print(missing_memberships)

# Drop them
# print(df)
df.dropna(subset = ['MembershipLevel'], inplace=True)
print(df)