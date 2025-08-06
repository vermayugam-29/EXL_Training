# import pandas as pd  
# import seaborn as sns 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
# import matplotlib.pyplot as plt 

# titanic = sns.load_dataset('titanic')

# titanic = titanic[['survived', 'age', 'sex', 'pclass']].dropna()

# titanic['sex'] = titanic['sex'].map({'male':0, 'female': 1})

# x = titanic[['sex', 'age', 'pclass']]
# y = titanic['survived']

# # splitting into train and test
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# # training model
# model = LogisticRegression()
# model.fit(x_train, y_train)

# # make presiction
# y_pred = model.predict(x_test)

# # ------ Evaluate the metrices-----------
# accuracy = accuracy_score(y_test, y_pred)
# precision = precision_score(y_test, y_pred)
# recall = recall_score(y_test, y_pred)
# f1 = f1_score(y_test, y_pred)

# print(f'Accuracy = {accuracy: .2f}')
# print(f'Precision = {precision: .2f}')
# print(f'Recall = {recall: .2f}')
# print(f'F1 score = {f1: .2f}')

# print('\n Classification report: ')
# print(classification_report(y_test, y_pred, target_names=['Not Survived', 'Survived']))

# # confuse matrix visualisation
# confuse_matrix = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(5,4))
# sns.heatmap(confuse_matrix, annot=True, fmt='d', cmap='Blues')
# plt.title('Confusion matrix')
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.tight_layout()
# plt.show()


# ------------------------------------------------MY attempt-----------------------------------------------------
# import pandas as pd  
# import seaborn as sns 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
# import matplotlib.pyplot as plt 

# titanic = sns.load_dataset('titanic')

# titanic = titanic[['survived', 'age', 'sex', 'pclass']].dropna()

# titanic['sex'] = titanic['sex'].map({'male':0, 'female': 1})

# x = titanic[['sex', 'age', 'pclass']]
# y = titanic['survived']

# # splitting into train and test
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42, title='Logistic Regression (All Features)')

# x_sex = titanic[['sex']]
# evaluate_model(LogisticRegression(), x_sex, y, test_size=0.2, title="Logistic Regression (Only Sex)")

# # training model
# model = LogisticRegression()
# model.fit(x_train, y_train)

# # make presiction
# y_pred = model.predict(x_test)

# # ------ Evaluate the metrices-----------
# accuracy = accuracy_score(y_test, y_pred)
# precision = precision_score(y_test, y_pred)
# recall = recall_score(y_test, y_pred)
# f1 = f1_score(y_test, y_pred)

# print(f'Accuracy = {accuracy: .2f}')
# print(f'Precision = {precision: .2f}')
# print(f'Recall = {recall: .2f}')
# print(f'F1 score = {f1: .2f}')

# print('\n Classification report: ')
# print(classification_report(y_test, y_pred, target_names=['Not Survived', 'Survived']))

# # confuse matrix visualisation
# confuse_matrix = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(5,4))
# sns.heatmap(confuse_matrix, annot=True, fmt='d', cmap='Blues')
# plt.title('Confusion matrix')
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.tight_layout()
# plt.show()


# -----------------------Help------------------------------------------------------------
import pandas as pd  
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt 

# Load and preprocess data
titanic = sns.load_dataset('titanic')
titanic = titanic[['survived', 'age', 'sex', 'pclass']].dropna()
titanic['sex'] = titanic['sex'].map({'male':0, 'female': 1})

# Helper function to evaluate model
def evaluate_model(model, x, y, test_size=0.3, title="Model Evaluation"):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"\n {title} | Test size: {test_size}")
    print(f'Accuracy  = {accuracy:.2f}')
    print(f'Precision = {precision:.2f}')
    print(f'Recall    = {recall:.2f}')
    print(f'F1 Score  = {f1:.2f}')
    # print('\nClassification Report:')
    # print(classification_report(y_test, y_pred, target_names=['Not Survived', 'Survived']))
    
    # Plot confusion matrix
    # cm = confusion_matrix(y_test, y_pred)
    # plt.figure(figsize=(4, 3))
    # sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    # plt.title(f'Confusion Matrix: {title}')
    # plt.xlabel('Predicted')
    # plt.ylabel('Actual')
    # plt.tight_layout()
    # plt.show()

# Target variable
y = titanic['survived']

# 1. Logistic Regression with all features
x_all = titanic[['sex', 'age', 'pclass']]
evaluate_model(LogisticRegression(), x_all, y, test_size=0.2, title="Logistic Regression (All Features)")

# 2. Logistic Regression with only 'sex'
x_sex = titanic[['sex']]
evaluate_model(LogisticRegression(), x_sex, y, test_size=0.2, title="Logistic Regression (Only Sex)")


# 4. Decision Tree with all features
evaluate_model(DecisionTreeClassifier(), x_all, y, test_size=0.2, title="Decision Tree (All Features)")
