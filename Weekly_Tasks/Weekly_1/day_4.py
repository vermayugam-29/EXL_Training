import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def handle_normalisation(df):
    #Step1. Normalize AnnualIncome and TotalRevenue
    features = ['AnnualIncome', 'TotalRevenue']
    minmax_scaler = MinMaxScaler()
    df_minmax = pd.DataFrame(
        minmax_scaler.fit_transform(df[features]),
        columns = [f'{col}_MinMax' for col in features],
        index=df.index
    )

    zscore_standard = StandardScaler()
    df_zscore = pd.DataFrame(
        zscore_standard.fit_transform(df[features]),
        columns = [f'{col}_ZScore' for col in features],
        index=df.index
    )

    #Stwp2 : Storing scaled versions as new columns
    df = pd.concat([df, df_minmax, df_zscore], axis=1)

    #Step3 : plotting histplot
    # AnnualIncome - Original
    plot(df, 'AnnualIncome', 'Original AnnualIncome', 'AnnualIncome', 'blue')
    plot(df, 'AnnualIncome_MinMax', 'Min-Max Scaled AnnualIncome', 'Scaled AnnualIncome', 'green')
    plot(df, 'AnnualIncome_ZScore', 'Z-Score Scaled AnnualIncome', 'Standardized AnnualIncome', 'red')
    plot(df, 'TotalRevenue', 'Original TotalRevenue', 'TotalRevenue', 'blue')
    plot(df, 'TotalRevenue_MinMax', 'Min-Max Scaled TotalRevenue', 'Scaled TotalRevenue', 'green')
    plot(df, 'TotalRevenue_ZScore', 'Z-Score Scaled TotalRevenue', 'Standardized TotalRevenue', 'red')

    return df


def plot(data, col, title, x_label, color):
    plt.figure(figsize=(10, 8))
    sns.histplot(
        data[col],
        bins=10,
        kde=True,
        color=color,
        edgecolor='black'
    )
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()