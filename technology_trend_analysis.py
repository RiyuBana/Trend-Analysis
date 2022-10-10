import json
import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np
from langdetect import detect
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.collocations import *
import matplotlib.pyplot as plt

#nltk.download('stopwords')

def clean(text = '', stopwords = []):
    #tokenize
    tokens = word_tokenize(text.strip())
    #lowercase
    clean = [i.lower() for i in tokens]
    #remove stopwords
    clean = [i for i in clean if i not in stopwords]
    #remove punctuations
    punctuations = list(string.punctuation)
    clean = [i.strip(''.join(punctuations)) for i in clean if i not in punctuations]

    return " ".join(clean)

data_1 = pandas.read_csv("data/test.csv", header=0)

print data_1

df = pandas.DataFrame(data_1)
print df.columns

df = df.dropna(subset=['description'])
print df.columns

df['lang'] = df.apply(lambda x: detect(x['description']),axis=1)
print df['lang']

df = df[df['lang'] == 'en']
#print df.columns

df['clean'] = df['description'].apply(str)
df['clean'] = df['clean'].apply(lambda x: clean(text = x, stopwords = stopwords.words('english')))
print df['clean'].head(5)

list_documents = df['clean'].apply(lambda x: x.split()).tolist()
print list_documents

bigram_measures = nltk.collocations.BigramAssocMeasures()
bigram_finder = BigramCollocationFinder.from_documents(list_documents)
bigram_finder.apply_freq_filter(3)

bigrams = bigram_finder.nbest(bigram_measures.raw_freq, 20)
ngram = list(bigram_finder.ngram_fd.items())
ngram.sort(key=lambda item: item[-1], reverse=True)
frequency = [(" ".join(k), v) for k,v in ngram]
print frequency

df=pandas.DataFrame(frequency)
plt.style.use('ggplot')
df.set_index([0], inplace = True)
df.sort_values(by = [1], ascending = False).head(20).plot(kind = 'barh')
plt.title('Trending Technologies')
plt.ylabel('Technology')
plt.xlabel('Popularity')
plt.legend().set_visible(False)

plt.show()
