import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = {
    'study_hours': [1, 2, 3.5, 5, 0.5, 4, 6, 2, 3, 4.5],
    'attendance': ['Low', 'Medium', 'High', 'High', 'Low', 'High', 'High', 'Medium', 'Medium', 'High'],
    'internet_usage': ['High', 'Low', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low'],
    'extra_classes': ['No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes'],
    'pass_exam': ['No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

#Encoding
le_attendance = LabelEncoder()
df['attendance'] = le_attendance.fit_transform(df['attendance'])

le_internet = LabelEncoder()
df['internet_usage'] = le_internet.fit_transform(df['internet_usage'])

le_extra = LabelEncoder()
df['extra_classes'] = le_extra.fit_transform(df['extra_classes'])

#map target
df['pass_exam'] = df['pass_exam'].map({'No' : 0, 'Yes' : 1})

#select the data for train and test
train_set = ['study_hours', 'attendance', 'internet_usage', 'extra_classes']
test = 'pass_exam'

x = df[train_set]
y = df[test]

#split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)

#modeling
model = LogisticRegression()
model.fit(x_train, y_train)

#evaluation / testing
y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred)) #how many predictions we got correct
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred)) #eg aapne 'yes' bola tha aya 'no' ha
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))

#deployment
sample_students = pd.DataFrame({
    'study_hours': [2.5, 0.5],
    'attendance': [
        le_attendance.transform(['Medium'])[0],
        le_attendance.transform(['Low'])[0]
    ],
    'internet_usage': [
        le_internet.transform(['High'])[0],
        le_internet.transform(['High'])[0]
    ],
    'extra_classes': [
        le_extra.transform(['Yes'])[0],
        le_extra.transform(['No'])[0]
    ]
})

sample_predictions = model.predict(sample_students)
print("Sample Predictions:", ['Yes' if pred == 1 else 'No' for pred in sample_predictions])
print(sample_students)