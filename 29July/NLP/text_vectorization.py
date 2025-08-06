from sklearn.feature_extraction.text import CountVectorizer

docs = [
    'I love programming in Java',
    'Java is a great programming language',
    'I love coding in Java'
]

vectorize = CountVectorizer()
x = vectorize.fit_transform(docs)

x_array = x.toarray()

print('Feature name (words) : ', vectorize.get_feature_names_out())
print('Bag of word matrix : \n', x_array)