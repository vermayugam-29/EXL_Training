import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Outlier_Handling_Input.csv')


#annual Income outlier
q1_ai = df['AnnualIncome'].quantile(0.25)
q3_ai = df['AnnualIncome'].quantile(0.75)
iqr_ai = q3_ai - q1_ai


lower_bound_ai = q1_ai - 1.5 * iqr_ai
upper_bound_ai = q3_ai + 1.5 * iqr_ai


#spending score outlier
q1_ss = df['SpendingScore'].quantile(0.25)
q3_ss = df['SpendingScore'].quantile(0.75)
iqr_ss = q3_ss - q1_ss


lower_bound_ss = q1_ss - 1.5 * iqr_ss
upper_bound_ss = q3_ss + 1.5 * iqr_ss


#purchase count outlier
q1_pc = df['PurchaseCount'].quantile(0.25)
q3_pc = df['PurchaseCount'].quantile(0.75)
iqr_pc = q3_pc - q1_pc


lower_bound_pc = q1_pc - 1.5 * iqr_pc
upper_bound_pc = q3_pc + 1.5 * iqr_pc


filtered_df = df[
    (df['AnnualIncome'] >= lower_bound_ai) & (df['AnnualIncome'] <= upper_bound_ai) &
    (df['SpendingScore'] >= lower_bound_ss) & (df['SpendingScore'] <= upper_bound_ss) &
    (df['PurchaseCount'] >= lower_bound_pc) & (df['PurchaseCount'] <= upper_bound_pc)
]

print(filtered_df)

plt.figure(figsize=(10,6))
sns.violinplot(
    filtered_df,
    x = 'AnnualIncome',
    y = 'PurchaseCount'
)
plt.title('Annual Income vs PurchaseCount')
plt.tight_layout()
plt.show()