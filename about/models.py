from django.db import models

# Create your models here.

class About(models.Model):
    """公司简介"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "公司简介"
        verbose_name_plural = "公司简介"

    def __str__(self):
        return self.title

class History(models.Model):
    """发展历程"""
    year = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ["sort"]
        verbose_name = "发展历程"
        verbose_name_plural = "发展历程"

    def __str__(self):
        return f"{self.year} - {self.title}"