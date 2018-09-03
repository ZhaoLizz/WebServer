from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from blog.models import Post, Category
import markdown

# def index(request):
#     return render(request, 'blog/index.html', context={
#         'title': '我的博客首页',
#         'welcome': '欢迎访问我的博客首页'
#     })
from comments.forms import CommentForm


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    ordering = '-created_time'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_time')


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # body文本转换为markdown格式,即渲染过的HTML文本
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.increase_views() # 阅读量+1

    form = CommentForm()
    comment_list = post.comment_set.all()
    # form变量可以自动生成HTML表单的全部数据
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    """
    归档视图,根据year和month对Post进行分类
    """
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
