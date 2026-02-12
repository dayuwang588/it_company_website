
# contact/urls.py 完整正确代码
from django.urls import path
from . import views  # 仅导入views模块，避免循环导入

# 定义应用命名空间（便于反向解析，如 {% url 'contact:contact' %}）
app_name = 'contact'

# 核心：urlpatterns 必须是包含 path() 的列表（可迭代对象）
urlpatterns = [
    # 联系我们页面：访问 /contact/
    path('', views.contact, name='contact'),
]