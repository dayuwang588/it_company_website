from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product

def product_list(request):
    """
    产品列表页：展示所有启用的产品，支持按分类筛选
    核心逻辑：查询分类 + 筛选产品 → 构造上下文 → 渲染模板
    """
    # 1. 查询所有产品分类（按sort排序）
    categories = ProductCategory.objects.all().order_by('sort')
    
    # 2. 查询所有启用的产品（按创建时间倒序）
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    
    # 3. 按分类筛选产品（URL传参?category_id=xxx）
    category_id = request.GET.get('category_id')
    if category_id and category_id.isdigit():
        products = products.filter(category_id=category_id)
    
    # 4. 构造模板上下文
    context = {
        "categories": categories,  # 所有产品分类（用于筛选）
        "products": products,      # 筛选后的产品列表
        "selected_category_id": category_id,  # 当前选中的分类ID（用于高亮）
        "page_title": "产品中心 - 我们的产品与解决方案"
    }
    
    # 5. 渲染模板
    return render(request, 'product/product_list.html', context)

def product_detail(request, product_id):
    """
    产品详情页：展示单个产品的完整信息
    适配URL传参，无数据/未启用则返回404
    """
    # 1. 查询指定ID的启用产品，无数据则404
    product = get_object_or_404(Product, id=product_id, is_active=True)
    
    # 2. 推荐产品：同分类的其他启用产品（排除当前产品，取前3个）
    recommend_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product_id)[:3]
    
    # 3. 构造上下文
    context = {
        "product": product,              # 当前产品详情
        "recommend_products": recommend_products,  # 同分类推荐产品
        "page_title": f"{product.title} - 产品详情"
    }
    
    # 4. 渲染模板
    return render(request, 'product/product_detail.html', context)