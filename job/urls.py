
from django.urls import path
from . import views

# 定义应用命名空间，便于跨应用反向解析
app_name = 'job'

urlpatterns = [
    # 招聘列表页：访问 /job/
    path('', views.job_list, name='job_list'),
    # 岗位详情页：访问 /job/detail/1/
    path('detail/<int:job_id>/', views.job_detail, name='job_detail'),
]