import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

x = df[['Credit_Score', 'Annual_Income']]
y = df['Loan_Approved']

model = LogisticRegression()
model.fit(x, y)

sample_data = pd.DataFrame({
    'Credit_Score': [230, 700],
    'Annual_Income' : [1700000, 40000]
})
predictions = model.predict(sample_data)

for i, pred in enumerate(predictions):
    print(f"Cust {i+1}: {pred}")

# Plot training data
# plt.scatter(df['Credit_Score'], df['Annual_Income'],
#             c=df['Loan_Approved'], cmap='bwr', label='Training Data')

# Plot sample data
plt.scatter(sample_data['Credit_Score'], sample_data['Annual_Income'],
            color='black', marker='X', s=100, label='Sample Customers')

# Labels and title
plt.figure(figsize=(8, 6))
colors = ['red' if val == 0 else 'green' for val in df['Loan_Approved']]
plt.scatter(df['Credit_Score'], df['Annual_Income'], c=colors, s=100, edgecolors='k')
plt.xlabel('Credit Score')
plt.ylabel('Annual Income')
plt.title('Credit Score vs Income (Colored by Loan Approval)')
plt.grid(True)
plt.tight_layout()
plt.show()