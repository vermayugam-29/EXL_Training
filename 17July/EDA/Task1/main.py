import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('matplotlib_sales_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

#bar chart :- total sales per region
region_sales = df.groupby('Region')['TotalSales'].sum()

region_sales.plot(kind='bar', title='Total Sales per Region', color='green')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

#Pie chart - Sales distribution by Product
product_sales = df.groupby('Product')['TotalSales'].sum()
product_sales.plot(kind='pie', title='Sales Distribution by Product', startangle=90)
plt.tight_layout()
plt.show()

#Line chart - Total Sales Over Time
date_sales = df.groupby('Date')['TotalSales'].sum()
date_sales.plot(kind='line', title='Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Histogram - Distribution of Units Sold
plt.hist(df['Units'], bins=10, color='blue', edgecolor='black')
plt.title('Distribution of Units Sold')
plt.xlabel('Units Sold')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter Plot - Units vs Total Sales
plt.scatter(df['Units'], df['TotalSales'], color='blue')
plt.title('Units vs Total Sales')
plt.xlabel('Units Sold')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()