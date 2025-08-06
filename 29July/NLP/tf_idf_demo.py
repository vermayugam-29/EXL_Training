from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'I love programming in Java',
    'Java is a great programming language',
    'I love coding in Java'
]

tf_idf_vectorizer = TfidfVectorizer()

x_tfIdf = tf_idf_vectorizer.fit_transform(docs)

x_tfIdf_array = x_tfIdf.toarray()

print('Feature name (words) : ', tf_idf_vectorizer.get_feature_names_out())
print('Bag of word matrix : \n', x_tfIdf_array)

# # Feature (word) order
# features = tf_idf_vectorizer.get_feature_names_out()
#
# # Print word-wise score for each sentence
# for idx, row in enumerate(x_tfIdf_array):
#     print(f"\n📌 Sentence {idx + 1}: {docs[idx]}")
#     print("TF-IDF Scores:")
#     for word, score in zip(features, row):
#         print(f"{word:>12}: {score:.3f}")