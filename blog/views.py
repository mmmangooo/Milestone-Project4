from django.shortcuts import render
from .models import BlogPost, BlogComment

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def blog(request):
    blogpost = BlogPost.objects.all()

    context = {
        'blogpost': blogpost,
    }

    return render(request, 'blog.html', context)


def blog_details(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, 'blogpost_id')

    context = {
        'blogpost': blogpost,
    }

    return render(request, 'blog_details.html', context)
