import pandas as pd

def features(df):
    df['Gender'] = df['Gender'].apply(
        lambda x : x.lower()
    )
    #one hot encoding for categorical fields
    df = pd.get_dummies(df, columns = ['Gender'], prefix = 'Gender', dtype = int)

    return df