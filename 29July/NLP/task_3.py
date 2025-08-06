import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('punkt') #for steming
nltk.download('wordnet') #for lemmatization

words = [
    'running', 'better', 'easily', 'happier', 'swimming',
    'studies', 'flying', 'worse', 'cats', 'geese'
]

#stemming
stemmer = PorterStemmer()

#lemmetizer
lemmatizer = WordNetLemmatizer()

stemmed_words = [stemmer.stem(i) for i in words]
print('Stemmed words : \n',stemmed_words)

lemmitized_words = [lemmatizer.lemmatize(i) for i in words]
print('Lemmitized words : \n',lemmitized_words)
