from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
 
words = ["game","gaming","gamed","games"]
ps = PorterStemmer()
for word in words:
    print( "%s \t %s" %(word,ps.stem(word)) )

print("\n")

sentence = "Gaming, the gamers played games and gamed over "
words = word_tokenize(sentence)
for word in words:
    print(word + ":" + ps.stem(word))