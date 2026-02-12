
# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages  # 用于提示信息
from .models import  ContactMessage

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():  # 表单验证通过
            form.save()  # 保存数据到数据库
            messages.success(request, "留言提交成功，我们将尽快与您联系！")
            return redirect("contact")  # 重定向到联系页面
    else:
        form = ContactForm()  # GET请求，显示空表单
    return render(request, 'contact/contact.html', {"form": form})