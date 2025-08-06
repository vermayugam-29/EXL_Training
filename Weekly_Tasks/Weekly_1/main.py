import pandas as pd
from day_1 import data_loading
from day_2 import handle_missing
from day_3 import handle_outliers
from day_4 import handle_normalisation
from day_5 import handle_features
from day_6 import handle_visualization

df = pd.read_csv('data.csv')
df = data_loading(df)
df = handle_missing(df)
df = handle_outliers(df)
df = handle_normalisation(df)
df = handle_features(df)
handle_visualization(df)