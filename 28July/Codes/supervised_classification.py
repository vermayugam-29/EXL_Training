import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

titanic = sns.load_dataset('titanic')

titanic = titanic[['survived', 'age', 'sex', 'pclass']].dropna() # cleaning


titanic['sex'] = titanic['sex'].map({'male':0, 'female': 1})

x = titanic[['sex', 'age', 'pclass']]
y = titanic['survived']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)

print(f'accuracy : {acc:.2f}')
print(classification_report(y_test, y_pred))

# ------------ prdict new data----------------

data = pd.DataFrame({
    'sex': ['female'],
    'age': [22],
    'pclass': [3]
})
data['sex'] = data['sex'].map({'female': 1, 'male': 0})

new_pred = model.predict(data)
print('Survived' if new_pred[0] == 1 else 'Did not survive')

