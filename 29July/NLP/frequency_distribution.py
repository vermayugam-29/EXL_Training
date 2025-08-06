import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')

# text = 'I am exploring more and more about ML algos and i love ML !'
text = 'Chocolate ice cream is the best treat ever!'
text = text.lower()

tokens = word_tokenize(text)

print('Tokens : ', tokens)
#
# fd = FreqDist(tokens)
# print('Most common words  : ', fd.most_common(3))

#total words
print('Total words : ', len(tokens))
print('First word : ', tokens[0])
print('Last word : ', tokens[-1])