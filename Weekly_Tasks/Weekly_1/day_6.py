import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def handle_visualization(df):
    #Step1. Region-wise Revenue: Bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(df, x='Region', y='TotalRevenue')
    plt.title('Region-wise Total Revenue')
    plt.xlabel('Region')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    plt.show()


    #Step2. Revenue over time: Line chart
    df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'])
    revenue_time = df.groupby('LastPurchaseDate')['TotalRevenue'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(revenue_time, x='LastPurchaseDate', y='TotalRevenue',marker='o')
    plt.title('Total Revenue Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    plt.show()

    #Step3. Product-wise share: Pie chart
    product_share = df['Product'].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(product_share,labels=product_share.index, startangle=90)
    plt.title('Product-wise Share')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


    #Step4. Scatter plot: Purchases vs TotalRevenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(df, x='Purchases', y='TotalRevenue', hue='Region', palette='Set2')
    plt.title('Purchases vs Total Revenue')
    plt.xlabel('Purchases')
    plt.ylabel('Total Revenue')
    plt.tight_layout()
    plt.show()


