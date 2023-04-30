import csv
lable=[]
with open("test_results.tsv","r",encoding='utf-8',) as csvfile:
    reader = csv.reader(csvfile,delimiter='\t')
    for line in reader:
        if float(line[0]) >= float(line[1]) and float(line[0]) >= float(line[2]):
            lable.append('-1')
        elif float(line[1]) > float(line[0]) and float(line[1]) >= float(line[2]):
            lable.append('0')
        elif float(line[2]) > float(line[0]) and float(line[2]) > float(line[1]):
            lable.append('1')
with open('Eresults.tsv','w',newline='',encoding='utf-8') as g:
    writer=csv.writer(g,delimiter='\t')
    for i in lable:
        writer.writerow([i])