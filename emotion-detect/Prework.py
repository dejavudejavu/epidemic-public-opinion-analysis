import csv
content=[]
with open('test.tsv','r',encoding='utf-8') as f:
    reader=csv.reader(f,delimiter='\t')
    for line in reader:
        if len(line)==2:
            content.append(line)
with open('test1.tsv','w',newline='',encoding='utf-8') as g:
    writer=csv.writer(g,delimiter='\t')
    for a in content:
        writer.writerow(a)