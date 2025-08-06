import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

#Load the csv
df = pd.read_csv('data.csv')

#identifying features and target
x = df[['Accidents_Last_3_Years', 'Age']]
y = df['Claimed_Insurance']


#Splitting the data for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)


#training the data
model = LogisticRegression()
model.fit(x_train, y_train)


#predicting
y_pred = model.predict(x_test)

print('Accuracy Score : \n',accuracy_score(y_test, y_pred))
print('Classification Report : \n',classification_report(y_test, y_pred))
print('Confusion Matrix : \n',confusion_matrix(y_test, y_pred))


#creating sample data and making predictions
sample_data = pd.DataFrame({
    'Accidents_Last_3_Years': [0, 1, 10, 4, 2],
    'Age': [34, 18, 23, 45, 67],
})

predictions = model.predict(sample_data)

for i, pred in enumerate(predictions):
    age = sample_data.loc[i, 'Age']
    accidents = sample_data.loc[i, 'Accidents_Last_3_Years']
    print(f'Cust {i + 1}, Age : {age}, Accidents : {accidents} ===> Insurance Claimed : {pred == 1}')


#ploting
plt.figure(figsize=(10,8))
colors = ['red' if val == 0 else 'green' for val in df['Claimed_Insurance']]
plt.scatter(
    df['Accidents_Last_3_Years'],
    df['Age'],
    c = colors,
    s = 100
)
plt.xlabel('Accidents Last_3_Years')
plt.ylabel('Age')
plt.title('Accidents Last_3_Years vs. Age')
plt.grid(True)
plt.tight_layout()
plt.show()