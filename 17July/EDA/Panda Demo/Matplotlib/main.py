import pandas as pd

try:
    df = pd.read_csv('sales_data.csv')
    print('Sales Data Loaded Successfully')
except FileNotFoundError:
    print('Sales Data Not Found.')
except FileExistsError:
    print('Sales Data not found, please check path or filename')

print('First n entries',df.head(10))

print('(rows, cols)',df.shape)

print('Cols list', list(df.columns))

print('data types',df.dtypes)

print('Number of null records in dataset',df.isnull().sum())

print('Missing values %',(df.isnull().mean() * 100).round(2))

print("Numerical Summary:")
print(df.describe())

print("Categorical Summary:")
print(df.describe(include='object'))

print("No. of Unique Cities:")
print(df['City'].nunique())

print("Unique Cities name:")
print(df['City'].unique())

print('Total quantity sold', df['Quantity'].sum())

print('Top 5 highest priced products:')
print(df[['Product', 'Price']].sort_values(by='Price', ascending=False).drop_duplicates(subset='Price'))