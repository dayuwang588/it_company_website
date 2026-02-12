
from django.shortcuts import render, get_object_or_404
from .models import Job

def job_list(request):
    """
    招聘列表页：展示所有启用的招聘岗位，按创建时间倒序排列
    核心逻辑：筛选数据 → 构造上下文 → 渲染模板
    """
    # 查询所有启用的招聘岗位（按创建时间倒序）
    job_list = Job.objects.filter(is_active=True).order_by('-created_at')
    
    # 构造模板上下文
    context = {
        "job_list": job_list,
        "page_title": "人才招聘 - 加入我们"
    }
    
    # 渲染模板
    return render(request, 'job/job_list.html', context)

def job_detail(request, job_id):
    """
    岗位详情页：展示单个招聘岗位的完整信息
    适配URL传参，无数据/未启用则返回404
    """
    # 查询指定ID的启用岗位，无数据则404
    job = get_object_or_404(Job, id=job_id, is_active=True)
    
    # 构造上下文（同时传递推荐岗位：最新的3个其他岗位）
    recommend_jobs = Job.objects.filter(is_active=True).exclude(id=job_id)[:3]
    
    context = {
        "job": job,
        "recommend_jobs": recommend_jobs,
        "page_title": f"{job.title} - 招聘详情"
    }
    
    # 渲染模板
    return render(request, 'job/job_detail.html', context)