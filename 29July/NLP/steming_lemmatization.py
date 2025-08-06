import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('punkt') #for steming
nltk.download('wordnet') #for lemmatization

#sample data
sentence = 'The cats are running towards the better cat.'

#tokenization
tokens = word_tokenize(sentence)
print('Tokens : ', tokens)

#steming
stemmer = PorterStemmer()

#lemmatization
lemmatizer = WordNetLemmatizer()

#Apply stemming
stemmed_words = [stemmer.stem(i) for i in tokens] #running --> run, cats --> cat
print('Stemmed Words : ', stemmed_words)

lemmatizer_words = [lemmatizer.lemmatize(i,pos = 'v') for i in tokens]
print('Lemmatizer Words : ', lemmatizer_words)