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
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    context = {
        'blogpost': blogpost,
    }

    return render(request, 'blog_details.html', context)


@login_required
def add_blogpost(request):
    """
    A view to add a blogpost
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'Successfully added blogpost!')
            return redirect(reverse('blog_details', args=[blogpost.id]))
        else:
            messages.error(
                request, 'Sorry, something went wrong. \
                    The blogpost was not added to the store')
    else:
        form = blogForm()

    template = 'blog/add_blogpost.html'
    context = {
        'form': form
    }

    return render(request, template, context)