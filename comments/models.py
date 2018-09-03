from django.db import models

from blog.models import Post


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,blank=True)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

