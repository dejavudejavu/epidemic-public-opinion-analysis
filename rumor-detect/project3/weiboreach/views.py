from django.shortcuts import render
from django.http import JsonResponse
from weiboreach.models import *
from weiboreach.dataAnalysis import *
from weiboreach.PosNegWord.posNegWord import get_PosNegWord
from weiboreach.textTrank.TextRank4Sentence_test import TextRank
import json
# 热搜榜----首页
def index(request):
    hotlist = HotTopicInfo.objects.all()[:10]
    context = {'hotlist': hotlist}
    return render(request, 'weiboreach/index.html', context)

# 测试页面
def main(request):
    return render(request, 'weiboreach/main.html')

# 总览模块
def overView(request, hId):
    # 后期修改为话题的唯一标识
    hId = '#美国新冠肺炎确诊病例超24万#'
    # 获取分析的结果
    weibo_overView = get_weiboOverview(hId)
    weiboContent = TextRank()
    # weiboContent = weibo_overView['weiboContent']
    weiboTime = weibo_overView['weiboTime']
    weiboRepostSum = weibo_overView['weiboRepostSum']
    weiboLikeSum = weibo_overView['weiboLikeSum']
    weiboCommentSum = weibo_overView['weiboCommentSum']
    weiboPostSum = weibo_overView['weiboPostSum']
    # 整体指标：4个方面，内容总评、情感值、用户质量、认证比例
    # weiboContentEvaluation = weibo_overView['weiboContentEvaluation']
    weiboContentEvaluation = weibo_overView['weiboContentEvaluation']
    weibo_overall = get_overallIndicators()
    weiboSentimentVal = 79
    weiboUserQuality = weibo_overall['fans_ratio']
    authenticationRatio = weibo_overall['authen_ratio']
    # 参与人数，筛选出参与该话题的用户，hID
    participantSum = Information.objects.count()

    overallIndex = []
    overallIndex.append(weiboContentEvaluation)
    overallIndex.append(weiboSentimentVal)
    overallIndex.append(weiboUserQuality)
    overallIndex.append(authenticationRatio)

    context = {
        'hId': hId,
        'weiboContent': weiboContent,
        'weiboTime': weiboTime,
        'weiboRepostSum': weiboRepostSum,
        'weiboLikeSum': weiboLikeSum,
        'weiboCommentSum': weiboCommentSum,
        'weiboPostSum': weiboPostSum,
        'participantSum': participantSum,
        'weiboContentEvaluation': weiboContentEvaluation,
        'weiboSentimentVal': weiboSentimentVal,
        'weiboUserQuality': weiboUserQuality,
        'authenticationRatio': authenticationRatio,
        'overallIndex': overallIndex
    }
    return render(request, 'weiboreach/overView.html', context)
# 热度趋势
def hotAnalysis(request, hId):
    weibo_introduction = get_weiboIntroduction(hId)
    weiboContent = TextRank()
    # weiboContent = weibo_introduction['weiboContent']
    weiboTime = weibo_introduction['weiboTime']
    weibo_optionLeaders = get_optionLeaders()
    weiboOptionLeaders = weibo_optionLeaders['optionLeaders']
    context = {
        'hId': hId,
        'weiboContent': weiboContent,
        'weiboTime': weiboTime,
        'weiboOptionLeaders': weiboOptionLeaders,
    }
    return render(request, 'weiboreach/hotAnalysis.html', context)

# 路径分析
def pathAnalysis(request, hId):
    weibo_introduction = get_weiboIntroduction(hId)
    weiboContent = weibo_introduction['weiboContent']
    weiboTime = weibo_introduction['weiboTime']
    context = {
        'hId': hId,
        'weiboContent': weiboContent,
        'weiboTime': weiboTime,
    }
    return render(request, 'weiboreach/pathAnalysis.html', context)

# 用户分析
def userInfoAnalysis(request, hId):
    weibo_overView = get_weiboOverview(hId)
    weiboContent = TextRank()
    # weiboContent = weibo_overView['weiboContent']
    weiboTime = weibo_overView['weiboTime']
    all_dict = get_UserInfo()
    genderratio = all_dict['gender']
    authratio = all_dict['authen']
    position = all_dict['position']
    fans = all_dict['fans']
    tool = all_dict['tool']
    context = {
        'hId': hId,
        'genderratio': genderratio,
        'authratio': authratio,
        'weiboContent': weiboContent,
        'weiboTime': weiboTime,
        'position': position,
        'fans': fans,
        'tool': tool,
    }
    return render(request, 'weiboreach/userInfoAnalysis.html', context)

# 影响力分析
def influenceAnalysis(request, hId):
    weibo_introduction = get_weiboIntroduction(hId)
    weiboContent = TextRank()
    # weiboContent = weibo_introduction['weiboContent']
    weiboTime = weibo_introduction['weiboTime']
    weibo_influenceLeaders = get_influenceLeaders()
    influenceLeaders = weibo_influenceLeaders['influenceLeaders']
    fansNum = weibo_influenceLeaders['fansNum']
    weibo_titleLeaders = get_titleLeaders()
    weiboTitleLeaders = weibo_titleLeaders['titleLeaders']
    context = {
        'hId': hId,
        'weiboContent': weiboContent,
        'weiboTime': weiboTime,
        'influenceLeaders': influenceLeaders,
        'fansNum': fansNum,
        'weiboTitleLeaders': weiboTitleLeaders,
    }
    return render(request, 'weiboreach/influenceAnalysis.html', context)

# 内容分析
def contentAnalysis(request, hId):
    weibo_overView = get_weiboOverview(hId)
    weiboContent = TextRank()
    # weiboContent = weibo_overView['weiboContent']
    weiboTime = weibo_overView['weiboTime']
    wordcloud = get_KeyWord()
    weiboPosNegWord = get_PosNegWord()
    weiboPosWord = weiboPosNegWord['pos']
    weiboNegWord = weiboPosNegWord['neg']
    context = {
        'wordcloud': json.dumps(wordcloud),
        'hId': hId,
        'weiboContent': weiboContent,
        'weiboTime': weiboTime,
        'weiboPosWord': json.dumps(weiboPosWord),
        'weiboNegWord': json.dumps(weiboNegWord),
    }
    return render(request, 'weiboreach/contentAnalysis.html', context)

# 谣言检测
def rumourDetection(request, hId):
    weibo_overView = get_weiboOverview(hId)
    weiboContent = TextRank()
    # weiboContent = weibo_overView['weiboContent']
    weiboTime = weibo_overView['weiboTime']
    context = {
        'hId': hId,
        'weiboContent': weiboContent,
        'weiboTime': weiboTime
    }
    return render(request, 'weiboreach/rumourDetection.html', context)

def rumourDateSeries(request, key):
    weibo_rumourDateSeries = get_hotTrend(key)
    return JsonResponse({'data': weibo_rumourDateSeries})

def leaderRelation(request):
    weibo_leaderRelation = get_leaderRelation()
    return JsonResponse(weibo_leaderRelation)





