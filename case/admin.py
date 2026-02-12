from django.contrib import admin
from .models import Case

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'image_preview', 'created_at')
    search_fields = ('title', 'client', 'desc', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="80" />'
        return "无图片"
    image_preview.short_description = "案例图片"
    image_preview.allow_tags = True

