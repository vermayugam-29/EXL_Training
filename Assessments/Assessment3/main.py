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
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#downloaded essential packages for nltk
nltk.download('stopwords')
nltk.download('punkt')

#load dataset
df = pd.read_csv('new_customer_emails.csv')

def data_prepration(data):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    new_texts = []

    for emails in data:
        tokens = word_tokenize(emails)
        tokens = [token.lower() for token in tokens if token.isalpha()] # used for punctuation removal
        tokens = [token for token in tokens if token not in stop_words]
        tokens = [stemmer.stem(i) for i in tokens]
        new_texts.append(' '.join(tokens))

    return new_texts

def vectorization(new_emails):
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(new_emails)

    return x, vectorizer

def model_training(x):
    #split the data
    x_train, x_test, y_train, y_test = train_test_split(x, df['Category'], test_size=0.2, random_state=42)

    #train the model
    model = LogisticRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    print('Accuracy Score : ', accuracy_score(y_test, y_pred))
    print('Classification Report : \n',classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    plot_confusion_matrix(cm)

    return model

def prediction_evaluation(vectorizer, model):
    sample_emails = [
        "Could you please provide details about the coverage under my current policy?",
        "When will I receive payment for the medical claim I filed?",
        "I want to understand what is covered for dental under my health insurance.",
        "My phone number has changed. How do I update it in my profile?",
        "I submitted a claim two weeks ago. Can you tell me its current status?",
        "I need to change my residential address in your records.",
        "I recently moved to another city. Please update my contact details.",
        "Just checking if my reimbursement for the doctor visit has been processed.",
        "Can you explain what benefits are included in the Silver plan?",
    ]

    cleaned_emails = data_prepration(sample_emails)

    y_test = vectorizer.transform(cleaned_emails)
    predictions = model.predict(y_test)

    for email, pred in zip(sample_emails, predictions):
        print(f"Email : {email}: \nPrediction : {pred}\n\n")

def count_plot():
    plt.figure(figsize=(12, 8))
    sns.countplot(
        x = 'Category',
        data = df,
    )
    plt.title('Category Distribution of Emails')
    plt.xlabel('Email Category')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def wordcloud_per_category():
    categories = df['Category'].unique()

    for category in categories:
        # Combine all email texts for the current category
        texts = df[df['Category'] == category]['Email Text']
        combined_text = ' '.join(texts)

        # Create WordCloud object
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            stopwords=set(stopwords.words('english'))
        ).generate(combined_text)

        # Plotting
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f"Word Cloud for '{category}' Emails")
        plt.tight_layout()
        plt.show()

def top_tfidf_words_per_category(x, vectorizer):
    feature_names = vectorizer.get_feature_names_out()
    categories = df['Category'].unique()

    for category in categories:
        indices = df[df['Category'] == category].index.tolist()
        x_cat = x[indices]

        avg_scores = x_cat.sum(axis=0) / x_cat.shape[0]

        avg_scores = avg_scores.tolist()[0]
        word_score_pairs = list(zip(feature_names, avg_scores))

        top_words = sorted(word_score_pairs, key=lambda x: x[1], reverse=True)[:10]

        words = [word for word, score in top_words]
        scores = [score for word, score in top_words]

        plt.figure(figsize=(8, 4))
        sns.barplot(x=scores, y=words, palette='flare')
        plt.title(f"Top TF-IDF Words in '{category}' Emails")
        plt.xlabel("Average TF-IDF Score")
        plt.tight_layout()
        plt.show()

def plot_confusion_matrix(cm):
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=sorted(df['Category'].unique()),
                yticklabels=sorted(df['Category'].unique())
                )
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.show()


def main():
    new_emails = data_prepration(df['Email Text'])
    x, vectorizer = vectorization(new_emails)
    model = model_training(x)
    prediction_evaluation(vectorizer, model)
    count_plot()


if __name__ == "__main__":
    main()