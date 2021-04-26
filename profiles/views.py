from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm


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

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)
