
# contact/forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """联系表单"""
    class Meta:
        model = ContactMessage  # 关联联系信息模型
        fields = ["name", "phone", "email", "content"]  # 表单字段
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入姓名"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "请输入电话"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "请输入邮箱"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "请输入留言内容", "rows": 5}),
        }
        labels = {
            "name": "姓名",
            "phone": "电话",
            "email": "邮箱",
            "content": "留言内容",
        }