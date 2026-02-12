
from django.shortcuts import render
from .models import Banner, Advantage, Partner

def index(request):
    # 获取所有启用的轮播图
    banners = Banner.objects.filter(is_active=True)
    # 获取所有核心优势
    advantages = Advantage.objects.all()
    # 获取所有合作伙伴
    partners = Partner.objects.all()
    # 构造上下文数据
    context = {
        "banners": banners,
        "advantages": advantages,
        "partners": partners,
    }
    # 渲染模板并传递数据
    return render(request, 'index.html', context)