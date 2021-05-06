from django.shortcuts import render
from .models import BlogPost, BlogComment
from django.db.models import Q

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def blog(request):
    """
    A view to show all blogposts and to search
    for blogposts by title or content
    """
    blogposts = BlogPost.objects.all()
    query = None

    if 'query' in request.GET:
        query = request.GET['query']
        if not query:
            messages.error(request, "No search qriteria entered")
            return redirect(reverse('blogposts'))

        queries = Q(
                title__icontains=query) | Q(content__icontains=query)
        blogposts = blogposts.filter(queries)

    context = {
        'blogposts': blogposts,
        'search_term': query,
    }

    return render(request, 'blog.html', context)


def blog_details(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, 'blogpost_id')

    context = {
        'blogpost': blogpost,
    }

    return render(request, 'blog_details.html', context)
