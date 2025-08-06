import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

#loading the dataset
df = pd.read_csv('data.csv')

#Preprocessing the data
#converting to lower case
def preprocessing():
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    cleaned_reviews = []
    for review in df['review']:
        tokens = word_tokenize(review)
        tokens = [token.lower() for token in tokens if token.isalpha()]
        tokens = [token for token in tokens if token not in stop_words]
        tokens = [stemmer.stem(token) for token in tokens]
        cleaned_reviews.append(' '.join(tokens))

    return cleaned_reviews

def feature_extraction(text):
    # split the data into train and test
    x_train, x_test, y_train, y_test = train_test_split(text, df['sentiment'], test_size=0.2, random_state=42)

    #applying tf-idf to cleaned text
    vectorizer = TfidfVectorizer()
    x_train_tfIDF = vectorizer.fit_transform(x_train)
    x_test_ifIdf = vectorizer.transform(x_test)

    return x_train_tfIDF, x_test_ifIdf, y_train, y_test, vectorizer

def model_training(x_train_tfIDF, x_test_ifIdf, y_train, y_test):
    model = LogisticRegression()
    model.fit(x_train_tfIDF, y_train)

    #predictions
    y_pred = model.predict(x_test_ifIdf)

    plot_confusion_matrix(y_test, y_pred)

    print('Accuracy score : ', accuracy_score(y_pred, y_test))
    print('Classification Report : \n', classification_report(y_test, y_pred))

    return model

def predict_new_reviews(vectorizer, model):
    new_reviews = [
        "Absolutely loved this product, works great!",
        "Worst item I've ever purchased. Totally disappointed.",
        "Decent quality for the price.",
        "It broke after two uses. Terrible quality."
    ]

    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    cleaned = []
    for review in new_reviews:
        tokens = word_tokenize(review)
        tokens = [token.lower() for token in tokens if token.isalpha()]
        tokens = [token for token in tokens if token not in stop_words]
        tokens = [stemmer.stem(token) for token in tokens]
        cleaned.append(' '.join(tokens))

    review_vectors = vectorizer.transform(cleaned)
    predictions = model.predict(review_vectors)

    print("\nPredictions for New Reviews:")
    for review, pred in zip(new_reviews, predictions):
        print(f"\"{review}\"\nPrediction: {pred}\n")


def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred, labels=["positive", "negative"])
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Positive", "Negative"], yticklabels=["Positive", "Negative"])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()



def main():
    text = preprocessing()
    x_train_tfIDF, x_test_tfIdf, y_train, y_test, vectorizer = feature_extraction(text)
    model = model_training(x_train_tfIDF, x_test_tfIdf, y_train, y_test)
    predict_new_reviews(vectorizer, model)


if __name__ == "__main__":
    main()




