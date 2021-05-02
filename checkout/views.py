from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings

from .models import Order, OrderLineItem
from .forms import OrderForm

from toys.models import Toy
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents


def checkout(request):
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty!")
            return redirect(reverse('toys'))

        order_form = OrderForm()
        context = {
            'order_form': order_form,
        }

        return render(request, 'checkout/checkout.html', context)
