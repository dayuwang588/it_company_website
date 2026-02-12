from django.contrib import admin

from .models import About, History

# 公司简介管理
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'image_preview')
    search_fields = ('title', 'content')
    readonly_fields = ('updated_at', 'image_preview')
    # 富文本编辑（需先装 django-tinymce，下文有说明）
    fields = ('title', 'content', 'image', 'updated_at')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="80" />'
        return "无图片"
    image_preview.short_description = "图片预览"
    image_preview.allow_tags = True

# 发展历程管理
@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'sort', 'desc_short')
    search_fields = ('year', 'title')
    list_filter = ('year',)
    ordering = ('sort',)

    def desc_short(self, obj):
        return obj.desc[:20] + "..." if len(obj.desc) > 20 else obj.desc
    desc_short.short_description = "描述"
