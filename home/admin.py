from django.contrib import admin
from .models import Banner, Advantage, Partner
# Register your models here.
# 轮播图管理
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('title', 'image_preview', 'link', 'is_active', 'created_at')
    # 可搜索的字段
    search_fields = ('title',)
    # 可过滤的字段
    list_filter = ('is_active', 'created_at')
    # 默认排序
    ordering = ('-created_at',)
    # 只读字段（创建时间自动生成）
    readonly_fields = ('created_at', 'image_preview')

    # 自定义图片预览（无需点击编辑就能看缩略图）
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="50" />'
        return "无图片"
    image_preview.short_description = "图片预览"
    image_preview.allow_tags = True

# 核心优势管理
@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'sort', 'desc_short')
    search_fields = ('title',)
    list_filter = ('sort',)
    ordering = ('sort',)

    # 自定义短描述（避免列表页文字过长）
    def desc_short(self, obj):
        return obj.desc[:20] + "..." if len(obj.desc) > 20 else obj.desc
    desc_short.short_description = "描述"

# 合作伙伴管理
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_preview', 'link')
    search_fields = ('name',)
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" width="80" height="40" />'
        return "无logo"
    logo_preview.short_description = "LOGO预览"
    logo_preview.allow_tags = True