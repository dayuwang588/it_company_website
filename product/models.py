from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    """产品分类"""
    name = models.CharField(max_length=50)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ["sort"]
        verbose_name = "产品分类"
        verbose_name_plural = "产品分类"

    def __str__(self):
        return self.name

class Product(models.Model):
    """产品"""
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product/")
    desc = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "产品"
        verbose_name_plural = "产品"

    def __str__(self):
        return self.title