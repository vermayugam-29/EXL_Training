import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure consistent visual style
sns.set_theme(style="whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create folder if not exists
os.makedirs("visualizations", exist_ok=True)

def perform_eda(df):
    df = df[df['Churn'].isin([0, 1])]
    df['Churn'] = df['Churn'].astype(int)
    df = df.dropna(subset=['Age', 'Tenure', 'Balance', 'EstimatedSalary'])

    # ========== 1. Churn Distribution (Pie Chart) ==========
    plt.figure(figsize=(6, 6))
    churn_counts = df['Churn'].value_counts()
    plt.pie(churn_counts, labels=['Not Churned', 'Churned'], autopct='%1.1f%%', colors=['#4CAF50', '#FF6F61'], startangle=90, explode=(0, 0.1))
    plt.title("Churn Distribution (Pie Chart)", weight='bold')
    plt.tight_layout()
    plt.savefig("visualizations/churn_pie.png")
    plt.close()

    # ========== 2. Age Distribution (with KDE) ==========
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Age'], kde=True, bins=20, color='#2196F3')
    plt.title("Age Distribution", weight='bold')
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("visualizations/age_distribution.png")
    plt.close()

    # ========== 3. Tenure Distribution ==========
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x='Tenure', color='#E91E63')
    plt.title("Tenure Distribution", weight='bold')
    plt.xlabel("Tenure (Years)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("visualizations/tenure_distribution.png")
    plt.close()

    # ========== 4. Correlation Matrix ==========
    plt.figure(figsize=(10, 8))
    numeric_cols = df.select_dtypes(include=['int64', 'float64'])
    corr = numeric_cols.corr()
    sns.heatmap(corr, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Matrix", weight='bold')
    plt.tight_layout()
    plt.savefig("visualizations/correlation_matrix.png")
    plt.close()

    # ========== 5. Card Ownership vs Churn ==========
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='HasCrCard', hue='Churn', palette='flare')
    plt.title("Credit Card Ownership vs Churn", weight='bold')
    plt.xlabel("Has Credit Card")
    plt.ylabel("Count")
    plt.xticks([0, 1], ['No', 'Yes'])
    plt.legend(title="Churn", labels=['Not Churned', 'Churned'])
    plt.tight_layout()
    plt.savefig("visualizations/credit_card_vs_churn.png")
    plt.close()

    # ========== 6. Age vs EstimatedSalary (Scatter) ==========
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='Age', y='EstimatedSalary', hue='Churn', palette='cool', alpha=0.7)
    plt.title("Age vs Estimated Salary", weight='bold')
    plt.xlabel("Age")
    plt.ylabel("Estimated Salary")
    plt.legend(title='Churn', labels=['Not Churned', 'Churned'])
    plt.tight_layout()
    plt.savefig("visualizations/age_salary_scatter.png")
    plt.close()

    # ========== 7. Products vs Balance (Box Plot) ==========
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='NumOfProducts', y='Balance', palette='crest')
    plt.title("Balance by Number of Products", weight='bold')
    plt.xlabel("Number of Products")
    plt.ylabel("Balance")
    plt.tight_layout()
    plt.savefig("visualizations/products_vs_balance.png")
    plt.close()

    # ========== 8. Active Member vs Churn ==========
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='IsActiveMember', hue='Churn', palette='viridis')
    plt.title("Active Membership vs Churn", weight='bold')
    plt.xlabel("Is Active Member")
    plt.ylabel("Count")
    plt.xticks([0, 1], ['Inactive', 'Active'])
    plt.legend(title="Churn", labels=['Not Churned', 'Churned'])
    plt.tight_layout()
    plt.savefig("visualizations/active_member_vs_churn.png")
    plt.close()

    # ========== 9. Products Count vs Churn ==========
    plt.figure(figsize=(7, 4))
    sns.countplot(data=df, x='NumOfProducts', hue='Churn', palette='icefire')
    plt.title("Number of Products vs Churn", weight='bold')
    plt.xlabel("Number of Products")
    plt.ylabel("Count")
    plt.legend(title="Churn", labels=['Not Churned', 'Churned'])
    plt.tight_layout()
    plt.savefig("visualizations/products_vs_churn.png")
    plt.close()

    # ========== 10. Balance Distribution (KDE by Churn) ==========
    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=df, x='Balance', hue='Churn', fill=True, common_norm=False, palette='rocket')
    plt.title("Balance Distribution by Churn", weight='bold')
    plt.xlabel("Balance")
    plt.ylabel("Density")
    plt.legend(title="Churn", labels=['Not Churned', 'Churned'])
    plt.tight_layout()
    plt.savefig("visualizations/balance_kde_churn.png")
    plt.close()
