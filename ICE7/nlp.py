import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.tag import pos_tag
import numpy
from nltk import ne_chunk
from collections import Counter
from nltk.util import ngrams
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
#nltk.download('punkt')
#nltk.download('word_tokenize')
#nltk.download('wordpunct_tokenize')
#nltk.download('sent_tokenize')

s="Hi this is a python program. I am doing the in class exercise. Time given to solve is 300 minutes."
meaning=wn.synsets('program')
for a in meaning:
    print (a.definition())
print ([str(syns.definition) for syns in meaning])
x=sent_tokenize(s)
print x
for t in x:
    print word_tokenize(t)

#lemmetization
print "lemmatization:"
lemmatizer=WordNetLemmatizer()
print lemmatizer.lemmatize('cooking')
print lemmatizer.lemmatize('cooking',pos='v')

#stemming
stemmer=PorterStemmer()
print "stemming"
print stemmer.stem('cooking')
#nltk.download('all')

#words=word_tokenize(s)
print pos_tag(word_tokenize(s))

# NER
print(ne_chunk(pos_tag(wordpunct_tokenize(s))))


token=nltk.word_tokenize(s)
trigrams=ngrams(token,3)
print Counter(trigrams)