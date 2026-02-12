from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    """公司联系方式"""
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    qrcode = models.ImageField(upload_to="contact/", blank=True, null=True)

    class Meta:
        verbose_name = "联系方式"
        verbose_name_plural = "联系方式"

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    """留言"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField('联系电话', max_length=20,default='00000000000')  # 新增phone字段
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "留言"
        verbose_name_plural = "留言"

    def __str__(self):
        return f"{self.name} - {self.email}"