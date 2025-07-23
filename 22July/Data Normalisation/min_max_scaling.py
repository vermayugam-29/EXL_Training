import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('income_data.csv')

print(df)

features = ['Age', 'AnnualIncome']

minmax_scaler = MinMaxScaler()
df_minmax_scaler = pd.DataFrame(
    minmax_scaler.fit_transform(df[features]),
    columns=[f"{col}_MinMax" for col in features]
)

standard_scaler = StandardScaler()
df_standard = pd.DataFrame(
    standard_scaler.fit_transform(df[features]),
    columns=[f"{col}_zscore" for col in features]
)


df_res = pd.concat([df, df_minmax_scaler, df_standard], axis=1)

print(df_minmax_scaler)