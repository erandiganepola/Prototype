import codecs
import glob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sinstopwords = set(stopwords.words("sinhala"))

file_output = codecs.open('new2stp.txt', 'w', 'utf-16')
with codecs.open('token1test.txt', 'r', 'utf-16') as myfile:
    data = myfile.read()
words = word_tokenize(data)

print ('{} {}'.format('token length before removing stop words :',len(words)))
filtered_sentence = [w for w in words if not w in sinstopwords]
#filtering the stop word list from the source text

print ('{} {}'.format('token length after removing stop words :',len(filtered_sentence)))
for i in filtered_sentence:
    file_output.write(i)
    file_output.write(u"\r\n")  

file_output.close()
