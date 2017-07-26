#import modules
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

#Read file
my_file=open("test.txt")
s=my_file.read()

#Remove all meaningless words
meaninglessWords = set(stopwords.words('english'))
word_tokens = word_tokenize(s)
filteredWords = [word for word in word_tokens if not word in meaninglessWords]
for word in word_tokens:
    if word not in meaninglessWords:
        filteredWords.append(word)
print("After Tokenization:")
print ("------------------")
print(word_tokens)
print("After removing meaningless words like a,the etc.,:")
print ("--------------------------------")
print(filteredWords)

#lemmetization
list1=[]
for i in filteredWords:
    lemmatizer = WordNetLemmatizer()
    l=lemmatizer.lemmatize(i,pos='v')
    list1.append(l)
print("After lemmatization:")
print ("------------------")
print(list1)


#Using POS, remove all the verbs
z=pos_tag(filteredWords)
print("POS tagging:")
print ("------------------")
print(z)
list2=[]
list3=[]
for (x,y) in z:
    if (y != 'VB') and (y != 'VBD') and (y != 'VBG') and (y != 'VBN') and (y != 'VBP') and (y != 'VBZ') and (x != ',') and (x != '.'):
        list2.append(x)
print("After removal of verbs:")
print ("------------------")
print(list2)

#Calculate the word frequency of the remaining words
import collections
count=collections.Counter(list2)
print("Word count:")
print ("------------------")
print(count)

#Summary consisting of sentences with most repeated words.
print("Summary:")
print ("------------------")
for line in open("test.txt"):
    if (("Little" in line) or ("Riding" in line) or ("Red" in line) or ("Hood" in line) or ("mother" in line)):
        print(line)