
from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    """
    新闻列表页：展示所有新闻，按「置顶+发布时间」倒序排列
    核心逻辑：查询数据 → 构造上下文 → 渲染模板
    """
    # 查询所有新闻（按置顶、发布时间倒序，匹配模型Meta的排序规则）
    news_list = News.objects.all().order_by("-is_top", "-created_at")
    
    # 构造模板上下文
    context = {
        "news_list": news_list,
        "page_title": "新闻动态 - 公司资讯"
    }
    
    # 渲染新闻列表模板
    return render(request, 'news/news_list.html', context)

def news_detail(request, news_id):
    """
    新闻详情页：展示单条新闻的完整信息
    适配URL传参，无数据则返回404
    """
    # 查询指定ID的新闻，无数据则返回404
    news = get_object_or_404(News, id=news_id)
    
    # 推荐新闻：取置顶/最新的3条其他新闻（排除当前新闻）
    recommend_news = News.objects.exclude(id=news_id).order_by("-is_top", "-created_at")[:3]
    
    # 构造上下文
    context = {
        "news": news,
        "recommend_news": recommend_news,
        "page_title": f"{news.title} - 新闻详情"
    }
    
    # 渲染新闻详情模板
    return render(request, 'news/news_detail.html', context)