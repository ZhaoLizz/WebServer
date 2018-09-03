from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from comments.forms import CommentForm


def post_comment(request, post_pk):

    # 首先获取被评论的文章
    post = get_object_or_404(Post, pk=post_pk)

    print('log', request.method)
    # 处理POST请求
    if request.method == 'POST':
        # request.POST是一个类字典的对象
        # 利用这些对象构造表单对象CommentForm实例
        form = CommentForm(request.POST)
        # 检查表单数据是否符合格式要求,如果符合要求就存进数据库
        if form.is_valid():
            # commit=False是利用表单的数据生成Comment模型类的实例,但还没有写到数据库
            # 这样做是为了把comment的外键对应的post填入.(POST里拿到的comment数据中并没有post对象信息
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # 重定向到post的详情页.
            # 重定向: 用户访问的是某个URL,但是这里服务器会将用户重定向到另外的URL
            # 如果传入一个模型实例对象,这个模型必须实现get_absolute_url方法,这样redirect才能根据url进行重定向
            return redirect(post)
        else:
            # 如果数据不合法,获取到当前post下的全部评论重新渲染
            comment_list = post.comment_set.all()  # 等价于Comment.objects.filter(post=post)
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    # 如果不是POST请求,说明用户没有提交数据,重定向到文章详情
    # 通过重定向,首先根据url进入blog/views.py里面的detail方法,
    return redirect(post)
