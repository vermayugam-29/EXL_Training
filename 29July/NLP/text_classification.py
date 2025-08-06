from sklearn.feature_extraction.text import CountVectorizer #Words to numbers
from sklearn.naive_bayes import MultinomialNB

texts = ['I love this', 'I hate that', 'This is awesome', 'This is awful']
labels = ['positive', 'negative', 'positive', 'negative']

#Converting words --> numbers
vectorizer = CountVectorizer()
#x is matrix. row = sentence , col = word count
x = vectorizer.fit_transform(texts)
print('Printing X :\n', x.toarray())

#train the model
model = MultinomialNB()
model.fit(x, labels)

#evaluation. test model with new sentences
new_texts = ['I love it', 'This is awful']
xtext = vectorizer.transform(new_texts)

#predictions on model
predictions = model.predict(xtext)
#pairing each sentence with its word
print(list(zip(new_texts, predictions)))