import plotly.express as px
import seaborn as sns

#loading tips
tips = sns.load_dataset('tips')

#Histogram: Show distribution of total_bill.
fig_histo = px.histogram(
    tips,
    x = 'total_bill',
    nbins = 10,
    title = 'Histogram of Total Bill'
)
fig_histo.show()

#Box Plot: Compare tips given by gender or day.
fig_box = px.box(
    tips,
    x = 'sex',
    y = 'tip',
    title= 'Box Plot: Tip Distribution by Gender',
    color='sex'
)
fig_box.show()

#Bar Plot: Total tip amounts by day of the week.
tip_day = tips.groupby('day')['total_bill'].sum().reset_index()
fig_bar = px.bar(
    tip_day,
    x = 'day',
    title='Total Tips by Day',
    text_auto=True,
)
fig_bar.show()

#Plot: Plot Total Bill vs. Tip
fig_scatter = px.scatter(
tips,
    x = 'total_bill',
    y = 'tip',
    color = 'sex',
    title = 'Scatter Plot : Total Bill vs Tip',
)
fig_scatter.show()

#Pie Chart: Percentage of smokers vs. non-smokers.
smoker_count = tips['smoker'].value_counts().reset_index()
smoker_count.columns = ['smoker', 'count']

fig_pie = px.pie(
    smoker_count,
    names='smoker',
    values='count',
    title='Smokers vs Non-Smokers'
)
fig_pie.show()
