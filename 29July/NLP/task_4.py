# Objective:
# Apply Bag of Words (BoW) to convert text into a word count matrix.
# Use TF-IDF to calculate the importance of words in the given text.
# Compare the output of BoW and TF-IDF to understand their differences.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love programming in Python",
    "Python is a great programming language",
    "I love to code in Python",
    "Python programming is amazing",
    "I am learning Python programming"
]

#Word count matrix
vectorize = CountVectorizer()
x = vectorize.fit_transform(documents)

x_array = x.toarray()

print('Feature names : ', vectorize.get_feature_names_out())
print('Bag of Words : \n' , x_array)

#TF_IDF vectorization
tfIdf = TfidfVectorizer()
x_tfidf = tfIdf.fit_transform(documents)

x_tfIdf_array = x_tfidf.toarray()

print('Feature names : ', tfIdf.get_feature_names_out())
print('Bag of Words : \n' , x_tfIdf_array)