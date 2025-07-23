import pandas as pd
import plotly.express as px
from scipy.stats import zscore

df = pd.read_csv('z_score_outlier.csv')

#Detect outliers in the Price column using Z-score.
numerical_cols = ['Price']
z_score = df[numerical_cols].apply(zscore)

threshold = 3
outliers = (z_score.abs() > threshold).any(axis = 1)
print('Outliers: \n', df[outliers])

filtered_df = df[(z_score.abs() < threshold).any(axis=1)]
print('Dataset after removing Outliers: \n', filtered_df)

print('Shape before cleaning', df.shape)
print('Shape after cleaning', filtered_df.shape)


fig_before = px.box(
    df,
    y='Price',
    title='Before Outlier Removal'
)
fig_after = px.box(
    filtered_df,
    y='Price',
    title='After Outlier Removal'
)

fig_before.show()
fig_after.show()