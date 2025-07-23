import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('employee_skills.csv')

# plt.figure(figsize=(10,6))
# sns.violinplot(
#     df,
#     x = 'Department',
#     y = 'TechSkills'
# )
# plt.title('Department wise Technical Skills Score distribution - (Before Outlier Handling)')
# plt.tight_layout()
# plt.show()


Q1 = df['TechSkills'].quantile(0.25)
Q3 = df['TechSkills'].quantile(0.75)
IQR = Q3 - Q1

filtered_df = df[(df['TechSkills'] >= Q1 - 1.5 * IQR) & (df['TechSkills'] <= Q3 + 1.5 * IQR)]

print(df)
print(filtered_df)
