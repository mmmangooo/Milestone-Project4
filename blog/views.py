from django.shortcuts import render
from .models import BlogPost, BlogComment
from .forms import BlogpostForm, BlogCommentForm
from django.db.models import Q

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required


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

    return render(request, 'blog/blog.html', context)


def blog_details(request, blogpost_id):
    """
    A view to show blogpost details with content text, and add comments to them
    """
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    comments = BlogComment.objects.all()
    new_comment = None
    comment_form = BlogCommentForm(data=request.POST)

    if request.method == 'POST':
        
        if comment_form.is_valid():
            # Creating new comment object, not saving yet
            new_comment = comment_form.save(commit=False)
            # Assigning the comment to the current blogpost
            new_comment.blogpost = blogpost
            new_comment.save()
        else:
            comment_form = BlogCommentForm()

    context = {
        'blogpost': blogpost,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_details.html', context)


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
        form = BlogpostForm(request.POST)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'Successfully added blogpost!')
            return redirect(reverse('blog_details', args=[blogpost.id]))
        else:
            messages.error(
                request, 'Sorry, something went wrong. \
                    The blogpost was not added to the store')
    else:
        form = BlogpostForm()

    template = 'blog/add_blogpost.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_blogpost(request, blogpost_id):
    """
    A view to edit a blogpost
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    if request.method == 'POST':
        form = BlogpostForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'Successfully updated blogpost!')
            return redirect(reverse('blog_details', args=[blogpost.id]))
        else:
            messages.error(
                request, 'Sorry, something went wrong. \
                    The blogpost was not updated.')
    else:
        form = BlogpostForm(instance=blogpost)
        messages.info(request, 'You are editing {blogpost.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


@login_required
def confirm_delete_blogpost(request, blogpost_id):
    """
    A view for rendering a template where deletion is confirmed or cancelled
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    context = {
        'blogpost': blogpost,
    }

    template = 'blog/confirm_delete_blog.html'

    return render(request, template, context)


@login_required
def delete_blogpost(request, blogpost_id):
    """
    Delete a blogpost
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'This functionality is only available to store owners')
        return redirect(reverse('home'))

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    blogpost.delete()
    messages.success(request, 'Blogpost successfully deleted.')
    return redirect(reverse('blog'))
