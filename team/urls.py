from django.urls import path
from . import views

# 定义应用命名空间，便于跨应用反向解析
app_name = 'team'

urlpatterns = [
    # 团队列表页：访问 /team/
    path('', views.team_list, name='team_list'),
    # 成员详情页：访问 /team/detail/1/
    path('detail/<int:member_id>/', views.team_detail, name='team_detail'),
]