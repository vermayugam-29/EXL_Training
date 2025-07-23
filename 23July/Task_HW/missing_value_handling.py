import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)


def handle_missing(df):

    #generating summary of data
    print('Summary of csv data \n', df.info())

    #Finding missing columns
    missing_cols = df.columns[df.isnull().any()]


    #dividing missing columns into numeric ones and category ones
    numeric_col = df[missing_cols].select_dtypes(include=['int64', 'float64']).columns.tolist()
    category_col = df[missing_cols].select_dtypes(include=['object']).columns.tolist()


    #Median and mean dataset for cols
    df_mean = df.copy()
    df_median = df.copy()

    #filling mean values to numeric cols
    for col in numeric_col:
        df_mean[col].fillna(df_mean[col].mean(), inplace=True)

    #filling median values to numeric cols
    for col in numeric_col:
        df_median[col].fillna(df[col].median(), inplace=True)

    #filling mode values to category cols
    for col in category_col:
        df_mean[col].fillna(df[col].mode()[0], inplace=True)
        df_median[col].fillna(df[col].mode()[0], inplace=True)

    #Comparing mean and median imputations in missing fields
    print('\nMean imputed dataset \n', df_mean.describe())
    print('\nMedian imputed dataset \n', df_median.describe())


    #dropping rows where more than 2 values are missing in the row
    df_drop_rows = df_median[df.isnull().sum(axis = 1) <= 2]

    #making new csv with cleaned data
    df_drop_rows.to_csv('customer_cleaned_imputed.csv', index=False)

    #ploting heatmap
    plot('Before filling missing places', df)
    plot('After filling missing places', df_drop_rows)

#using functions so that we can reuse it
def plot(title, data):
    plt.figure(figsize = (10,6))
    sns.heatmap(
        data.isnull(),
        cbar = False,
        cmap = 'viridis'
    )
    plt.title(title)
    plt.show()