import pandas as pd


pd.set_option('display.max_columns', None)


data = {
    'CustomerID': [101, 102, 103],
    'PurchaseDate': ['2023-05-01', '2023-05-03', '2023-05-05'],
    'Quantity': [3, 2, 4],
    'PricePerUnit': [500, 1000, 800],
    'Category': ['Electronics', 'Furniture', 'Outfit']
}

def revenue(val):
    if val < 2000:
        return 'Low'
    elif val < 5000:
        return 'Medium'
    else:
        return 'High'

df = pd.DataFrame(data)

df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

df['TotalCost'] = df['Quantity'] * df['PricePerUnit']

df['Month'] = df['PurchaseDate'].dt.month_name()

df['isWeekend'] = df['PurchaseDate'].dt.weekday >= 5

df['Cid_Category'] = df['CustomerID'].astype(str) + "-" + df['Category']

df['PremiumBuyer'] = (df['TotalCost'] > 1500) & (df['Quantity']  > 2)


df['RevenueCategory'] = df['TotalCost'].apply(revenue)

df['DaysSincePurchase'] = (pd.Timestamp.today() - df['PurchaseDate']).dt.days


avg_rev = df.groupby('Category')['TotalCost'].mean().reset_index().rename(columns={'TotalCost': 'AverageRevenue'})
df = df.merge(avg_rev, on='Category', how='left')


upper_cap = df['TotalCost'].quantile(0.9)
df['RevenueGreaterThan_90'] = df['TotalCost'] > upper_cap

print(df)