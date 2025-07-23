import pandas as pd
import seaborn as sns
import plotly.express as px


#Load csv file
csv_file = pd.read_csv('ecommerce_sales.csv')


#Bar chart for total sales by region
region_sales = csv_file.groupby('Region')['Sales'].sum().reset_index()

fig_bar = px.bar(
    region_sales,
    x = 'Region',
    y='Sales',
    title='Total Sales by Region',
)
fig_bar.show()

#Pie Chart : Total Sales by Category
category_sales = csv_file.groupby('Category')['Sales'].sum().reset_index()

fig_pie = px.pie(
    category_sales,
    names='Category',
    values='Sales',
    title='Pie Chart : Total Sales by Category',
)
fig_pie.show()

#Line Chart : Sales Trend Over Time
daily_sales = csv_file.groupby('Date')['Sales'].sum().reset_index()

fig_line = px.line(
    daily_sales,
    x = 'Date',
    y = 'Sales',
    title='Line Chart : Sales Trend Over Time',
)
fig_line.show()

#Scatter Plot: Quantity vs Sales

fig_scatter = px.scatter(
    csv_file,
    x = 'Quantity',
    y = 'Sales',
    # color='Category',
    title='Scatter Plot: Quantity vs Sales',
)
fig_scatter.show()