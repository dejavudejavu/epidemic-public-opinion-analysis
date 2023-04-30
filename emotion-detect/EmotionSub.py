import csv
import jieba
import json
from collections import Counter
results=[]
comments=[]
with open('Eresults.tsv','r',encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for line in reader:
        results.append(line)
with open('test.tsv','r',encoding='utf-8') as g:
    reader=csv.reader(g,delimiter='\t')
    for line in reader:
        comments.append(line)
neg=''
neu=''
pos=''
for (index,result) in enumerate(results):
    if result[0]=='1':
        pos=pos+comments[index][0]
    elif result[0]=='0':
        neu=neu+comments[index][0]
    elif result[0]=='-1':
        neg=neg+comments[index][0]
pos_list=jieba.cut(pos)
neu_list=jieba.cut(neu)
neg_list=jieba.cut(neg)
stop_words = []
with open('stopwords.txt','r',encoding='utf-8') as h:
    lines = h.readlines()
    for i in lines:
        word = i.strip()
        stop_words.append(word)

pos_dict={}
for seg in pos_list:
    if (seg not in stop_words) and len(seg)!=1 :
        if pos_dict.get(seg) != None:
            pos_dict[seg] += 1
        else:
            pos_dict[seg] = 1
most_pos=dict(Counter(pos_dict).most_common(100))
pos_sub=[]
for a in most_pos:
    pos_sub.append({'name':a,'value':most_pos[a]})

neu_dict={}
for seg in neu_list:
    if (seg not in stop_words) and len(seg)!=1 :
        if neu_dict.get(seg) != None:
            neu_dict[seg] += 1
        else:
            neu_dict[seg] = 1
most_neu=dict(Counter(neu_dict).most_common(100))
neu_sub=[]
for a in most_neu:
    neu_sub.append({'name':a,'value':most_neu[a]})

neg_dict={}
for seg in neg_list:
    if (seg not in stop_words) and len(seg)!=1 :
        if neg_dict.get(seg) != None:
            neg_dict[seg] += 1
        else:
            neg_dict[seg] = 1
most_neg=dict(Counter(neg_dict).most_common(100))
neg_sub=[]
for a in most_neg:
    neg_sub.append({'name':a,'value':most_neg[a]})

content=[{'pos':pos_sub,'neu':neu_sub,'neg':neg_sub}]
with open('EmotionSub.json','w',encoding='utf-8') as ff:
    json.dump(content,ff,ensure_ascii=False)