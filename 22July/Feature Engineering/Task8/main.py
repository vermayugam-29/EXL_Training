import pandas as pd

df = pd.read_csv('data.csv')

df['TotalInterest'] = ( df['LoanAmount'] * df['InterestRate'] * df['LoanTerm_Years'] ) / 100

print(df)