from django.urls import path, re_path
from weiboreach import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('main/', views.main, name='main'),
    re_path(r'overView/(#.*#)', views.overView, name='overView'),
    re_path(r'hotAnalysis/(#.*#)', views.hotAnalysis, name='hotAnalysis'),
    re_path(r'path/(#.*#)', views.pathAnalysis, name='pathAnalysis'),
    re_path(r'userinfo/(#.*#)', views.userInfoAnalysis, name='userInfoAnalysis'),
    re_path(r'influence/(#.*#)', views.influenceAnalysis, name='influenceAnalysis'),
    re_path(r'content/(#.*#)', views.contentAnalysis, name='contentAnalysis'),
    re_path(r'rumour/(#.*#)', views.rumourDetection, name='rumourDetection'),
    re_path(r'rumourDate/(\d+)', views.rumourDateSeries, name='rumourDateSeries'),
    path('leaderRelation/', views.leaderRelation, name='leaderRelation'),
    path('bwx/', views.bwx, name='bwx'),
]