import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv('customer_data.csv')

#converting to dateandtime
df['signup_date'] = pd.to_datetime(df['signup_date'])

#Signup month and signup weekday
df['signup_month'] = df['signup_date'].dt.month_name()
df['signup_day'] = df['signup_date'].dt.weekday

#gender col to 0, 1, 2 format
df['gender'] = df['gender'].apply(
    lambda x : 0 if x.lower() == 'male' else 1 if x.lower() == 'female' else 2
)

#creating binary feature
df['is_returning_customer'] = df['num_previous_orders'].apply(
    lambda x : 1 if x > 0 else 0
)

#binning the total spend
df['bin'] = df['total_spent'].apply(
    lambda x : 'Low' if x < 100 else 'Medium' if x < 300 else 'High'
)

#one-hot encode country
df_dummies = pd.get_dummies(df['country'], prefix='country')
df = pd.concat([df, df_dummies], axis=1)

print(df)

#Additional Task to try
# What other features could you create from the existing ones?
# Would normalization/scaling help for any feature?
# How would you handle missing values if any were present?

#Features
#give old customer discount like if days > 1000
#we can analyse order_cnt and total_spend and give the customer some perks if he
# spends a good amount per order or give him some pts which will help him in buying
# products from that pts/coins