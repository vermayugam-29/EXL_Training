import pandas as pd
import plotly.express as px

df = pd.read_csv('sales_data.csv')

df['Date'] = pd.to_datetime(df['Date'])


#1. Line Chart: Revenue Over Time
df = df.sort_values('Date')
fig_line = px.line(
    df,
    x = 'Date',
    y = 'Sales',
    title = 'Revenue over Time',
    color = 'Region'
)
fig_line.show()

#2. Bar Chart: Region-wise Revenue Comparison
region_revenue = df.groupby('Region')['Sales'].sum().reset_index()
region_revenue = region_revenue.sort_values(by = 'Sales', ascending=False)

fig_bar = px.bar(
    region_revenue,
    x = 'Region',
    y = 'Sales',
    title = 'Region-wise Revenue Comparison',
    color = 'Sales'
)
fig_bar.show()


#3. Pie Chart: Product-wise Revenue Share
product_revenue = df.groupby('Product')['Sales'].sum().reset_index()
fig_pie = px.pie(
    product_revenue,
    names='Product',
    values='Sales',
    title='Product-wise Revenue Share',
    hover_data=['Sales']
)
fig_pie.show()

#4. Scatter Plot: Units Sold vs Revenue
fig_scatter = px.scatter(
    df,
    x = 'Quantity',
    y = 'Sales',
    color = 'Region',
    hover_data=['Product', 'Region'],
    title='Units Sold vs Total Revenue',
)
fig_scatter.show()