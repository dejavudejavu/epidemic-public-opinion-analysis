import csv
import json
times=[]
lables=[]
dict_list={}
with open('test.tsv','r',encoding='utf-8') as f:
    reader1=csv.reader(f,delimiter='\t')
    for line in reader1:
        times.append(line[1])
with open('Rresults.tsv','r',encoding='utf-8') as g:
    reader2=csv.reader(g,delimiter='\t')
    for line in reader2:
        lables.append(line[0])
for (index,a) in enumerate(times):
    if lables[index]=='1':
        if dict_list.get(times[index]) != None:
            dict_list[times[index]] += 1
        else:
            dict_list[times[index]] = 1
content=[]
for a in dict_list:
    content.append({'time':a,'num':dict_list[a]})
with open('RumorChange.json','w',encoding='utf-8') as fff:
    json.dump(content,fff,ensure_ascii=False)