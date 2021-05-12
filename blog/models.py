from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """
    This model defines the blog posts in the db
    """
    author = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=254, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=254)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    """
    This model defines comments on blog posts in the db
    """
    post = models.ForeignKey(
        BlogPost, related_name='comments',
        null=False, blank=False, on_delete=models.CASCADE)
    author = models.CharField(max_length=254,
                              null=False, blank=False, default='Your name')
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
