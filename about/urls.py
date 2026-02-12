
from django.urls import path
from . import views

# 定义应用命名空间，便于跨应用反向解析
app_name = 'about'

urlpatterns = [
    # 关于我们首页：访问 /about/
    path('', views.about_index, name='about_index'),
    # 公司简介详情页：访问 /about/detail/1/
    path('detail/<int:about_id>/', views.about_detail, name='about_detail'),
]