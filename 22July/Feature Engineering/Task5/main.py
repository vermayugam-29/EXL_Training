import pandas as pd
from scipy.linalg import sqrtm

df = pd.read_csv('data.csv')

df['BMI'] = df['Weight_KG'] / (df['Height_M'] * df['Height_M'])

df['Category'] = df['BMI'].apply(
    lambda x : 'Underweight' if x < 18.5 else 'Normal' if x < 24.9 else 'Overweight' if x < 29.9 else 'Obese'
)

print(df)