import nltk
from nltk.book import *

print(set(text1))
text1.concordance("monstrous")
text1_len = len(text1)
text2_len = len(text2)
print("Hello length %s %s" %(text1_len, text2_len))

text3_count=text3.count("smote")
print("Hello count %d" %text3_count)

def lexical_diversity(text):
    return len(set(text)) / len(text)
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
text4_lexical = lexical_diversity(text4)
print("Hello lexical %f" %text4_lexical)