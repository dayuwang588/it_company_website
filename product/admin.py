from django.contrib import admin
from .models import ProductCategory, Product

# 产品分类管理
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort')
    search_fields = ('name',)
    ordering = ('sort',)

# 产品管理（关联分类）
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_preview', 'is_active', 'created_at')
    search_fields = ('title', 'desc', 'content')
    list_filter = ('category', 'is_active', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="80" />'
        return "无图片"
    image_preview.short_description = "产品图片"
    image_preview.allow_tags = True

