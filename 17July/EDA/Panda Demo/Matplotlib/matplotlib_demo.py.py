# import matplotlib.pyplot as plt

# plt.plot([1,2,3,4,5,6],[20, 20, 90, 90,20, 20])
# plt.title('Test Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()


#-------------------------line graph daily sales----------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# #load csv file
# df = pd.read_csv('sales_data.csv')

# # print(df.describe())

# # print('Sample data',df.head())

# #Converting data type in 'Date' column to datetime
# df['Date'] = pd.to_datetime(df['Date'])

# #Draw line chart - daily total sales
# daily_sales = df.groupby('Date')['Sales'].sum()


# plt.figure(figsize=(10, 10))
# plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-', color='blue')
# plt.title('Daily Total Sales')
# plt.xlabel('Date')
# plt.ylabel('Total Sales')
# plt.show()


#-----------------------bar graph region per sales--------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# #load csv file
# df = pd.read_csv('sales_data.csv')

#Converting data type in 'Date' column to datetime
# df['Date'] = pd.to_datetime(df['Date'])

#bar chart : total sales per region
# region_sales = df.groupby('Region')['Sales'].sum()

# plt.figure(figsize=(10, 6))
# region_sales.plot(kind='bar', title='Total Sales by region' ,color='skyblue')
# # plt.bar(region_sales.index, region_sales.values, color='pink')
# # plt.plot(region_sales.index, region_sales.values, marker='o', linestyle='-', color='blue')
# # plt.title('Total Sales per Region')
# plt.xlabel('Region')
# plt.ylabel('Total Sales')
# plt.show()


#------------------------------------Scatter / dotted data in graph-------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# #load csv file
# df = pd.read_csv('sales_data.csv')
# plt.scatter(df['Quantity'], df['Sales'], color='orange')
# plt.title("Quantity vs Sales")
# plt.xlabel("Quantity")
# plt.ylabel("Sales")
# plt.tight_layout()
# plt.show()



#-----------------------histogram--------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# #load csv file
# df = pd.read_csv('sales_data.csv')

# plt.hist(df['Sales'], bins=10, color='orange', edgecolor='green')
# plt.title('Sales Distribution')
# plt.xlabel('Sales')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()


#-----------------------pie chart : sales per region--------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

#load csv file
df = pd.read_csv('sales_data.csv')

category_sales = df.groupby('Region')['Sales'].sum()
category_sales.plot(kind='pie', startangle=180)
plt.title('Sales Distribution by Region')
plt.tight_layout()
plt.show()

