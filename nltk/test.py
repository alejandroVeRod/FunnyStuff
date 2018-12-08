from nltk.tokenize import sent_tokenize,word_tokenize

ex="Hello there, what is your name? My name is Alex, please to meet you."

print(sent_tokenize(ex))
print(word_tokenize(ex))
li=word_tokenize(ex)
print(max(li))

#https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/