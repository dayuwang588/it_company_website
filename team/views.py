from django.shortcuts import render, get_object_or_404
from .models import Team

def team_list(request):
    """
    团队成员列表页：展示所有团队成员，按sort字段排序
    核心逻辑：查询数据 → 构造上下文 → 渲染模板
    """
    # 查询所有团队成员（按sort排序，匹配模型Meta的排序规则）
    team_members = Team.objects.all().order_by('sort')
    
    # 构造模板上下文
    context = {
        "team_members": team_members,
        "page_title": "核心团队 - 我们的专业团队"
    }
    
    # 渲染团队列表模板
    return render(request, 'team/team_list.html', context)

def team_detail(request, member_id):
    """
    团队成员详情页：展示单个成员的完整信息
    适配URL传参，无数据则返回404
    """
    # 查询指定ID的团队成员，无数据则返回404
    member = get_object_or_404(Team, id=member_id)
    
    # 构造上下文（同时传递其他团队成员，用于详情页展示团队列表）
    other_members = Team.objects.exclude(id=member_id).order_by('sort')[:5]
    
    context = {
        "member": member,
        "other_members": other_members,
        "page_title": f"{member.name} - {member.position} - 团队详情"
    }
    
    # 渲染成员详情模板
    return render(request, 'team/team_detail.html', context)
