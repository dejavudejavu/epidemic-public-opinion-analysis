import csv
maxpos=0
maxneu=0
maxneg=0
with open('test_results.tsv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile,delimiter='\t')
    for (index,line) in enumerate(reader):
        if float(line[0]) > maxneg:
            negIn=index
            maxneg=float(line[0])
        if float(line[1]) > maxneu:
            neuIn=index
            maxneu = float(line[1])
        if float(line[2]) > maxpos:
            posIn=index
            maxpos = float(line[2])
content=[]
with open('test.tsv','r',encoding='utf-8') as g:
    reader=csv.reader(g,delimiter='\t')
    for line in reader:
        content.append(line[0])

with open('Max.txt','w',encoding='utf-8') as h:
    h.write('最积极：'+content[posIn]+'\n')
    h.write('最中性：'+content[neuIn]+'\n')
    h.write('最消极：'+content[negIn])