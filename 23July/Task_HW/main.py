import pandas as pd
from missing_value_handling import handle_missing
from outlier_handling import handle_outliers
from data_normalisation_handling import handle_normalisation
from feature_handling import handle_feature

#Reading csv
df = pd.read_csv('customer_insights_raw.csv')


#calling functions
handle_missing(df.copy())
handle_outliers(df.copy())
handle_normalisation(df.copy())
handle_feature(df.copy())