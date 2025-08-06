import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

df = pd.read_csv('data.csv')

#features and target
x = df['review']
y = df['label']

#split the data for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#vectorizing using tf-idf
vectorizer = TfidfVectorizer(stop_words='english')
x_trained_tfIdf = vectorizer.fit_transform(x_train)
x_test_tfIdf = vectorizer.transform(x_test)

#train the data
model = LogisticRegression()
model.fit(x_trained_tfIdf, y_train)

#predict and evaluate
y_pred = model.predict(x_test_tfIdf)
print('Accuracy score : ', accuracy_score(y_test, y_pred))
print('Classification report : \n', classification_report(y_test, y_pred))

#make predictions on sample data
sample_data = [
    "Completely boring and predictable.",
    "Absolutely fantastic! A must-watch.",
    "An emotional and powerful story."
]
sample_data_tfidf = vectorizer.transform(sample_data)
predictions = model.predict(sample_data_tfidf)

for review, pred in zip(sample_data, predictions):
    label = "Positive" if pred == 1 else "Negative"
    print(f"\n{review} Prediction: {label}")


cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(
    cm
)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()


sns.countplot(x='label', data=df, palette='Set1')

# Title and labels
plt.title('Visualization')
plt.xlabel('Review')
plt.ylabel('No of Reviews')

plt.show()


