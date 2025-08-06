import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder #Convert text to numeric values
from sklearn.linear_model import LogisticRegression #Categorical binary classification
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report #evalutaion/ testing
pd.set_option('display.max_columns', None)

# Step 1 & 2: Business & Data Understanding
data = {
    'age': [25, 20, 22, 40, 35, 23, 31, 28, 45, 37],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'time_on_site': [5.5, 10.2, 3.1, 8.5, 7.0, 2.0, 6.0, 9.1, 4.3, 11.5],
    'pages_visited': [4, 10, 2, 7, 6, 1, 5, 9, 3, 11],
    'device': ['Mobile', 'Desktop', 'Mobile', 'Desktop', 'Tablet', 'Mobile', 'Tablet', 'Desktop', 'Mobile', 'Desktop'],
    'purchase': ['No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

# Step 3: Data Preparation
# Encode categorical features
le_gender = LabelEncoder()
df['gender_encoded'] = le_gender.fit_transform(df['gender'])

le_device = LabelEncoder()
df['device_encoded'] = le_device.fit_transform(df['device'])

# Encode target variable
df['purchase_encoded'] = df['purchase'].map({'No': 0, 'Yes': 1})

# Select features and target
#features ke base par prediction honge
features = ['age', 'time_on_site', 'pages_visited', 'gender_encoded', 'device_encoded']
#target ko predict karna ha
target = 'purchase_encoded'

x = df[features] #x for input
y = df[target] # y for output

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Step 4: Modeling
model = LogisticRegression()
model.fit(x_train, y_train)

# Step 5: Evaluation
y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred)) #how many predictions we got correct
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred)) #eg aapne 'yes' bola tha aya 'no' ha
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 6: Simulated Deployment
sample_test_data = pd.DataFrame({
    'age': [29, 24],
    'time_on_site': [7.5, 3.2],
    'pages_visited': [6, 2],
    'gender_encoded': [
        le_gender.transform(['Female'])[0],
        le_gender.transform(['Male'])[0]
    ],
    'device_encoded': [
        le_device.transform(['Mobile'])[0],
        le_device.transform(['Desktop'])[0]
    ]
})

sample_predictions = model.predict(sample_test_data)
print("Sample Predictions:", ['Yes' if pred == 1 else 'No' for pred in sample_predictions])
print(sample_test_data)