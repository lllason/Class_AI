import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
words = word_tokenize(data)
print(words)

stopWords = set(stopwords.words('chinese'))

print("------------------------")
print(stopWords)
print("------------------------")

words = word_tokenize(data)
wordsFiltered = []
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
print(wordsFiltered)