import csv
import json
neg=0
neu=0
pos=0
with open('Eresults.tsv','r',encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for line in reader:
        if line[0]=='-1':
            neg = neg + 1
        elif line[0]=='0':
            neu = neu + 1
        elif line[0]=='1':
            pos = pos + 1
content=[{'name':'积极','value':pos},{'name':'中性','value':neu},{'name':'消极','value':neg}]
with open('emotion.json','w',encoding='utf-8') as g:
    json.dump(content,g,ensure_ascii=False)