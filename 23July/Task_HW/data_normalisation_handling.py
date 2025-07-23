import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

pd.set_option('display.max_columns', None)

def handle_normalisation(df):

    #Selecting the columns for normalisation
    cols = ['AnnualIncome', 'AvgTransactionValue', 'LoginFrequency']


    #Min-Max scaling
    minmax_scaler = MinMaxScaler()
    df_minmax = pd.DataFrame(
        minmax_scaler.fit_transform(df[cols]),
        columns = [f'{col}_MinMax' for col in cols]
    )

    #Z-Score standardisation
    zscore_standardisation = StandardScaler()
    df_zscore = pd.DataFrame(
        zscore_standardisation.fit_transform(df[cols]),
        columns=[f'{col}_zscore' for col in cols]
    )

    #making them into data set to push further to csv files
    df_minmax = pd.concat([df, df_minmax], axis=1)
    df_zscore = pd.concat([df, df_zscore], axis=1)

    #plotting histogram
    plt.figure(figsize = (10,10))
    for col in cols:
        plot(df, col, f'Original - {col}', 'skyblue')
        plot(df_minmax, f'{col}_MinMax', f'Min Max - {col}', 'green')
        plot(df_zscore, f'{col}_zscore', f'Z-Score - {col}', 'orange')


    #Making a new csv with the data frames
    df_minmax.to_csv('customer_minmax_scaled.csv', index = False)
    df_zscore.to_csv('customer_standard_scaled.csv', index = False)

def plot(df, col, title, clr):
    plt.hist(
        df[col],
        bins = 10,
        color = clr
    )
    plt.title(title)
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()