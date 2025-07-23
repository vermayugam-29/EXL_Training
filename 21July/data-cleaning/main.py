import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Read csv
data = pd.read_csv('data_cleaning_customer_data.csv')

#Original File
# print('Original Data')
# print(data.head())
# #
# # #Check Missing values
# print('Missing Values')
# print(data.isnull().sum())
# #
# # #Impute Missing values in Age
# data['Age'] = data['Age'].fillna(data['Age'].median())
# # print(data.head(31))
#
#
# # #Impute Missing values in Annual Income
# data['AnnualIncome'] = data['AnnualIncome'].fillna(data['AnnualIncome'].median())
#
# #Drop rows where membership level is missing
# data.dropna(subset=['MembershipLevel', 'CustomerSatisfaction'], inplace=True)
#
# #update to csv
# # data.to_csv('data_cleaning_customer_data.csv', index=False)
#
#
# # Remove Outliers in Annual income
# data = data[data['AnnualIncome'] > 25000]
# print(data.describe())

# data_dropped = data.dropna()
#
# #Visualize Missing values using heatmap
# plt.figure(figsize=(10,10))
# sns.heatmap(data.isnull(), cbar = False, yticklabels=False, cmap = 'viridis')
# plt.title('Missing Data heatmap')
# plt.tight_layout()
# plt.show()

# print('Original Data', data.shape)
# print('After dropping missing fields', data_dropped.shape)

# print(data)

# # Impute Age with mean
# data['Age'] = data['Age'].fillna(data['Age'].mean())
#
# # Impute Annual Income with median
# data['AnnualIncome'] = data['AnnualIncome'].fillna(data['AnnualIncome'].median())
#
# # Impute Customer Satisfaction with mode (use [0] to get the first mode value)
# data['CustomerSatisfaction'] = data['CustomerSatisfaction'].fillna(data['CustomerSatisfaction'].mode()[0])
# modes = data['CustomerSatisfaction'].mode()
# print(data['CustomerSatisfaction'].value_counts())
# print(modes)


print(data.head(10))
data['CustomerSatisfaction'] = data['CustomerSatisfaction'].fillna(method = 'bfill')
print(data.head(10))
