import numpy as np
from sklearn.ensemble import  RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split


def model_train(df):
    df['Churn'] = df['Churn'].apply(
        lambda x: 1 if int(x) == 1 else 0
    )


    features = ['Gender_male', 'Gender_female', 'Age',
                'Tenure', 'Balance', 'EstimatedSalary',
                'NumOfProducts','HasCrCard','IsActiveMember']

    x = df[features]
    y = df['Churn']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    #metrices store for future use
    acc = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("Confusion Matrix:\n", cm)
    print(f"Accuracy: {acc:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}")

    #Top 3 influential features by coefficient values
    importances = model.feature_importances_
    top_indices = np.argsort(importances)[-3:][::-1]
    top_features = [(x.columns[i], importances[i]) for i in top_indices]
    print("Top 3 influential features:", top_features)

    return model , acc, precision, recall, cm, top_features, features, f1

