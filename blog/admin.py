from django.contrib import admin
from .models import BlogPost, BlogComment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
    )


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'content',
        'posted_date',
        'post'
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
