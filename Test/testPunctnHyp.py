import codecs
import re
import glob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sinstopwords = set(stopwords.words("sinhala"))

file_output = codecs.open('PuctHyptest.txt', 'w', 'utf-16')
with codecs.open('token1test.txt', 'r', 'utf-16') as myfile:
    data = myfile.read().replace('-','')
p = re.compile('[0-9]{1,9}')
p1 = re.compile('[0-9]{1,9}.[0-9]{1,9}')
newdata = p1.sub('0', p.sub('0',data))
words = word_tokenize(newdata)

print ('{} {}'.format('token length before removing stop words :',len(words)))
filtered_sentence = [w for w in words if not w in sinstopwords]
#filtering the stop word list from the source text

print ('{} {}'.format('token length after removing stop words :',len(filtered_sentence)))
for i in filtered_sentence:
    file_output.write(i)
    file_output.write(u"\r\n")  

file_output.close()
