import csv
times=[]
comments=[]
with open("test.csv","r",encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        if line!=[]:
            times.append(line[1][:-8])
            comments.append(line[3])
del times[0]
del comments[0]
with open("test.tsv","w",newline='',encoding='utf-8') as g:
    writer=csv.writer(g,delimiter='\t')
    for (index,time) in enumerate(times):
        writer.writerow([comments[index],times[index]])

