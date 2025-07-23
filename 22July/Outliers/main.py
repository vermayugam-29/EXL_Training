import pandas as pd

df = pd.read_csv('cap_floor.csv')

#print the original data
print(df)

#calculate 5th and 95th percentile
lower_cap = df['PurchaseAmount'].quantile(0.05)
upper_cap = df['PurchaseAmount'].quantile(0.95)

print(lower_cap)
print(upper_cap)

df['PurchaseAmount'] = df['PurchaseAmount'].apply(
    lambda x: lower_cap if x < lower_cap else upper_cap if x > upper_cap else x
)

print(df)