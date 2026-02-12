
from django.urls import path
from . import views

app_name = 'case'

urlpatterns = [
    # 案例列表页
    path('', views.case_list, name='case_list'),
    # 案例详情页（接收case_id参数）
    path('<int:case_id>/', views.case_detail, name='case_detail'),
]