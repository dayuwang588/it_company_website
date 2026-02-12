from django.contrib import admin

from .models import ContactInfo, ContactMessage

# 公司联系方式（单条数据即可）
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'qrcode_preview')
    search_fields = ('name', 'phone', 'email')
    readonly_fields = ('qrcode_preview',)

    def qrcode_preview(self, obj):
        if obj.qrcode:
            return f'<img src="{obj.qrcode.url}" width="80" height="80" />'
        return "无二维码"
    qrcode_preview.short_description = "二维码预览"
    qrcode_preview.allow_tags = True

# 留言管理（只读，不能修改，只能删除/查看）
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'content_short', 'created_at')
    search_fields = ('name', 'email', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    # 留言是用户提交的，禁止修改
    readonly_fields = ('name', 'email', 'content', 'created_at')
    # 隐藏编辑按钮，只能查看/删除
    actions_on_edit = False

    def content_short(self, obj):
        return obj.content[:30] + "..." if len(obj.content) > 30 else obj.content
    content_short.short_description = "留言内容"
    
