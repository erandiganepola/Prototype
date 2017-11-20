import nltk
import math
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from collections import Counter
import operator

data = 'Julie loves me more than Linda loves me'
data1 = 'Jane likes me more than Julie loves me'
#Contrarily a term that occurs in nearly all documents has hardly any discriminative power and is given a low weight, which is usually true for stop words. For calculating the tf-idf weight of a term in a particular document, it is necessary to know two things
data2 = 'subash basnayake subash basnayake subash basnayake'
data3 = 'Julie loves me more than Linda loves me'
data4 = 'Jane likes me more than Julie loves me'
token = nltk.word_tokenize(data)
token1 = nltk.word_tokenize(data1)
token2 = nltk.word_tokenize(data2)
bigrams = set(ngrams(token,2))
bigrams2 = ngrams(token,2)
bigrams3 = ngrams(token1,2)
trigrams = set(ngrams(token,3))
bigrams1 = set(ngrams(token1,2))
trigrams1 = set(ngrams(token1,3))
inter = bigrams.intersection(bigrams1)
inter1 = trigrams.intersection(trigrams1)
union = bigrams.union(bigrams1)
union1 = trigrams.union(trigrams1)
inter2 = set(token).intersection(set(token1))
union2 = set(token).union(set(token1))
print ('Jaccard using bigram =' + str(len(inter)/len(union)))
print ('Jaccard using trigram =' + str(len(inter1)/len(union1)))
print ('Jaccard =' + str(len(inter2)/len(union2)))
def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

#print (trigrams)

#def ngrams(sentence, n):
 #   return ([sentence.split()[i:] for i in range(n)])

#print (data.split())
#print (ngrams(data,2))
##fdist = nltk.FreqDist(token)
##vector = []
##for k,v in fdist.items():
##    #print (k,v)
##    vector.append(v)
##
##print (len(vector))


##fdist1 = nltk.FreqDist(token1)
##vector1 = []
##for k,v in fdist1.items():
##    #print (k,v)
##    vector1.append(v)
##
##print (len(vector1))
def dot_product2(v1, v2):
    return sum(map(operator.mul, v1, v2))


def vector_cos5(v1, v2):
    prod = dot_product2(v1, v2)
    len1 = math.sqrt(dot_product2(v1, v1))
    len2 = math.sqrt(dot_product2(v2, v2))
    return prod / (len1 * len2)
v1,v2 = build_vector(token,token1)
print (v1)
print (v2)
print (vector_cos5(v1,v2))

