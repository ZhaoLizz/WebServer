from django import template

from blog.models import Post, Category

register = template.Library()

# register 注册为模板标签,可以在html中通过{% xxx %}引用这个函数
@register.simple_tag
def get_recent_posts(num=5):
    # 获取最近发布的5篇文章
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    # 获取归档信息,根据发布的月份分类归档
    # dates返回一个列表,列表中元素为每一个Post的date时间对象
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 分类模板
    return Category.objects.all()