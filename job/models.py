from django.db import models

# Create your models here.
class Job(models.Model):
    """招聘岗位"""
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    num = models.IntegerField(default=1)
    experience = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "招聘岗位"
        verbose_name_plural = "招聘岗位"

    def __str__(self):
        return self.title