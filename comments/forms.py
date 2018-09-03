from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # 表单对应的model
        fields = ['name', 'email', 'url', 'text']  # 表单需要显示的字段
