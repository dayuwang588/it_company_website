
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static  # 配置媒体文件路由
from home.views import index
from about.views import about_index,about_detail
from product.views import product_list, product_detail
from case.views import case_list, case_detail
from team.views import team_list,team_detail
from news.views import news_list, news_detail
from job.views import job_list, job_detail
from contact.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # 首页路由
    path('tinymce/', include('tinymce.urls')), #富文本
    path('about/', include('about.urls')),  # 关于我们
    path('product/', include('product.urls')),  # 产品服务
    path('case/', include('case.urls')),  # 案例展示
    path('team/', include('team.urls')),  # 团队介绍
    path('news/', include('news.urls')),  # 新闻动态
    path('job/', include('job.urls')),  # 招聘信息
    path('contact/', include('contact.urls')),  # 联系我们
]
# 开发环境配置媒体文件访问（生产环境用Nginx代理）
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
