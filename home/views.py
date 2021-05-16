from django.shortcuts import render
from toys.models import Toy
from blog.models import BlogPost


def index(request):
    """ This view returns the index page """

    popular = Toy.objects.filter(rating=4)
    campaign = Toy.objects.filter(campaign=True)[:4]
    blogposts = BlogPost.objects.all()[:4]

    context = {
        'popular': popular,
        'campaign': campaign,
        'blogposts': blogposts
    }

    return render(request, 'home/index.html', context)
