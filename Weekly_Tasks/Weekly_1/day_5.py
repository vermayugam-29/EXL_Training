import pandas as pd
from sklearn.preprocessing import LabelEncoder
pd.set_option('display.max_columns', None)

def handle_features(df):
    # Convert LastPurchaseDate to datetime
    df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'], errors='coerce')

    # Step 1: Revenue per Purchase
    df['RevenuePerPurchase'] = df['TotalRevenue'] / df['Purchases']

    # Step 2: Customer Tenure in Months (Fixed)

    df['CustomerTenureMonths'] = (
            (pd.to_datetime('today').normalize() - df['LastPurchaseDate'])
            / pd.Timedelta(days=30)
    ).fillna(0).astype(int)

    #Step3. Categorize customers based on income brackets.
    df['IncomeCategory'] = df['AnnualIncome'].apply(
        lambda x : 'Low' if x < 900000 else 'Medium' if x < 4000000 else 'High'
    )

    # Step 4: Label Encode MembershipLevel
    le_encode = LabelEncoder()
    df['MembershipLevel'] = le_encode.fit_transform(df['MembershipLevel'])

    print(df)

    df.to_csv('modified_data.csv', index=False)

    return df
