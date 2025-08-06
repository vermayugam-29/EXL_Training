import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt_tab')
nltk.download('stopwords')

text = "Artificial Intelligence is transforming industries by enabling machines to learn, adapt, and make decisions with minimal human intervention."
tokens = word_tokenize(text)
print("Tokens: ", tokens)


#step 2 remove stop words
stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word.lower() not in stop_words]
print("Stop words: ",filtered)


#step3 steming
stemer = PorterStemmer()
stemed = [stemer.stem(word) for word in filtered]
print("After stemming: ",stemed)