import pandas as pd

df = pd.read_csv('data.csv')

# dummies = pd.get_dummies(df['FuelType'], prefix = 'Is')
#
# df = pd.concat([df, dummies], axis = 1)

df['isPetrol'] = df['FuelType'] == 'Petrol'
df['isDiesel'] = df['FuelType'] == 'Diesel'
df['isElectric'] = df['FuelType'] == 'Electric'
df['isHybrid'] = df['FuelType'] == 'Hybrid'

print(df)