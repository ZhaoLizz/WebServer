from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_time','modified_time','category','author')
    list_filter = ['title','created_time']
    search_fields = ['title']  # 搜索的字段

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)