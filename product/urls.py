from django.urls import path
from . import views

# 定义应用命名空间，便于跨应用反向解析
app_name = 'product'

urlpatterns = [
    # 产品列表页：访问 /product/
    path('', views.product_list, name='product_list'),
    # 产品详情页：访问 /product/detail/1/
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
]