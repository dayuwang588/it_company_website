from django.contrib import admin
from .models import Team  

# 团队成员管理
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'avatar_preview', 'sort')
    search_fields = ('name', 'position', 'desc')
    list_filter = ('position',)
    ordering = ('sort',)
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        if obj.avatar:
            return f'<img src="{obj.avatar.url}" width="80" height="80" style="border-radius: 50%;" />'
        return "无头像"
    avatar_preview.short_description = "头像预览"
    avatar_preview.allow_tags = True

