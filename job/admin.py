from django.contrib import admin

from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'salary', 'experience', 'education', 'is_active', 'created_at')
    search_fields = ('title', 'department', 'content')
    list_filter = ('department', 'experience', 'education', 'is_active')
    ordering = ('-created_at',)

    # 自定义薪资显示（突出显示）
    def salary(self, obj):
        return f'<span style="color: red; font-weight: bold;">{obj.salary}</span>'
    salary.short_description = "薪资"
    salary.allow_tags = True
