import csv
import json
num=0
rumor=0
with open('test_results.tsv','r',encoding='utf-8') as f:
    reader=csv.reader(f,delimiter='\t')
    for line in reader:
        rumor=rumor+float(line[0])
        num=num+1
with open('RumorAve.json','w',encoding='utf-8') as g:
    json.dump({'真实值':format(rumor/num*100,'.2f')+'%'},g,ensure_ascii=False)