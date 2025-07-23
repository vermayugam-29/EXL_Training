import pandas as pd
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt

def handle_outliers(df):

    #taking the numerical cols
    numeric_cols = ['AnnualIncome', 'AvgTransactionValue', 'LoginFrequency']

    #Appling zscore
    z_score = df[numeric_cols].apply(zscore)

    threshold = 3
    outliers_zcore = (z_score.abs() > threshold)
    # print(outliers_zcore.sum())

    data_outliers_zscore = df[outliers_zcore.any(axis=1)]

    print('Outliers in data frame : \n', data_outliers_zscore)

    #Applying IQR

    iqr_bounds = {}
    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        iqr_bounds[col] = (lower_bound, upper_bound)

        print(f'{col}: {lower_bound:.2f} - {upper_bound:.2f}')


    capping_data = df.copy()

    for col in numeric_cols:
        lower_bound, upper_bound = iqr_bounds[col]
        capping_data[col] = capping_data[col].apply(
            lambda x : lower_bound if x < lower_bound else upper_bound if x > upper_bound else x
        )


    #Before Outlier
    plt.figure(figsize = (10,10))
    for col in numeric_cols:
        plot(df, f'{col} - Before', col)

    #After Outlier
    for col in numeric_cols:
        plot(capping_data, f'{col} - After', col)

    capping_data.to_csv("customer_outliers_handled.csv", index=False)

def plot(data, title, col):
    sns.boxplot(
        data,
        y = col
    )
    plt.title(title)
    plt.tight_layout()
    plt.show()
