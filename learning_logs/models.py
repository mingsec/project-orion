from django.db                  import models
from django.contrib.auth.models import User

# Create your models here.
#在此处创建你的模型。

class Topic(models.Model):
    """用户学习的主题"""
    text       = models.CharField(max_length=20)
    name       = models.CharField(max_length=40)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """用户学习的主题的科目"""
    topic      = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text       = models.CharField(max_length=100)
    name       = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Blog(models.Model):
    """用户学习的主题的科目的条目"""
    entry       = models.ForeignKey(Entry, on_delete=models.CASCADE)
    owner       = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=100)
    name        = models.CharField(max_length=200)
    text        = models.TextField()
    date_added  = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
