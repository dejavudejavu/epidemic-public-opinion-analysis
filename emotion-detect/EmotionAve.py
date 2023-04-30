import csv
import json
num=0
pos=0
with open('test_results.tsv','r',encoding='utf-8') as f:
    reader=csv.reader(f,delimiter='\t')
    for line in reader:
        pos=pos+float(line[2])
        num=num+1
with open('EmotionAve.json','w',encoding='utf-8') as g:
    json.dump({'情感值':format(pos/num*100,'.2f')+'%'},g,ensure_ascii=False)