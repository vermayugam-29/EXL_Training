import pandas as pd

# Step 1: Create a sample DataFrame
data = {
    'CustomerID': [101, 102, 103],
    'PurchaseDate': ['2023-05-01', '2023-05-03', '2023-05-05'],
    'Quantity': [500, 1000, 800],
    'PricePerUnit': [3, 2, 4],
    'ProductCategory': ['Electronics', 'Furniture', 'Outfit']
}

df = pd.DataFrame(data)

# Step 2: Convert 'PurchaseDate' to datetime format
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

# Step 3: Feature 1 - TotalSales = Quantity * PricePerUnit
df['TotalSales'] = df['Quantity'] * df['PricePerUnit']

# Step 4: Feature 2 - Extract Weekday (0 = Monday, 6 = Sunday)
df['WeekDay'] = df['PurchaseDate'].dt.weekday

# Step 5: Feature 3 - Flag High-Value Purchase (>1500)
df['IsHighValue'] = df['TotalSales'] > 1500

# Step 6: Feature 4 - Combine ProductCategory and WeekDay
df['Category_Weekday'] = df['ProductCategory'] + "_" + df['WeekDay'].astype(str)

# Final Output
print("\nNew FEATURE Engineered Data:\n", df)
