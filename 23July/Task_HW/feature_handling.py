import pandas as pd
pd.set_option('display.max_columns', None)

def handle_feature(df):

    #creating new feature
    df['TotalSpend'] = df['TotalTransactions'] * df['AvgTransactionValue']


    #creating age groups
    df['AgeGroup'] = df['Age'].apply(
        lambda x :'Child' if x < 18 else
        'Young' if x < 25 else 'Young Adults'
        if x < 36 else 'Mid-Age Adults' if x < 46 else 'Old'
    )

    #converting isChurned
    df['IsChurned'] = df['IsChurned'].apply(
        lambda x : 1 if x.lower() == 'yes' else 0
    )

    #average transaction frequency per month
    df['MonthlyTransactionRate'] = df['TotalTransactions'] / (df['LoginFrequency'] / 4)

    #Derive a new score
    df['CustomerScore'] = (df['TotalSpend'] * df['SatisfactionScore']) / df['CartAbandonRate']

    df.to_csv('customer_features_enriched.csv', index=False)