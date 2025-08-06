from sklearn.feature_extraction.text import CountVectorizer #Words to numbers
from sklearn.naive_bayes import MultinomialNB

texts = [
    "I love this game",
    "This is amazing",
    "I feel so happy today",
    "This is awful",
    "I hate this",
    "I am really sad",
    "It was a great day",
    "I don’t like it",
    "This is terrible",
    "I feel fantastic!"
]
feelings = [
    "positive","positive","positive","negative","negative",
    "negative","positive","negative","negative","positive"
]

#count words
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)

#train the model
model = MultinomialNB()
model.fit(x, feelings)

#evaluate
test_sentences = [
    "I really love it",
    "This is the worst",
    "What a wonderful day",
    "I am not happy with this",
    "It makes me sad"
]
#test
xsentences = vectorizer.transform(test_sentences)

#predictions
predictions = model.predict(xsentences)
print(list(zip(test_sentences, predictions)))
