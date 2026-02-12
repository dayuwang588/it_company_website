
from django.shortcuts import render, get_object_or_404
from .models import Case, CaseCategory  # 补充案例分类模型（可选，增强实用性）

# 案例列表页视图（对应原示例的index逻辑）
def case_list(request):
    """案例列表页面：展示所有启用的案例，支持按分类筛选"""
    # 获取所有启用的案例（按创建时间倒序）
    cases = Case.objects.filter(is_active=True).order_by('-created_at')
    # 获取所有案例分类（用于筛选）
    categories = CaseCategory.objects.all()
    
    # 可选：按分类筛选案例（URL传参?category_id=xxx）
    category_id = request.GET.get('category_id')
    if category_id and category_id.isdigit():
        cases = cases.filter(category_id=category_id)
    
    # 构造上下文数据（贴合原示例的简洁风格）
    context = {
        "cases": cases,
        "categories": categories,
    }
    # 渲染案例列表模板
    return render(request, 'case/case_list.html', context)

# 案例详情页视图
def case_detail(request, case_id):
    """案例详情页面：展示单个案例的完整信息"""
    # 获取指定ID的启用案例，不存在则返回404
    case = get_object_or_404(Case, id=case_id, is_active=True)
    # 获取相关案例（同分类的其他启用案例，排除当前案例）
    related_cases = Case.objects.filter(
        category=case.category, 
        is_active=True
    ).exclude(id=case_id)[:3]  # 仅展示3个相关案例
    
    # 构造上下文数据
    context = {
        "case": case,
        "related_cases": related_cases,
    }
    # 渲染案例详情模板
    return render(request, 'case/case_detail.html', context)