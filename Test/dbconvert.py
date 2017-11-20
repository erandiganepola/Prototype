import codecs
import glob

file_output = codecs.open('sinhala.txt', 'w', 'utf-8')
with codecs.open('WORD1.txt', 'r', 'utf-8') as myfile1:
    data1 = myfile1.read()

data = str(data1)
data2 = data.replace("|",",")
data3 = data2.replace('\"','')

file_output.write(data3)
