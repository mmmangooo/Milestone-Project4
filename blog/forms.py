from django import forms
from .models import BlogPost, BlogComment


class BlogpostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ('author', 'content')
