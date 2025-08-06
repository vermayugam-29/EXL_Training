import pandas as pd

def handle_missing(df):

    #Step1 : Columns with missing values
    missing_before = df.isnull().sum()
    print('Missing Value Columns \n',missing_before)

    #Step2 : Drop rows where Age is missing.
    df = df.dropna(subset=['Age'])

    #Step3 : Fill missing AnnualIncome by group median based on MembershipLevel
    df['AnnualIncome'] = df.groupby('MembershipLevel')['AnnualIncome'].transform(
        lambda x: x.fillna(x.median())
    )

    #Step4 : Fill missing gender with mode
    df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])

    #Step5 : Create a summary DataFrame showing before vs after missing values.
    summary_df = pd.DataFrame({
        'Missing_Before': missing_before,
        'Missing_After' : df.isnull().sum()
    })

    print("\nSummary of Missing Values (Before vs After):")
    print(summary_df)
    print(df.isnull().sum())
    return df
