#Turn Words into Their Root Forms Using Stemming and Lemmatization
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('punkt') #for steming
nltk.download('wordnet') #for lemmatization


sentence = "The children were playing in the parks and having fun while the dogs were running happily."

#tokenization
tokens = word_tokenize(sentence)
print('Tokens : \n',tokens)

#stemming
stemmer = PorterStemmer()

#lemmetizer
lemmatizer = WordNetLemmatizer()

stemmed_words = [stemmer.stem(i) for i in tokens]
print('Stemmed words : \n',stemmed_words)

lemmitized_words = [lemmatizer.lemmatize(i, pos = 'v') for i in tokens]
print('Lemmitized words : \n',lemmitized_words)
