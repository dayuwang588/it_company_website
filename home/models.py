from django.db import models

# Create your models here.
class Banner(models.Model):
    """首页轮播图"""
    title = models.CharField(max_length=100, verbose_name="轮播标题")
    image = models.ImageField(upload_to="banner/", verbose_name="轮播图片")  # 图片上传到media/banner/
    link = models.URLField(blank=True, null=True, verbose_name="跳转链接")
    is_active = models.BooleanField(default=True, verbose_name="是否启用")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"  # 后台显示复数名称
        ordering = ["-created_at"]  # 按创建时间倒序

    def __str__(self):
        return self.title

class Advantage(models.Model):
    """核心优势"""
    icon = models.CharField(max_length=50, verbose_name="图标类名(Font Awesome)")
    title = models.CharField(max_length=50, verbose_name="优势标题")
    desc = models.TextField(verbose_name="优势描述")
    sort = models.IntegerField(default=0, verbose_name="排序序号")

    class Meta:
        verbose_name = "核心优势"
        verbose_name_plural = "核心优势"
        ordering = ["sort"]

    def __str__(self):
        return self.title

class Partner(models.Model):
    """合作伙伴"""
    name = models.CharField(max_length=50, verbose_name="合作方名称")
    logo = models.ImageField(upload_to="partner/", verbose_name="合作方logo")
    link = models.URLField(blank=True, null=True, verbose_name="官网链接")

    class Meta:
        verbose_name = "合作伙伴"
        verbose_name_plural = "合作伙伴"

    def __str__(self):
        return self.name
