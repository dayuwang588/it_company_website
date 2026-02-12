from django.db import models

class CaseCategory(models.Model):
    """案例分类模型（如：网站开发、小程序开发、大数据分析）"""
    name = models.CharField('分类名称', max_length=50)
    sort = models.IntegerField('排序（升序）', default=0)
    is_active = models.BooleanField('是否启用', default=True)

    class Meta:
        verbose_name = '案例分类'
        verbose_name_plural = '案例分类'
        ordering = ['sort']

    def __str__(self):
        return self.name

class Case(models.Model):
    """案例核心模型（贴合原示例的字段设计）"""
    title = models.CharField('案例标题', max_length=100)
    category = models.ForeignKey(
        CaseCategory, 
        verbose_name='案例分类',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    cover = models.ImageField('案例封面', upload_to='case/covers/', blank=True)
    client = models.CharField('客户名称', max_length=100, blank=True)
    desc = models.TextField('案例简介')
    content = models.TextField('案例详情')
    is_active = models.BooleanField('是否启用', default=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '案例'
        verbose_name_plural = '案例'
        ordering = ['-created_at']

    def __str__(self):
        return self.title