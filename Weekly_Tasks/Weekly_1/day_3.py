import matplotlib.pyplot as plt
from scipy.stats import zscore

def handle_outliers(df):
    #Z-Score
    z_score = df[['TotalRevenue']].apply(zscore)

    threshold = 3
    outliers = (z_score.abs() > threshold).any(axis=1)
    print('Outliers found using z-score \n', df[outliers])

    #IQR
    q1 = df['TotalRevenue'].quantile(0.25)
    q3 = df['TotalRevenue'].quantile(0.75)
    iqr = q3 - q1

    upper_bound = q3 + 1.5 * iqr
    lower_bound = q1 - 1.5 * iqr

    outliers_iqr = df[
        (df['TotalRevenue'] < lower_bound) | (df['TotalRevenue'] > upper_bound)
    ]
    print('Outliers IQR = ', outliers_iqr)

    #Before capping/floring
    plot(df, 'Before Outlier')

    #Step2 : cap/floor the outliers.
    df['TotalRevenue'] = df['TotalRevenue'].apply(
        lambda x : lower_bound if x < lower_bound else upper_bound if x > upper_bound else x
    )

    #Step3 : Show comparison using boxplot before and after.
    plot(df, 'After Outlier')
    # print(df.isnull().sum())
    return df

def plot(data, title):
    plt.figure(figsize=(6,4))
    plt.boxplot(
        data['TotalRevenue']
    )
    plt.title(title)
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    plt.show()