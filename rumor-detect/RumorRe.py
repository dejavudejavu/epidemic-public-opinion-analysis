import csv
lable=[]
with open("test_results.tsv","r",encoding='utf-8',) as csvfile:
    reader = csv.reader(csvfile,delimiter='\t')
    for line in reader:
        if float(line[0]) >= 0.5:
            lable.append('1')
        else:
            lable.append('0')
with open('Rresults.tsv','w',newline='',encoding='utf-8') as g:
    writer=csv.writer(g,delimiter='\t')
    for i in lable:
        writer.writerow([i])