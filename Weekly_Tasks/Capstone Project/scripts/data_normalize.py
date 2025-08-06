from sklearn.preprocessing import MinMaxScaler


def normalize_data(df):
    scaler = MinMaxScaler()

    numeric_cols = ['Age', 'Tenure', 'Balance', 'EstimatedSalary']
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    df.to_csv('data/processed/cleaned_data.csv', index=False)

    return df, scaler