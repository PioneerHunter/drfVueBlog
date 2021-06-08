# 评论模型
from django.db import models
from django.utils import timezone

from article.models import Article
from django.contrib.auth.models import User

class Comment(models.Model):
    # 一对多的作者外键
    author = models.ForeignKey(
        User, # 直接引用对应的模型
        on_delete=models.CASCADE,
        related_name='comments'
    )
    # 一对多的文章外键
    article = models.ForeignKey(
        Article, # 直接引用对应的模型
        on_delete=models.CASCADE,
        related_name='comments'
    )

    # 多级评论，评论模型与自身相关联
    # 一个父评论可以由多个子评论，反过来却不行，因此是用的一对多外键
    parent = models.ForeignKey(
        'self', # 语法限制，只能用self
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='children'
    )

    content = models.TextField() # 评论内容
    created = models.DateTimeField(default=timezone.now) # 评论时间

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:20]