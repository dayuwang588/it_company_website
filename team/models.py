from django.db import models

# Create your models here.
class Team(models.Model):
    """团队成员"""
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="team/")
    desc = models.TextField()
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ["sort"]
        verbose_name = "团队成员"
        verbose_name_plural = "团队成员"

    def __str__(self):
        return self.name