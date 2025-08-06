import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')

text = 'I love ice cream and pizza. Pizza is my favourite food and i LoVe pizza!'

text = text.lower()

tokens = word_tokenize(text)

print('Tokens : ', tokens)

fd = FreqDist(tokens)
print('Freq Dist : ', fd.most_common(3))