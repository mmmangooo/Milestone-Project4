from django.shortcuts import render
from toys.models import Toy, Campaign
from blog.models import BlogPost


def index(request):
    """ This view returns the index page """

    toy = Toy.objects.all()
    campaign = Campaign.objects.all()
    blogpost = BlogPost.objects.all()

    context = {
        'toy': toy,
        'campaign': campaign,
        'blogpost': blogpost
    }

    return render(request, 'home/index.html', context)
