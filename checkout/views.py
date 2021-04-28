from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings

from .models import Order, OrderLineItem

from toys.models import Toy
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents


def checkout(request):
    if request.method == 'POST':
        bag = request.session.get('bag', {})

    context = {
        'bag': bag

    }

    return render(request, 'checkout/checkout.html', context)




