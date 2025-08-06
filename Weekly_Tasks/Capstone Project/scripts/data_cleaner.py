def clean_data(df):
    #--------------------handling missing values---------------------------

    #using mode
    df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
    df['HasCrCard'] = df['HasCrCard'].fillna(df['HasCrCard'].mode()[0])
    df['IsActiveMember'] = df['IsActiveMember'].fillna(df['IsActiveMember'].mode()[0])
    df['Churn'] = df['Churn'].fillna(df['Churn'].mode()[0])

    #using mean
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df['EstimatedSalary'] = df['EstimatedSalary'].fillna(df['EstimatedSalary'].mean())

    #using median
    df['Tenure'] = df['Tenure'].fillna(df['Tenure'].median())
    df['Balance'] = df['Balance'].fillna(df['Balance'].median())
    df['NumOfProducts'] = df['NumOfProducts'].fillna(df['NumOfProducts'].median())


    #handling edge cases
    df = df[df['Age'] > 0]
    df = df[df['EstimatedSalary'] >= 0]

    #--------------------------outlier handling----------------------------
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df[col] = df[col].apply(lambda x: lower if x < lower else upper if x > upper else x)

    return df