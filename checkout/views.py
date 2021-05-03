from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings

from .models import Order, OrderLineItem
from .forms import OrderForm

from toys.models import Toy
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import bag_contents
from django.views.decorators.http import require_POST

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request,
                       'Your payment could not be processed.'
                       'Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()(commit=False)
            pid = request.POST.get('client_secret').split('secret')[0]
            order.stripe.pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    toy = Toy.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            toy=toy,
                            quantity=item_data
                        )
                        order_line_item.save()
                except Toy.DoesNotExist:
                    messages.error(request, 'One of the toys in your bag does'
                                   'not exist in our database. We are'
                                   'sorry for the inconvenience,'
                                   'please contact us for help.')
                    order.delete()
                    return redirect(reverse, 'view_bag')

        if not bag:
            messages.error(request, "Your bag is empty!")
            return redirect(reverse('toys'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        # Prefill order form with users saved info, if the user
        # is signed in and has saved info

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': profile.user.first_name,
                    'last_name': profile.user.last_name,
                    'email': profile.user.email,
                    'phone_number': profile.phone_number,
                    'country': profile.country,
                    'postcode': profile.postcode,
                    'town_or_city': profile.town_or_city,
                    'street_address1': profile.street_address1,
                    'street_address2': profile.street_address2,
                    'county': profile.county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        }

    return render(request, 'checkout/checkout.html', context)
