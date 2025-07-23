import pandas as pd
from scipy.stats import zscore

df = pd.read_csv('Outlier_Handling_Input.csv')


#Outlier detection using zscore
numerical_cols = ['AnnualIncome', 'SpendingScore']
z_score = df[numerical_cols].apply(zscore)

threshold = 3
outliers = (z_score.abs() > threshold)
print('Outlier detected\n', df[outliers.any(axis=1)])

clean_df = df[(z_score.abs() < threshold).all(axis=1)]
print(clean_df)

#Outlier detection using IQR
# Q1 = df['PurchaseCount'].quantile(0.25)
# Q3 = df['PurchaseCount'].quantile(0.75)


# IQR = Q3 - Q1

# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR


# outlier_iqr = df[
#     (df['PurchaseCount'] < lower_bound) |
#     (df['PurchaseCount'] > upper_bound)
# ]

# remove_outlier = df[
#     (df['PurchaseCount'] >= lower_bound) &
#     (df['PurchaseCount'] <= upper_bound)
# ]

# print("Outliers using IQR Method:\n", outlier_iqr)
# print("Outliers removed using IQR Method:\n", remove_outlier)