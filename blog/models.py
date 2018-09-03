from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)  # 对应数据库字符型数据

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()  # CharField存储小文本,TextField存储大文本
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)  # 文章摘要,可以允许为空值

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Post -m-1- Category
    tag = models.ManyToManyField(Tag, blank=True)  # Post -m-m- Tag
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # django提供User类,对应命令创建的user

    views = models.PositiveIntegerField(default=0)#阅读量

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        使用redirect重定向函数时,redirect函数自动调用Post对象的这个方法
        """
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 自定义Post的默认排序方式
    class Meta:
        ordering = ['-created_time'] #也可以ordering = ['-created_time', 'title']

    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])

