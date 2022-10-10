import json
import csv
import requests
import pandas 
from requests.auth import HTTPBasicAuth
import matplotlib.pyplot as plt
import numpy as np

data_1 = pandas.read_csv("data/lang.csv", header=0)
fin_list = list(data_1.language)

n = len(fin_list)

lang_count_2015 = [0] * len(fin_list)
#for n in fin_list:
for i in range(0,len(fin_list)):
    with open('data/trend_2015.csv', 'r') as f1:
        reader = csv.reader(f1, delimiter=',')
        reader.next()
        for row in reader:
            if row[42] == fin_list[i]:
                lang_count_2015[i] = lang_count_2015[i] + 1
            else:
                continue
    f1.close()
    
#for i in range(0,len(fin_list)):
 #   print fin_list[i] + "-"+ str(lang_count_2015[i])

lang_count_2016 = [0] * len(fin_list)
#for n in fin_list:
for i in range(0,len(fin_list)):
    with open('data/trend_2016.csv', 'r') as f2:
        reader = csv.reader(f2, delimiter=',')
        reader.next()
        for row in reader:
            if row[42] == fin_list[i]:
                lang_count_2016[i] = lang_count_2016[i] + 1
            else:
                continue
    f2.close()
    
#for i in range(0,len(fin_list)):
 #   print fin_list[i] + "-"+ str(lang_count_2016[i])

lang_count_2017 = [0] * len(fin_list)
#for n in fin_list:
for i in range(0,len(fin_list)):
    with open('data/trend_2017.csv', 'r') as f3:
        reader = csv.reader(f3, delimiter=',')
        reader.next()
        for row in reader:
            if row[42] == fin_list[i]:
                lang_count_2017[i] = lang_count_2017[i] + 1
            else:
                continue
    f3.close()
    
#for i in range(0,len(fin_list)):
 #   print fin_list[i] + "-"+ str(lang_count_2017[i])


fig, ax = plt.subplots()
index = np.arange(n)
print index
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index - bar_width, lang_count_2015, bar_width, alpha=opacity, color='b', label='2015')
rects2 = plt.bar(index , lang_count_2016, bar_width, alpha=opacity, color='r', label='2016')
rects3 = plt.bar(index + bar_width , lang_count_2017, bar_width, alpha=opacity, color='g', label='2017')

#labels = tuple(fin_list)
print type(fin_list)
#labels = tuple(fin_list)
#l = n in labels
#print type(labels)
print fin_list
a=('ccsd','adad','asd')
plt.xlabel('Languages')
plt.ylabel('Number of Repositories')
plt.title('Number of Created Repositories per Year (Popularity of Programming Languages per year)')
#plt.setp(axes,xticks
plt.xticks(index,fin_list,rotation=90) 
#ax.set_xticklabels(fin_list)
#plt.xticklabels(fin_list)
plt.legend()
ax.autoscale(tight=True)
#plt.tight_layout()
plt.show()
    
