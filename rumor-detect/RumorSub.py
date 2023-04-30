import csv
import jieba
import json
from collections import Counter
results=[]
comments=[]

with open('test.tsv','r',encoding='utf-8') as f:
    reader=csv.reader(f,delimiter='\t')
    for line in reader:
        comments.append(line)

with open('test_results.tsv','r',encoding='utf-8') as g:
    reader=csv.reader(g,delimiter='\t')
    for line in reader:
        results.append(line)

content=[]
R=[]
for (index,result) in enumerate(results):
        if float(result[0])<0.5:
            content.append(comments[index][0])
            R.append(float(result[1]))

words=[]
for dic in content:
    words.append(list(jieba.cut(dic)))

stop_words = []
with open('stopwords.txt','r',encoding='utf-8') as h:
    lines = h.readlines()
    for i in lines:
        word = i.strip()
        stop_words.append(word)
dict_list = {}
for w in words:
    for seg in w:
        if (seg not in stop_words) and len(seg)!=1 :
            if dict_list.get(seg) != None:
                dict_list[seg] += 1
            else:
                dict_list[seg] = 1

most_rum=dict(Counter(dict_list).most_common(100))
rum_sub=[]
rum_val=[]
for a in most_rum:
    rum_sub.append(a)
    rum_val.append(most_rum[a])

most_rum1=dict(Counter(dict_list).most_common(7))
rum_sen=[]
for a in most_rum1:
    num=0
    position=0
    for (index,w) in enumerate(words):
        if a in w and R[index]>num:
            position=index
            num=R[index]
    rum_sen.append(content[position])

con={'words':rum_sub,'value':rum_val,'sentence':rum_sen}
with open('RumorSub.json','w',encoding='utf-8') as fff:
    json.dump(con,fff,ensure_ascii=False)