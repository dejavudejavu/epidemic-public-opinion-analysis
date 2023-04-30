#-*- encoding:utf-8 -*-
import pymysql
import pandas as pd
import re
from weiboreach.textTrank.textrank4zh.TextRank4Sentence import TextRank4Sentence
def TextRank():
    # 正则表达式，对话题的内容进行清洗
    surplus = re.compile('【(.*)】')
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            # 筛选条件：topic,话题ID
            sql = "SELECT * FROM weiboreach_weibopost"
            cur.execute(sql)
            # 获取数据，并转化为DataFrame
            weiboData = pd.read_sql(sql, conn)
            weiboData = weiboData.sort_values(by='likeNum', ascending=False)[:10]

            postText = '\n'.join(weiboData['content'].values)
            tr4s = TextRank4Sentence()
            tr4s.analyze(text=postText, lower=True, source='all_filters')

            for item in tr4s.get_key_sentences(num=1):
                weiboContent = item.sentence
            weiboContent = surplus.sub('', weiboContent)
            return weiboContent
    finally:
        conn.close()