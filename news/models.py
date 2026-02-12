
from django.db import models

class News(models.Model):
    """新闻动态模型（公司新闻/行业资讯）"""
    # 新闻标题（必填，最长100字）
    title = models.CharField(max_length=100, verbose_name="新闻标题")
    # 新闻封面图（可选，上传到 news/ 目录）
    image = models.ImageField(
        upload_to="news/", 
        blank=True, 
        null=True, 
        verbose_name="新闻封面图"
    )
    # 新闻正文（必填，长文本）
    content = models.TextField(verbose_name="新闻正文")
    # 发布时间（自动生成，无需手动填写）
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    # 可选：是否置顶（扩展字段，方便后台排序）
    is_top = models.BooleanField(default=False, verbose_name="是否置顶")

    class Meta:
        # 后台显示名称（中文）
        verbose_name = "新闻动态"
        verbose_name_plural = "新闻动态"
        # 默认排序：置顶的在前，最新发布的在前
        ordering = ["-is_top", "-created_at"]

    def __str__(self):
        # 后台列表显示新闻标题（方便识别）
        return self.title

    # 可选：自定义方法 - 截取正文前30字（后台列表预览）
    def content_short(self):
        return self.content[:30] + "..." if len(self.content) > 30 else self.content
    content_short.short_description = "新闻摘要"