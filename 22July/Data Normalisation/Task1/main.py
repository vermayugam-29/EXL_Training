import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('retail_sales.csv')

numeric_cols = ['UnitsSold','UnitPrice','TotalRevenue']

scaler = MinMaxScaler()
df_minmax = pd.DataFrame(
    scaler.fit_transform(df[numeric_cols]),
    columns=[f"{col}_MinMax" for col in numeric_cols]
)

standard = StandardScaler()
df_standard = pd.DataFrame(
    standard.fit_transform(df[numeric_cols]),
    columns = [f'{col}_Z-Score' for col in numeric_cols]
)

df_res = pd.concat([df, df_minmax, df_standard], axis=1)

print(df_res.head())