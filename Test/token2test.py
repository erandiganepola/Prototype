import codecs
import string
import glob
from nltk.tokenize import sent_tokenize, word_tokenize

file_output = codecs.open('era1.txt', 'w', 'utf-16')
file_output_punctuation = codecs.open('era2.txt', 'w', 'utf-16')
with codecs.open('token1test.txt', 'r', 'utf-16') as myfile:
    data = myfile.read()

    for c in string.punctuation:
        data = data.replace(c, "")
    file_output_punctuation.write(data)

for i in word_tokenize(data):
    file_output.write(i)
    file_output.write(u"\r\n")  

file_output.close()

# string module have some other sets of elements that can be removed (like digits).