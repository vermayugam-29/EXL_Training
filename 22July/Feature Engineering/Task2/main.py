import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('data.csv')

df['AgeGroup'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult' if x <= 50 else 'Senior')

avg_income = df.groupby('AgeGroup')['AnnualIncome'].mean().reset_index().rename(columns={'AnnualIncome': 'AvgIncomeByAgeGroup'})
df = df.merge(avg_income, on='AgeGroup', how='left')


print(df)