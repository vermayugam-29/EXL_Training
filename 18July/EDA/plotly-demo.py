import plotly.express as px
import pandas as pd
import seaborn as sns

#loading tips
tips = sns.load_dataset('tips')
# print(tips.head())


#---------------scatter plot-----------------
fig_scatter = px.scatter(
    tips,
    x = 'total_bill',
    y = 'tip',
    color = 'sex',
    title = 'Scatter Plot : Total Bill vs Tip',
)
fig_scatter.show()


# Bar Graph
avg_tip = tips.groupby('day')['tip'].mean().reset_index()
fig_bar = px.bar(
    avg_tip,
    x = 'day',
    y = 'tip',
    title='Bar Chart: Average Tip per Day',
    text_auto=True,
)
fig_bar.show()

#Pie Chart (Used for percentage show)
gender_tip = tips.groupby('sex', observed = False)['tip'].sum().reset_index()
fig_pie = px.pie(
    gender_tip,
    names = 'sex',
    values = 'tip',
    title = 'Pie Chart : Tip Distribution by Gender',
    color_discrete_sequence = ['skyblue','green'],
)
fig_pie.show()

#Line Graph
tips['cumulative_tip'] = tips['tip'].cumsum()
tips['index'] = tips.index
fig_line = px.line(
    tips,
    x='index',
    y='cumulative_tip',
    title='Line Chart : Cumulative Tip Over the time',
)
fig_line.show()


#Histograph
fig_hist = px.histogram(
    tips,
    x = 'total_bill',
    nbins = 10,
    title = 'Histogram of Total Bill',
    color_discrete_sequence = ['green'],
)
fig_hist.show()

#box plot
fig_box = px.box(
    tips,
    x = 'sex',
    y = 'tip',
    title= 'Box Plot: Tip Distribution by Gender',
    color='sex'
)
fig_box.show()