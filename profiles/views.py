from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

# Code adapted from Boutique Ado walkthrough project:
# https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/f5880efee43b3b9ea1276a09ca972f4588001c59/profiles/views.py


@login_required
def profile(request):
    """
    A view to display the users profile and update it

    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(
                request, 'Update failed.'
                'Please check that the form is valid and try again.')

    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all().order_by('-date')

    context = {
        'form': form,
        'on_profile_page': True,
        'orders': orders,
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a confirmation for a previous order with\
           order number {order_number} We sent a confirmation\
            email for this order on the date it was created.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
