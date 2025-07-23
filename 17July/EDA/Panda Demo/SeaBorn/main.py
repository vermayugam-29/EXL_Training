import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the 'tips' dataset
tips = sns.load_dataset("tips")

# Create the scatter plot
# plt.figure(figsize = (6,4))
# sns.scatterplot(data=tips, x="total_bill", y="tip")
# plt.title("Scatter Plot: Total Bill vs Tip")
# plt.xlabel("Total Bill")
# plt.ylabel("Tip")
# plt.tight_layout()
# plt.grid(True)
# plt.show()


#Histograph : distribution of total bills
# plt.figure(figsize = (6,4))
# sns.histplot(data=tips, x = 'total_bill', bins = 20, kde = True, color = 'blue')
# plt.title('Histograph Total Bill')
# plt.xlabel('Total Bill')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()

# Box Plot :- Tip amount by per day
# plt.figure(figsize = (6, 4))
# sns.boxplot(data=tips, x = 'day', y= 'tip', hue='day', palette = 'Set3')
# plt.title('Box Plot of tips by day')
# plt.xlabel('Day')
# plt.ylabel('Tips')
# plt.show()

#Count plot : Gender Distribution
# plt.figure(figsize=(6,4))
# sns.countplot(x='sex', data=tips,hue='sex', palette='pastel')
# plt.title('Gender Distribution')
# plt.xlabel('Gender')
# plt.ylabel('Count')
# plt.show()



#bar plot average total bill by day
plt.figure(figsize = (6, 4))
sns.barplot(x='day', y='total_bill', data=tips, palette='rocket')
plt.title('Average Total Bill')
plt.xlabel('Days')
plt.ylabel('Total Bill')
plt.show()

#box plot tip amounts by time of day
plt.figure(figsize = (6, 4))
sns.boxplot(x='time', y='tip', data=tips, palette='rocket')
plt.title('Tip Chart')
plt.xlabel('Time')
plt.ylabel('Tip')
plt.show()

#Scatter Plot – Total Bill vs Tip, Colored by Smoking Status
plt.figure(figsize = (6, 4))
sns.scatterplot(x='total_bill', y='tip', data=tips, palette='rocket')
plt.title('Total Bill vs Tip')
plt.xlabel('Total')
plt.ylabel('Tip')
plt.show()
