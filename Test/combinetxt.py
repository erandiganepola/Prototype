import codecs
import commands
import glob   
path = '/home/subash/Documents/SINHALACORPUS/NEWSPAPERS/FEATURE/OTHER/*.TXT'   
files=glob.glob(path)
file_output = codecs.open('new.TXT', 'w', 'utf-16')

for file in files:
    file_stream = codecs.open(file, 'r', 'utf-16')
    for l in file_stream:
        file_output = codecs.open('new.TXT', 'a', 'utf-16')
        file_output.write(l)
        
file_stream.close()
file_output.close()