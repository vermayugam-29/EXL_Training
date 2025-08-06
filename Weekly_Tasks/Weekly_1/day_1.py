import pandas as pd

def data_loading(df):
    print('First 10 rows of dataset \n',df.head(10))

    print(df.info())
    print(df.describe())

    print('Unique Value Counts \n')
    print(df['Region'].value_counts(dropna=False))
    print(df['Gender'].value_counts(dropna=False))
    print(df['MembershipLevel'].value_counts(dropna=False))

    df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'])

    return df