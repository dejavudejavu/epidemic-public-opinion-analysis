import pymysql
import pandas as pd
import numpy as np
import re
import jieba
from project1.settings import STATICFILES_DIRS
'''
函数名：get_weiboIntroduction
参数：hId: 话题的唯一标识ID
作用: 获取话题概括
返回值：weibo_introduction，包含博文内容和博文发布的时间，字典类型
'''
def get_weiboIntroduction(hId):
    # 正则表达式，对话题的内容进行清洗
    surplus = re.compile('【(.*)】')
    # 返回字典
    weibo_introduction = {}
    # 连接数据库，后期可以改为MongoDB的
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            # 筛选条件：topic,话题ID
            sql = "SELECT * FROM weiboreach_weibopost where topic='{}'".format(hId)
            cur.execute(sql)
            # 获取数据，并转化为DataFrame
            weiboData = pd.read_sql(sql, conn)

            # 获取权重最大的博文，权重=转发量*70% + 评论*20% + 点赞*10%
            weiboContent = weiboData.iloc[weiboData['likeNum'].idxmax(), 4]
            # 处理博文内容
            weibo_introduction['weiboContent'] = surplus.sub('', weiboContent)
            # 博文时间
            weibo_introduction['weiboTime'] = weiboData.iloc[weiboData['likeNum'].idxmax(), 5]
            return weibo_introduction
    finally:
        conn.close()

'''
>>总览模块<<
函数名：get_weiboOverview
参数：hId: 话题的唯一标识ID
作用: 获取话题的总体信息
返回值：weibo_overView,包含博文的内容、博文时间、转发量、点赞量、评论量、博文量。字典类型
'''
def get_weiboOverview(hId):
    # 正则表达式，对话题的内容进行清洗
    surplus = re.compile('【(.*)】')
    # 返回字典
    weibo_overView = {}

    # 连接数据库，后期可以改为MongoDB的
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            # 筛选条件：topic,话题ID
            sql = "SELECT * FROM weiboreach_weibopost where topic='{}'".format(hId)
            cur.execute(sql)
            # 获取数据，并转化为DataFrame
            weiboData = pd.read_sql(sql, conn)

            # 获取权重最大的博文，权重=转发量*70% + 评论*20% + 点赞*10%
            weiboContent = weiboData.iloc[weiboData['likeNum'].idxmax(), 4]
            # 处理博文内容
            weibo_overView['weiboContent'] = surplus.sub('', weiboContent)
            # 博文时间
            weibo_overView['weiboTime'] = weiboData.iloc[weiboData['likeNum'].idxmax(), 5]
            # 转发量
            weibo_overView['weiboRepostSum'] = weiboData['repostNum'].sum()
            # 点赞量
            weibo_overView['weiboLikeSum'] = weiboData['repostNum'].sum()
            # 评论量
            weibo_overView['weiboCommentSum'] = weiboData['commentNum'].sum()
            # 博文量
            weibo_overView['weiboPostSum'] = weiboData.shape[0]

            # 整体指标
            weibo_overView['weiboContentEvaluation'] = int(((weibo_overView['weiboRepostSum'] * 0.5 + weibo_overView['weiboCommentSum'] * 0.4 + weibo_overView['weiboLikeSum'] * 0.2)/(weibo_overView['weiboRepostSum'] + \
                                                                        weibo_overView['weiboCommentSum'] + weibo_overView['weiboLikeSum'])) * 100)
            return weibo_overView
    finally:
        conn.close()
def get_overallIndicators():
    weibo_overall = {}
    fans_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM weiboreach_information"
            cur.execute(sql)
            userinfoData = pd.read_sql(sql, conn)
            # 获取认证信息
            BasicInfo = userinfoData[['authentication', 'gender', 'fansNum']]
            BasicInfo = BasicInfo.replace(to_replace=r'^\s*$', value=np.nan, regex=True)
            # 1. 未认证数量
            unauthenSum = BasicInfo['authentication'].isna().sum()
            # 认证比例
            authen_ratio = int(((BasicInfo.shape[0] - unauthenSum)/BasicInfo.shape[0])*100)
            weibo_overall['authen_ratio'] = authen_ratio

            # 粉丝质量
            fans100 = BasicInfo['fansNum'][BasicInfo['fansNum'] < 100].count()
            fans_list.append(fans100)
            # print(fans100)
            fans1000 = BasicInfo['fansNum'][(BasicInfo['fansNum'] >= 100) & (BasicInfo['fansNum'] < 1000)].count()
            fans_list.append(fans1000)
            # print(fans1000)
            fans10000 = BasicInfo['fansNum'][(BasicInfo['fansNum'] >= 1000) & (BasicInfo['fansNum'] < 10000)].count()
            fans_list.append(fans10000)
            # print(fans10000)
            fans100000 = BasicInfo['fansNum'][(BasicInfo['fansNum'] >= 10000) & (BasicInfo['fansNum'] < 100000)].count()
            fans_list.append(fans100000)
            # print(fans100000)
            fans1000000 = BasicInfo['fansNum'][(BasicInfo['fansNum'] >= 100000) & (BasicInfo['fansNum'] < 1000000)].count()
            fans_list.append(fans1000000)
            # print(fans1000000)
            fansmore = BasicInfo['fansNum'][BasicInfo['fansNum'] >= 1000000].count()
            fans_list.append(fansmore)
            # 求权重
            func = lambda x, y: x * y
            fans_weight = map(func, [0.05, 0.1, 0.15, 0.2, 0.2, 0.3], fans_list)
            fans_ratio = int((sum(fans_weight)/sum(fans_list)) * 100)

            weibo_overall['fans_ratio'] = fans_ratio
            return weibo_overall

    finally:
        conn.close()
'''
>>热度趋势模块<<
函数名：get_hotTrend
参数：无
作用：获取热度趋势图数据
返回值：weiboTrend，包含时间序列和对应的值。字典类型
'''
def get_hotTrend(key):
    weiboTrend = []
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM weiboreach_repost"
            cur.execute(sql)
            # 读取转发数据
            repostData = pd.read_sql(sql, conn)
            repostData = repostData[['createdAt', 'repostUserId']]
            repostData['createdAt'] = pd.to_datetime(repostData['createdAt'])
            repostData.set_index('createdAt', inplace=True)
            if key == '1':
                repostData = repostData.resample('5H').count()['repostUserId']
                repost_index = repostData.index
                repost_index = [i.strftime('%Y-%m-%d %H:%M') for i in repost_index]
                # repost_data = repostData.values
                # repost_data = [i for i in repost_data]
                # weiboTrend['trendTime'] = repost_index
                # weiboTrend['trendData'] = repost_data
                repost_data = {'time': repost_index, 'data': repostData.values}
                repost_data = pd.DataFrame(repost_data)

                for index, row in repost_data.iterrows():
                    each_dict = {}
                    each_dict['x'] = row['time']
                    each_dict['y'] = row['data']
                    weiboTrend.append(each_dict)
                    del each_dict
            else:
                repostData = repostData.resample('10H').count()['repostUserId']
                repost_index = repostData.index
                repost_index = [i.strftime('%Y-%m-%d %H:%M') for i in repost_index]
                # repost_data = repostData.values
                # repost_data = [i for i in repost_data]
                # weiboTrend['trendTime'] = repost_index
                # weiboTrend['trendData'] = repost_data
                repost_data = {'time': repost_index, 'data': repostData.values}
                repost_data = pd.DataFrame(repost_data)

                for index, row in repost_data.iterrows():
                    each_dict = {}
                    each_dict['x'] = row['time']
                    each_dict['y'] = row['data']
                    weiboTrend.append(each_dict)
                    del each_dict
            # print(weiboTrend)
            return weiboTrend
    finally:
        conn.close()
'''
>>热度趋势模块<<
函数名：get_optionLeaders
参数：无
作用：获取top10影响力博主
返回值：weibo_optionLeaders，包含昵称、粉丝数和发博量，字典类型
'''
def get_optionLeaders():
    # 连接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')

    try:
        with conn.cursor() as cur:
            # 筛选条件：topic,话题ID
            sql = "SELECT * FROM weiboreach_repost where repostLevel=1"
            cur.execute(sql)
            # 获取数据，并转化为DataFrame
            repostLevel = pd.read_sql(sql, conn)
            repostLevel = repostLevel[['repostLevel', 'repostUserId']]

            sql = "SELECT * FROM weiboreach_information"
            cur.execute(sql)
            # 获取数据，并转化为DataFrame
            userInformation = pd.read_sql(sql, conn)
            userInformation = userInformation[['InfoId', 'nickName', 'fansNum', 'weiboNum']]
            repost_user = repostLevel.merge(userInformation, left_on='repostUserId', right_on='InfoId', how='left')
            influence_user = repost_user.sort_values(by='fansNum', ascending=False)[:9]

            weibo_optionLeaders = {}
            optionLeaders = []
            for index, row in influence_user.iterrows():
                eachLeader = {}
                # eachLeader['profile'] = 'www.baidu.com'
                eachLeader['username'] = row['nickName']
                eachLeader['fansNum'] = row['fansNum']
                eachLeader['weiboNum'] = row['weiboNum']
                optionLeaders.append(eachLeader)
                del eachLeader
            weibo_optionLeaders['optionLeaders'] = optionLeaders
            return weibo_optionLeaders

    finally:
        conn.close()

'''
>>影响力模块<<
函数名：get_influenceLeaders
参数：无
作用：获取top10影响力博主（以粉丝数量为判断标准）
返回值：weibo_influenceLeaders，包含昵称和粉丝数。字典类型
'''
def get_influenceLeaders():
    # 连接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')

    try:
        with conn.cursor() as cur:
            # 筛选条件：topic,话题ID
            sql = "SELECT * FROM weiboreach_repost where repostLevel=1"
            cur.execute(sql)
            # 获取数据，并转化为DataFrame
            repostLevel = pd.read_sql(sql, conn)
            repostLevel = repostLevel[['repostLevel', 'repostUserId']]

            sql = "SELECT * FROM weiboreach_information"
            cur.execute(sql)
            # 获取数据，并转化为DataFrame
            userInformation = pd.read_sql(sql, conn)
            userInformation = userInformation[['InfoId', 'nickName', 'fansNum', 'weiboNum']]
            repost_user = repostLevel.merge(userInformation, left_on='repostUserId', right_on='InfoId', how='left')
            influence_user = repost_user.sort_values(by='fansNum', ascending=False)[:10]

            weibo_influenceLeaders = {}
            influenceLeaders = ['引爆点']
            fansNum = [0]
            for index, row in influence_user.iterrows():
                influenceLeaders.append(row['nickName'])
                fansNum.append(row['fansNum'])
            weibo_influenceLeaders['influenceLeaders'] = influenceLeaders
            weibo_influenceLeaders['fansNum'] = fansNum
            return weibo_influenceLeaders

    finally:
        conn.close()
'''
>>影响力模块<<
函数名：get_leaderRelation
参数：无
作用：显示转发关系
'''
def get_leaderRelation():
    tree_dict = {}
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM weiboreach_repost"
            cur.execute(sql)
            # 读取转发数据
            repostData = pd.read_sql(sql, conn)

            # 读取用户数据
            sql = "SELECT * FROM weiboreach_information"
            cur.execute(sql)
            # 读取用户数据
            userInfoData = pd.read_sql(sql, conn)
            userInfoData = userInfoData[['InfoId', 'nickName', 'fansNum']]

            # 获取转发1次和2次的数据
            repostData_1 = repostData[repostData['repostLevel'] == 1][['repostUrl', 'createdAt', 'repostUserId']]
            repostData_2 = repostData[repostData['repostLevel'] == 2]

            repost_1_user = repostData_1.merge(userInfoData, left_on='repostUserId', right_on='InfoId', how='left')
            repost_2_user = repostData_2.merge(userInfoData, left_on='repostUserId', right_on='InfoId', how='left')
            group = repostData_2.groupby(by='weiboUrl').count()['RepostId'].sort_values(ascending=False)[:10]
            group.index.name = 'weiboUrl'
            group = group.reset_index()
            repost_12 = group.merge(repost_1_user, left_on='weiboUrl', right_on='repostUrl', how='left')
            tree_dict['name'] = 'Leader'
            sub0_list = []
            for index, row in repost_12.iterrows():
                sub1_dict = {}
                sub1_dict['name'] = row['nickName']
                repost_2_each = repost_2_user[repost_2_user['weiboUrl'] == row['repostUrl']]
                sub1_list = []
                for index, row in repost_2_each.iterrows():
                    sub2_dict = {}
                    sub2_dict['name'] = row['nickName']
                    sub2_dict['value'] = row['fansNum']
                    sub1_list.append(sub2_dict)
                    del sub2_dict
                sub1_dict['children'] = sub1_list
                sub0_list.append(sub1_dict)
                del sub1_dict
            tree_dict['children'] = sub0_list
            return tree_dict
    finally:
        conn.close()
'''
>>参与者分析模块<<
函数名：get_UserInfo
参数：无
作用：获取参与者地域分布、微博认证比例、男女比例、粉丝质量以及设备比例信息
返回值：all_dict，字典类型
'''
def get_UserInfo():
    all_dict = {}
    authen_list = []
    gender_list = []
    fans_list = []
    tool_list = []
    position_list = []
    province_all = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南',
                    '四川', '贵州', '云南', '陕西', '甘肃', '青海', '台湾',
                    '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重庆', '香港', '澳门', '南海诸岛']
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM weiboreach_information"
            cur.execute(sql)
            userinfoData = pd.read_sql(sql, conn)

            # 发布设备
            # 读取转发数据
            sql = "SELECT tool FROM weiboreach_repost"
            cur.execute(sql)
            repost_tool = pd.read_sql(sql, conn)

            # 读取博文数据
            sql = "SELECT tool FROM weiboreach_weibopost"
            cur.execute(sql)
            post_tool = pd.read_sql(sql, conn)

            # 连接两个表
            toolInfo = pd.concat([repost_tool, post_tool], ignore_index=True)
            # iPhone客户端
            iPhoneSum = toolInfo['tool'].str.contains('iPhone').sum()
            tool_dict = {}
            tool_dict["name"] = 'iPhone客户端'
            tool_dict["value"] = iPhoneSum
            tool_list.append(tool_dict)
            del tool_dict

            # 安卓客户端
            androidSum = toolInfo.shape[0] - iPhoneSum
            tool_dict = {}
            tool_dict["name"] = 'Android'
            tool_dict["value"] = androidSum
            tool_list.append(tool_dict)
            all_dict['tool'] = tool_list
            del tool_dict

            # 获取认证信息
            BasicInfo = userinfoData[['authentication', 'gender', 'fansNum']]
            BasicInfo = BasicInfo.replace(to_replace=r'^\s*$', value=np.nan, regex=True)
            # authen_kinds = ['官方认证', '知名博主', '普通认证', '未认证']
            # 1. 未认证数量
            unauthenSum = BasicInfo['authentication'].isna().sum()
            authen_dict = {}
            authen_dict["name"] = '未认证'
            authen_dict["value"] = unauthenSum
            authen_list.append(authen_dict)
            del authen_dict
            # 2. 官方认证数量
            office_authenSum = BasicInfo['authentication'].str.contains('官方').sum()
            authen_dict = {}
            authen_dict["name"] = '官方认证'
            authen_dict["value"] = office_authenSum
            authen_list.append(authen_dict)
            del authen_dict
            # 3. 知名博主
            famous_bloggerSum = BasicInfo['authentication'].str.contains('博主|超话', regex=True).sum()
            authen_dict = {}
            authen_dict["name"] = '知名博主'
            authen_dict["value"] = famous_bloggerSum
            authen_list.append(authen_dict)
            del authen_dict
            # 4. 普通认证
            normal_authenSum = BasicInfo.shape[0] - unauthenSum - office_authenSum - famous_bloggerSum
            authen_dict = {}
            authen_dict["name"] = '普通认证'
            authen_dict["value"] = normal_authenSum
            authen_list.append(authen_dict)
            all_dict['authen'] = authen_list
            del authen_dict

            # 性别信息
            femaleSum = BasicInfo['gender'].str.contains('女', regex=True).sum()
            gender_dict = {}
            gender_dict["name"] = '女'
            gender_dict["value"] = femaleSum
            gender_list.append(gender_dict)
            del gender_dict

            maleSum = BasicInfo['gender'].str.contains('男', regex=True).sum()
            gender_dict = {}
            gender_dict["name"] = '男'
            gender_dict["value"] = maleSum
            gender_list.append(gender_dict)
            del gender_dict
            # print(gender_list)
            all_dict['gender'] = gender_list

            # 粉丝质量
            fans100 = BasicInfo['fansNum'][BasicInfo['fansNum'] < 100].count()
            fans_dict = {}
            fans_dict['name'] = '0~99'
            fans_dict['value'] = fans100
            fans_list.append(fans_dict)
            del fans_dict
            # print(fans100)
            fans1000 = BasicInfo['fansNum'][(BasicInfo['fansNum'] >= 100) & (BasicInfo['fansNum'] < 1000)].count()
            fans_dict = {}
            fans_dict['name'] = '100~999'
            fans_dict['value'] = fans1000
            fans_list.append(fans_dict)
            del fans_dict
            # print(fans1000)
            fans10000 = BasicInfo['fansNum'][(BasicInfo['fansNum'] >= 1000) & (BasicInfo['fansNum'] < 10000)].count()
            fans_dict = {}
            fans_dict['name'] = '1000~9999'
            fans_dict['value'] = fans10000
            fans_list.append(fans_dict)
            del fans_dict
            # print(fans10000)
            fans100000 = BasicInfo['fansNum'][(BasicInfo['fansNum'] >= 10000) & (BasicInfo['fansNum'] < 100000)].count()
            fans_dict = {}
            fans_dict['name'] = '10000~99999'
            fans_dict['value'] = fans100000
            fans_list.append(fans_dict)
            del fans_dict
            # print(fans100000)
            fans1000000 = BasicInfo['fansNum'][(BasicInfo['fansNum'] >= 100000) & (BasicInfo['fansNum'] < 1000000)].count()
            fans_dict = {}
            fans_dict['name'] = '100000~999999'
            fans_dict['value'] = fans1000000
            fans_list.append(fans_dict)
            del fans_dict
            # print(fans1000000)
            fansmore = BasicInfo['fansNum'][BasicInfo['fansNum'] >= 1000000].count()
            fans_dict = {}
            fans_dict['name'] = '>=1000000'
            fans_dict['value'] = fansmore
            fans_list.append(fans_dict)
            del fans_dict
            # for eachfans in fans_list
            all_dict['fans'] = fans_list

            # 地域分布
            res_position = userinfoData['province'].groupby(userinfoData['province']).count()
            res_position.index.name = 'pos'
            res_position = res_position.reset_index()
            # 处理其他和海外的用户
            # res_position = res_position.replace(to_replace=r'^\s*$|其他|海外', value=np.nan, regex=True)
            # res_position = res_position.replace(to_replace=r'海外', value=np.nan, regex=True)
            # res_position.dropna(subset=['pos'], inplace=True)
            res_position.sort_values("province", inplace=True, ascending=False)
            for item in res_position.values:
                if item[0] in province_all:
                    dict_position = {}
                    province_all.remove(item[0])
                    dict_position["name"] = item[0]
                    dict_position["value"] = item[1]
                    position_list.append(dict_position)
                    del dict_position
            for item in province_all:
                dict_position = {}
                dict_position["name"] = item
                dict_position["value"] = 0
                position_list.append(dict_position)
                del dict_position
            all_dict['position'] = position_list
            return all_dict

    finally:
        conn.close()
'''
>>内容分析模块<<
函数名：get_titleLeaders
参数“无
作用：话题领袖，获取二次转发量Top5用户的昵称，粉丝数，微博URL,二次转发量以及转发时间
返回值：weibo_titleLeaders，字典类型
'''
def get_titleLeaders():
    weibo_titleLeaders = {}
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            sql = "SELECT * FROM weiboreach_repost"
            cur.execute(sql)
            # 读取转发数据
            repostData = pd.read_sql(sql, conn)

            # 读取用户数据
            sql = "SELECT * FROM weiboreach_information"
            cur.execute(sql)
            # 读取用户数据
            userInfoData = pd.read_sql(sql, conn)
            userInfoData = userInfoData[['InfoId', 'nickName', 'fansNum']]

            # 获取转发1次和2次的数据
            repostData_1 = repostData[repostData['repostLevel'] == 1][['repostUrl', 'createdAt', 'repostUserId']]
            repostData_2 = repostData[repostData['repostLevel'] == 2]

            group = repostData_2.groupby(by='weiboUrl').count()['RepostId'].sort_values(ascending=False)[:10]
            # weiboUrl = group.index
            # repostCount = group.values
            group.index.name = 'weiboUrl'
            group = group.reset_index()

            repost_12 = group.merge(repostData_1, left_on='weiboUrl', right_on='repostUrl', how='left')
            repost_user = repost_12.merge(userInfoData, left_on='repostUserId', right_on='InfoId', how='left')

            titleLeaders = []
            for index, row in repost_user.iterrows():
                eachLeader = {}
                eachLeader['nickName'] = row['nickName']
                eachLeader['fansNum'] = row['fansNum']
                eachLeader['weiboUrl'] = row['weiboUrl']
                eachLeader['repostCount'] = row['RepostId']
                eachLeader['createdAt'] = row['createdAt']
                titleLeaders.append(eachLeader)
                del eachLeader
            weibo_titleLeaders['titleLeaders'] = titleLeaders
            return weibo_titleLeaders
    finally:
        conn.close()

'''
>>内容分析模块<<
函数名：filter_emoji
参数：desstr:预处理的文本；restr:空字符串
作用：处理Emoji表情。将文本中的Emoji表情清除掉
返回值：不带Emoji表情的文本。字符串类型
'''
def filter_emoji(desstr,restr=''):
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

'''
>>内容分析模块<<
函数名：get_KeyWord
参数：无
作用：统计评论信息的热门词汇并生成词云图
返回值：list_word。词汇和所出现的数量。字典类型
'''
def get_KeyWord():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Www.13720147676', charset='utf8mb4',
                           db='weiboDB')
    try:
        with conn.cursor() as cur:
            sql_comment = "SELECT * FROM weiboreach_comment"
            cur.execute(sql_comment)
            commentData = pd.read_sql(sql_comment, conn)
            # commentData['content'].values
            commentText = '.'.join(commentData['content'].values)
            commentText = filter_emoji(commentText)
            commentText = ''.join(re.findall(r'[\u4e00-\u9fa5]', commentText))
            # commentText = re.sub(r"\[\S+\]", "", commentText)  # 去除表情符号
            result = jieba.cut(commentText)
            # stopwords = restopwords()
            stopwords = open(STATICFILES_DIRS[0]+'/dataAnalysis/hit_stopwords.txt', encoding='utf-8').read()
            stopwords = stopwords.split('\n')

            allwords = [word for word in result if len(word) > 1 and word not in stopwords]
            # allwords = [word for word in result if len(word) > 1]
            res = pd.DataFrame(allwords, columns=['word'])
            res = res['word'].groupby(res['word']).count()
            res.index.name = 'txt'
            res = res.reset_index()
            res = res[res['word'] > 10].reset_index(drop=True)
            list_word = []
            for item in res.values:
                dict_word = {}
                dict_word["name"] = item[0]
                dict_word["value"] = item[1]
                list_word.append(dict_word)
            return list_word

    finally:
        conn.close()
