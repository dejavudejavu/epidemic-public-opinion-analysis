from django.db import models

class HotTopicInfo(models.Model):
    hotIndex = models.IntegerField(default=-1)
    hotLink = models.CharField(max_length=300)
    hotTitle = models.CharField(max_length=50)
    hotReadNum = models.IntegerField(default=0)

# 博文信息
class WeiboPost(models.Model):
    PostId = models.CharField(max_length=30)
    topic = models.CharField(max_length=50)
    weiboUrl = models.CharField(max_length=50)
    content = models.TextField()
    createdAt = models.CharField(max_length=20)
    tool = models.CharField(max_length=30)
    crawlTime = models.IntegerField(default=0)
    userId = models.CharField(max_length=20)
    repostNum = models.IntegerField(default=0)
    likeNum = models.IntegerField(default=0)
    commentNum = models.IntegerField(default=0)
    isRepost = models.IntegerField(default=0)
    originWeibo = models.CharField(max_length=50, default="")

class Repost(models.Model):
    RepostId = models.CharField(max_length=30)
    crawlTime = models.IntegerField(default=0)
    weiboUrl = models.CharField(max_length=50)
    repostUrl = models.CharField(max_length=50)
    content = models.TextField()
    tool = models.CharField(max_length=30)
    createdAt = models.CharField(max_length=20)
    likeNum = models.IntegerField(default=0)
    repostLevel = models.IntegerField(default=0)
    repostUserId = models.CharField(max_length=20)

class Information(models.Model):
    InfoId = models.CharField(max_length=20)
    crawlTime = models.IntegerField(default=0)
    personUrl = models.CharField(max_length=50)
    nickName = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    province = models.CharField(max_length=5)
    city = models.CharField(max_length=10)
    # briefIntroduction = models.TextField()
    birthday = models.CharField(max_length=15)
    vipLevel = models.CharField(max_length=10)
    authentication = models.CharField(max_length=100)
    weiboNum = models.IntegerField(default=0)
    followsNum = models.IntegerField(default=0)
    fansNum = models.IntegerField(default=0)

class Comment(models.Model):
    CommentId = models.CharField(max_length=20)
    crawlTime = models.IntegerField(default=0)
    weiboUrl = models.CharField(max_length=50)
    commentUserId = models.CharField(max_length=20)
    content = models.TextField()
    createdAt = models.CharField(max_length=20)
    likeNum = models.IntegerField(default=0)
    tool = models.CharField(max_length=30)






























