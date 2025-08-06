import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')

#identify features and target
x = df[['Years_At_Company', 'Job_Satisfaction']]
y = df['Left_Company']

#split the data into train test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#train the data
model = LogisticRegression()
model.fit(x_train, y_train)

#predictions
y_pred = model.predict(x_test)

#evaluation
print('Accuracy Score : \n',accuracy_score(y_test, y_pred))
print('Classification Report : \n',classification_report(y_test, y_pred))
print('Confusion Matrix : \n',confusion_matrix(y_test, y_pred))

#predicting from sample data
sample_data = pd.DataFrame({
    'Years_At_Company' : [1, 15, 7, 2],
    'Job_Satisfaction' : [9, 0, 3, 3],
})
prediction = model.predict(sample_data)

for i, pred in enumerate(prediction):
    print(f'Employee {i + 1} : {pred}')


#visualize
colors = ['red' if val == 0 else 'green' for val in df['Left_Company']]
plt.scatter(df['Years_At_Company'], df['Job_Satisfaction'],
            c=colors, s= 100)
plt.xlabel('Years At Company')
plt.ylabel('Job Satisfaction')
plt.title('Visualization')
plt.grid(True)
plt.show()
