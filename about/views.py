from django.shortcuts import render, get_object_or_404
from .models import About, History

def about_index(request):
    """
    关于我们首页：展示公司简介 + 发展历程
    核心逻辑：查询数据 → 构造上下文 → 渲染模板
    """
    # 1. 查询公司简介（取最新的一条，无则返回空）
    try:
        about_info = About.objects.order_by('-updated_at').first()
    except:
        about_info = None
    
    # 2. 查询发展历程（按sort字段排序）
    history_list = History.objects.all().order_by('sort')
    
    # 3. 构造模板上下文数据
    context = {
        "about_info": about_info,  # 公司简介
        "history_list": history_list,  # 发展历程
    }
    
    # 4. 渲染模板并返回
    return render(request, 'about/about_index.html', context)

def about_detail(request, about_id):
    """
    公司简介详情页（扩展功能）：展示单条简介的完整信息
    适配URL传参，无数据时返回404
    """
    # 查询指定ID的公司简介，无数据则返回404
    about_info = get_object_or_404(About, id=about_id)
    # 同时查询发展历程（用于详情页侧边展示）
    history_list = History.objects.all().order_by('sort')
    
    context = {
        "about_info": about_info,
        "history_list": history_list,
    }
    return render(request, 'about/about_detail.html', context)
