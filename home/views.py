from django.shortcuts import render
from toys.models import Toy
from blog.models import BlogPost, BlogComment


def index(request):
    """ This view returns the index page """

    toys = Toy.objects.order_by('-rating')[:3]
    has_campaigns = Toy.objects.filter(campaign=True)[:3]
    blogposts = BlogPost.objects.all().order_by('-posted_date')[:3]

    context = {
        'toys': toys,
        'blogposts': blogposts,
        'has_campaigns': has_campaigns
    }

    return render(request, 'home/index.html', context)
