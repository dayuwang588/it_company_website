
from django.urls import path
from . import views

# 定义应用命名空间，便于跨应用反向解析
app_name = 'news'

urlpatterns = [
    # 新闻列表页：访问 /news/
    path('', views.news_list, name='news_list'),
    # 新闻详情页：访问 /news/detail/1/
    path('detail/<int:news_id>/', views.news_detail, name='news_detail'),
]