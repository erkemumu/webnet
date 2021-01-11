from django.db import models
import django.utils.timezone

# Create your models here.
"""
数据库
主要负责定义要存取的数据类型
"""


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
