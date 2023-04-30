# coding=utf-8
import csv
import pymysql
import pandas as pd
import re
from textrank4zh import TextRank4Keyword
from project1.settings import STATICFILES_DIRS
def get_PosNegWord():
    pos_negWord = {}
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            # 筛选条件：topic,话题ID
            sql = "SELECT * FROM weiboreach_comment"
            cur.execute(sql)
            # 获取数据，并转化为DataFrame
            weiboData = pd.read_sql(sql, conn)
            lines=[]
            for index, row in weiboData.iterrows():
                commentText = ''.join(re.findall(r'[\u4e00-\u9fa5]', row['content']))
                lines.append(commentText)
            lables=[]
            with open(STATICFILES_DIRS[0]+'/dataAnalysis/test_results.tsv', 'r', encoding='utf-8') as f:
                reader=csv.reader(f,delimiter='\t')
                for lable in reader:
                    lables.append(float(lable[0]))
            other_lines1=[]
            other_lines2=[]
            for index,num in enumerate(lables):
                if num>=0.5:
                    other_lines1.append(lines[index])
                else:
                    other_lines2.append(lines[index])
            tr4w=TextRank4Keyword()
            sum=''
            for text in other_lines1:
                sum=sum+text
            tr4w.analyze(text=sum, lower=True, window=3, pagerank_config={'alpha': 0.85})
            pos_list = []
            for item in tr4w.get_keywords(20, word_min_len=2):
                posWord = {}
                posWord['name'] = item.word
                posWord['value'] = round(item.weight * 10000)
                pos_list.append(posWord)
                del posWord

            tr4w_1=TextRank4Keyword()
            sum_1=''
            for text in other_lines2:
                sum_1=sum_1+text
            tr4w_1.analyze(text=sum_1, lower=True, window=3, pagerank_config={'alpha': 0.85})
            neg_list = []
            for item in tr4w_1.get_keywords(20, word_min_len=2):
                negWord = {}
                negWord['name'] = item.word
                negWord['value'] = round(item.weight * 10000)
                neg_list.append(negWord)
                del negWord
            pos_negWord['pos'] = pos_list
            pos_negWord['neg'] = neg_list
            return pos_negWord
    finally:
        conn.close()
