from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

documents = [
    "Free lottery ticket, claim now", #Spam
    "Hey, how are you doing today?",  #NotSpam
    "Get free meal",                  #Spam
    "Interview scheduled tomorrow 12 PM", #NotSpam
    "Important: Your account has been compromised" #Spam
]

#Spam --> 1, NotSpam --> 0
labels = [
    1, 0, 1, 0, 1
]

#Convert text into numbers using tf - idf
vectorizer = TfidfVectorizer(stop_words='english')
x = vectorizer.fit_transform(documents)


#Split the data into  train and test
X_train, X_test, y_train, y_test = train_test_split(x, labels, test_size=0.3, random_state=42)

#trainn the model
model = LogisticRegression()
model.fit(X_train, y_train)

#predicting using training model
y_predict = model.predict(X_test)

#evaluate
print('Classification Report : \n',classification_report(y_test, y_predict, zero_division=0))