import sys
import codecs
import glob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

doc1 = sys.argv[1]
doc2 = sys.argv[2]
sinstopwords = set(stopwords.words("sinhala"))

file_output = codecs.open('result.txt', 'w', 'utf-16')
with codecs.open(doc1, 'r', 'utf-16') as myfile1:
    data1 = myfile1.read()
words1 = word_tokenize(data1)
with codecs.open(doc2, 'r', 'utf-16') as myfile2:
    data2 = myfile2.read()
words2 = word_tokenize(data2)

print ('{} {}'.format('token length of doc1 before removing stop words :',len(words1)))
print ('{} {}'.format('token length of doc2 before removing stop words :',len(words2)))

filtered_sentence1 = [w1 for w1 in words1 if not w1 in sinstopwords]
filtered_sentence2 = [w2 for w2 in words2 if not w2 in sinstopwords]
#filtering the stop word list from the source text

print ('{} {}'.format('token length of doc1 after removing stop words :',len(filtered_sentence1)))
print ('{} {}'.format('token length of doc2 after removing stop words :',len(filtered_sentence2)))

for i in filtered_sentence1:
    file_output.write(i)
    file_output.write(' ')

file_output.write(u"\r\n")
file_output.write(u"\r\n")

for j in filtered_sentence2:
    file_output.write(j)
    file_output.write(' ')    

file_output.close()
